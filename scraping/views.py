from django.shortcuts import render
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from kiwipiepy import Kiwi, Option
from django.http import HttpResponse
from .models import dcData, fmkorData
from wordcloud import WordCloud

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
    wc = WordCloud(
    font_path='NanumGothic.ttf',
    background_color='white',
    )
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
                    dcData(title=data).save()

    wcImg = wc.generate_from_frequencies(wordCounts)
    wcImg.to_file('wordcloud_dc.jpg')
    return HttpResponse(wcImg, content_type="image/jpeg")

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
    wc = WordCloud(
    font_path='NanumGothic.ttf',
    background_color='white',
    )
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
                    dcData(title=data).save()

    wcImg = wc.generate_from_frequencies(wordCounts)
    wcImg.to_file('wordcloud_fmkor.jpg')
    return HttpResponse(wcImg, content_type="image/jpeg")
    