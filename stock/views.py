from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import *
import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
import requests
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, tzinfo
from bs4 import BeautifulSoup
import requests
from threading import Timer
from pykrx import stock as st
from stock import stockScraping
from stock.serializers import *

def initApp(request):
    stockScraping.initSet()
    return HttpResponse("App initial table setting")

def setMarket(request):
    kospiTickers = st.get_market_ticker_list("20210523", market="KOSPI")
    kosdaqTickers = st.get_market_ticker_list("20210523", market="KOSDAQ")
    konexTickers = st.get_market_ticker_list("20210523", market="KONEX")

    for ticker in kospiTickers:
        try:
            company = StockList.objects.using("stockDB").get(code = ticker)
            marketFK = MarketList.objects.using("stockDB").get(market="kospi")
            company.market = marketFK
            company.save(using='stockDB')
        except:
            continue
        
    for ticker in kosdaqTickers:
        try:
            company = StockList.objects.using("stockDB").get(code = ticker)
            marketFK = MarketList.objects.using("stockDB").get(market="kosdaq")
            company.market = marketFK
            company.save(using='stockDB')
        except:
            continue

    for ticker in konexTickers:
        try:
            company = StockList.objects.using("stockDB").get(code = ticker)
            marketFK = MarketList.objects.using("stockDB").get(market="konex")
            company.market = marketFK
            company.save(using='stockDB')
        except:
            continue
    return HttpResponse("done")

def read_naver(request):
    pages_to_fetch =100
    codes = dict()
    codes = StockList.objects.values('code','company')
    
    stockList_df = pd.DataFrame(codes)
    # update_daily_price
    for code in stockList_df.code:
        url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
        
        html = BeautifulSoup(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
        pgrr = html.find("td", class_="pgRR")
        lastpage =1
        if pgrr is None:
            lastpage = 1
        else:
            s = str(pgrr.a["href"]).split('=')
            lastpage = s[-1]
        df = pd.DataFrame()
        pages = min(int(lastpage), pages_to_fetch)
        for page in range(1, pages + 1):
            pg_url = '{}&page={}'.format(url, page)
            df = df.append(pd.read_html(requests.get(pg_url,
                                                    headers={'User-agent': 'Mozilla/5.0'}).text)[0])
            tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
        df = df.rename(columns={'날짜': 'date', '종가': 'close', 
                                '전일비': 'diff', '시가': 'open', '고가': 'high', 
                                '저가': 'low', '거래량': 'volume'})
        df['date'] = df['date'].replace('.', '-')
        
        df = df.dropna()
        df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close',
                                                                'diff', 'open', 'high', 'low',
                                                                'volume']].astype(int)
        df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]

        codeFK = StockList.objects.get(code=code)
        for r in df.itertuples():
            strDate = r.date[:4]+'-'+r.date[5:7]+'-'+r.date[8:]
            ## 주식 모델 변경( 이름 코드 확인)
            strClass = 'Xstock'+code
            instance = eval(strClass)
            stockinfo = instance(
                code = codeFK,
                date = strDate,
                open = r.open,
                high = r.high,
                low = r.low,
                close = r.close,
                diff = r.diff,
                volume =r.volume,
            )

            stockinfo.save(using='stockDB')
    return HttpResponse('finish')


@api_view(['POST'])
def backtesting_api(request):
    if request.method == 'POST':
        # 입력조건
        request.data['운용자금']
        request.data['운용기간 시작']
        request.data['운용기간 끝']
        request.data['시장']
        # kospi, kosdaq
        request.data['업종']
        # "업종" : ["it", "철강", "석유"]
        max = request.data['최대 종목 보유수']

        # 매수조건 / 우선순위
        request.data['체크박스']
        
        주가데이터 = stockData.objects.filter(date__range = ["운용기간 시작", "운용기간 끝"],
                                            date__day = "01"
        ) & 지표데이터.objects.filter(per__range = ["1", "10"], pbr__range = ["0.3", "1"]
        ) & stockList.objects.filter(시장 = "kospi"
        ) & sectorList.objects.filter(업종 = ["화학", "기계", "의약품"]
        ).order_by('date_joined')[:max]
        # 오름차순


        주가데이터_serializer = 주가Serializer(주가데이터, many=True)
        # id = 주가데이터_serializer.data[0]['id']

        # 수익률 계산

        # 3월 시작이라면, 3월01일 가격과 4월01의 가격을 비교
        # 수익률을 각 종목마다 딕셔너리 형태로 저장

        return JsonResponse(주가데이터_serializer)


@api_view(['POST'])
def tensorflow_api(request):
    if request.method == 'POST':
        # 입력조건
        종목 = request.data['종목']
        예측날짜 = request.data['예측날짜']
        # 7일, 15일, 30일

        request.data['모델']
        # RNN, LSTM, GRU

        request.data['지표 체크박스']
        
        종목데이터 = stockList.objects.get(종목명 = 종목)

        종목데이터_serializer = 주가Serializer(종목데이터, many=True)
        code = 종목데이터_serializer.data[0]['code']

        result = tensorflow(code, 예측날짜)
        # 이미지 파일로 받아서

        return HttpResponse(result, content="image/png")
