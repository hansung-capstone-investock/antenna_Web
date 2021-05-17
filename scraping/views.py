from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
from bs4 import BeautifulSoup
import requests
import json
from kiwipiepy import Kiwi, Option
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scraping.serializers import *


# dcinside 주식갤러리 크롤링
def parse_dc(request):
    url = 'https://gall.dcinside.com/board/lists/?id=neostock'
    # &page=1
    # 전체 페이지 읽어오기
    df = pd.DataFrame()
    for page in range(1, int(50)+1):
        page_url = '{}&page={}'.format(url, page)
        response_page = requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text
        df = df.append(pd.read_html(response_page)[0])
    df = df.dropna()
    df = df.drop_duplicates()

    kiwi = Kiwi()
    kiwi.prepare()
    temp = {}
    data = {}
    wordCounts = {}
    i = 0
    for nouns in df['제목']:
        noun = kiwi.analyze(nouns)
        temp = noun
        # 명사만 저장
        if (temp[0][0][0][1] == "NNG") or (temp[0][0][0][1] == "NNP") or (temp[0][0][0][1] == "NNB") or (temp[0][0][0][1] == "NR") or (temp[0][0][0][1] == "NP"):
                if len(temp[0][0][0][0]) != 1:  # 한글자 단어 제거
                    data = temp[0][0][0][0]
                    if data not in wordCounts:
                        wordCounts[data] = 0
                    wordCounts[data] += 1
                    dcData(title=data, count=wordCounts[data]).save()
    return HttpResponse("dc 크롤링 성공")

# 에펨코리아 주식게시판 크롤링
# 테스트 자주하면 사이트에서 막음
def parse_fmkor(request):
    url = 'https://www.fmkorea.com/index.php?mid=stock'
    # &page=1
    # 전체 페이지 읽어오기
    df = pd.DataFrame()
    for page in range(1, int(50)+1):
        page_url = '{}&page={}'.format(url, page)
        response_page = requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text
        df = df.append(pd.read_html(response_page)[0])
    df = df.dropna()
    df = df.drop_duplicates()

    kiwi = Kiwi()
    kiwi.prepare()
    temp = {}
    data = {}
    wordCounts = {}
    i = 0
    for nouns in df['제목']:
        noun = kiwi.analyze(nouns)
        temp = noun
        # 명사만 저장
        if (temp[0][0][0][1] == "NNG") or (temp[0][0][0][1] == "NNP") or (temp[0][0][0][1] == "NNB") or (temp[0][0][0][1] == "NR") or (temp[0][0][0][1] == "NP"):
                if len(temp[0][0][0][0]) != 1:  # 한글자 단어 제거
                    data = temp[0][0][0][0]
                    if data not in wordCounts:
                        wordCounts[data] = 0
                    wordCounts[data] += 1
                    fmkorData(title=data, count=wordCounts[data]).save()

    return HttpResponse("fmkor 크롤링 성공")

# KRX로부터 상장기업 목록 파일을 읽어옴
def company_list(request):
    url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
    krx = pd.read_html(url, header=0)[0]
    krx = krx[['종목코드', '회사명']]
    krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'})
    krx.code = krx.code.map('{:06d}'.format)

    for i, j in zip(krx['code'], krx['company']):
        companyData(code=i, name=j).save()
    return HttpResponse('krx')

#네이버 증권 주요 뉴스 스크래핑
def crawlerNews(request):
    BASE_URL = 'https://finance.naver.com/'
    
    now = dt.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    nowTime = now.strftime('%H:%M:%S').split(':')[0]
    
    url = BASE_URL+"news/mainnews.nhn?date="+str(nowDate)
    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser",from_encoding='euc-kr')
    articleList = soup.select("#contentarea_left > div.mainNewsList > ul > li > dl")

    # 기사를 매시각 정각마다 1시간씩 받아오도록 반복문 설정
    title_list=[]
    
    for article in articleList:
        articleTime = article.select_one(".articleSummary > .wdate").get_text()
        # articleHour = int(articleTime.split(' ')[1].split(':')[0]) 
        # if articleHour <  int(nowTime)-1:
        #     break
        title = article.select_one(".articleSubject > a").get_text()
        summaryList = article.select_one(".articleSummary").get_text().strip().split('..')[0]
        linkList = article.select_one(".articleSubject > a")
        links = url
        links += linkList.attrs['href']
        mainnews = MainNews(
            title = title,
            summary= summaryList,
            link = links,
            publishDay = nowDate
        )
        title_list = title
        mainnews.save()

    return HttpResponse(title_list)

def liveNews(request):
    url = 'https://finance.naver.com/news/news_list.nhn?&page='

    for i in range(1, 5):
        page_url = url + str(i)
        res = req.urlopen(page_url)
        soup = BeautifulSoup(res,"html.parser",from_encoding='euc-kr')
        
        # newsList top
        titleList = soup.select("#contentarea_left > ul > li.newsList.top > dl > .articleSubject > a")
        summaryList = soup.select("#contentarea_left > ul > li.newsList.top > dl > .articleSummary")
        linkList = soup.select("#contentarea_left > ul > li.newsList.top > dl > .articleSubject > a")
        dateList = soup.select("#contentarea_left > ul > li.newsList.top > dl > .articleSummary > .wdate")
        for title, summary, link, date in zip(titleList, summaryList, linkList, dateList):
            link = link.attrs['href']
            links = url[0:25] + link[0:55]
            title = title.text
            summary = summary.text.strip().split('..')[0]
            date = date.text
            LiveNews(
                title = title,
                summary = summary,
                link = links,
                publishDate = date
            ).save()

        # newsList bottom
        titleList = soup.select("#contentarea_left > ul > li:nth-of-type(2) > dl > .articleSubject > a")
        summaryList = soup.select("#contentarea_left > ul > li:nth-of-type(2) > dl > .articleSummary")
        linkList = soup.select("#contentarea_left > ul > li:nth-of-type(2) > dl > .articleSubject > a")
        dateList = soup.select("#contentarea_left > ul > li:nth-of-type(2) > dl > .articleSummary > .wdate")
        for title, summary, link, date in zip(titleList, summaryList, linkList, dateList):
            link = link.attrs['href']
            links = url[0:25] + link[0:55]
            title = title.text
            summary = summary.text.strip().split('..')[0]
            date = date.text
            LiveNews(
                title = title,
                summary = summary,
                link = links,
                publishDate = date
            ).save()

    return HttpResponse("실시간 뉴스 크롤링 성공")

@api_view(['GET', 'POST'])
def mainnews_list(request):
    if request.method == 'GET':
        news = MainNews.objects.all()
        news_serializer = MainNewsSerializer(news, many=True)
        return Response(news_serializer.data)

    elif request.method == 'POST':
        news_serializer = MainNewsSerializer(data=request.data)
        if news_serializer.is_valid():
            news_serializer.save()
            return Response(news_serializer.data, status=status.HTTP_201_CREATED)
        return Response(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def livenews_list(request):
    if request.method == 'GET':
        livenews = LiveNews.objects.all()
        livenews_serializer = LiveNewsSerializer(livenews, many=True)
        return Response(livenews_serializer.data)

    elif request.method == 'POST':
        livenews_serializer = LiveNewsSerializer(data=request.data)
        if livenews_serializer.is_valid():
            livenews_serializer.save()
            return Response(livenews_serializer.data, status=status.HTTP_201_CREATED)
        return Response(livenews_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def dc_list(request):
    if request.method == 'GET':
        dc = dcData.objects.all()
        dc_serializer = DcSerializer(dc, many=True)
        return Response(dc_serializer.data)

    elif request.method == 'POST':
        dc_serializer = DcSerializer(data=request.data)
        if dc_serializer.is_valid():
            dc_serializer.save()
            return Response(dc_serializer.data, status=status.HTTP_201_CREATED)
        return Response(dc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def fmkor_list(request):
    if request.method == 'GET':
        fmkor = fmkorData.objects.all()
        fmkor_serializer = FmkorSerializer(fmkor, many=True)
        return Response(fmkor_serializer.data)

    elif request.method == 'POST':
        fmkor_serializer = FmkorSerializer(data=request.data)
        if fmkor_serializer.is_valid():
            fmkor_serializer.save()
            return Response(fmkor_serializer.data, status=status.HTTP_201_CREATED)
        return Response(fmkor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
