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
from django.db.models import Count


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

    dcData.truncate()

    kiwi = Kiwi()
    kiwi.prepare()
    temp = {}
    data = {}
    wordCounts = {}
    res = {}
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
                    res[data] = wordCounts[data]
    for i, j in zip(res.keys(), res.values()):
        dcData(title=i, count=j).save()
    return HttpResponse("dc 크롤링 성공")

# 에펨코리아 주식게시판 크롤링
# 테스트 자주하면 사이트에서 막음
# def parse_fmkor(request):
#     url = 'https://www.fmkorea.com/index.php?mid=stock'
#     # &page=1
#     # 전체 페이지 읽어오기
#     df = pd.DataFrame()
#     for page in range(1, int(50)+1):
#         page_url = '{}&page={}'.format(url, page)
#         response_page = requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text
#         df = df.append(pd.read_html(response_page)[0])
#     df = df.dropna()
#     df = df.drop_duplicates()

#     fmkorData.truncate()

#     kiwi = Kiwi()
#     kiwi.prepare()
#     temp = {}
#     data = {}
#     wordCounts = {}
#     res = {}
#     i = 0
#     for nouns in df['제목']:
#         noun = kiwi.analyze(nouns)
#         temp = noun
#         # 명사만 저장
#         if (temp[0][0][0][1] == "NNG") or (temp[0][0][0][1] == "NNP") or (temp[0][0][0][1] == "NNB") or (temp[0][0][0][1] == "NR") or (temp[0][0][0][1] == "NP"):
#                 if len(temp[0][0][0][0]) != 1:  # 한글자 단어 제거
#                     data = temp[0][0][0][0]
#                     if data not in wordCounts:
#                         wordCounts[data] = 0
#                     wordCounts[data] += 1
#                     res[data] = wordCounts[data]
#     for i, j in zip(res.keys(), res.values()):
#         fmkorData(title=i, count=j).save()
#     return HttpResponse("fmkor 크롤링 성공")

#네이버 증권 주요 뉴스 스크래핑
def crawlerNews(request):
    MainNews.truncate()

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
        link = url[0:25] + links[59:]
        
        mainnews = MainNews(
            title = title,
            summary= summaryList,
            link = link,
            publishDay = nowDate
        )
        mainnews.save()

    return HttpResponse("메인뉴스 크롤링")

def liveNews(request):
    LiveNews.truncate()
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

@api_view(['GET'])
def mainnews_list(request):
    if request.method == 'GET':
        news = MainNews.objects.all()
        news_serializer = MainNewsSerializer(news, many=True)
        return Response(news_serializer.data)

@api_view(['GET'])
def livenews_list(request):
    if request.method == 'GET':
        livenews = LiveNews.objects.all()
        livenews_serializer = LiveNewsSerializer(livenews, many=True)
        return Response(livenews_serializer.data)

@api_view(['GET'])
def dc_list(request):
    if request.method == 'GET':
        dc = dcData.objects.all().order_by('-count')
        dc_serializer = DcSerializer(dc, many=True)
        return Response(dc_serializer.data)


@api_view(['GET'])
def fmkor_list(request):
    if request.method == 'GET':
        fmkor = fmkorData.objects.order_by('-count').all().annotate(Count('title'))
        # fmkor = fmkorData.objects.order_by('-count').values('count').annotate(Count('count'))
        fmkor_serializer = FmkorSerializer(fmkor, many=True)
        return Response(fmkor_serializer.data)