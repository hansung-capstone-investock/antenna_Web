from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
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
from datetime import datetime, timedelta, tzinfo
from bs4 import BeautifulSoup
import requests
from threading import Timer
from pykrx import stock as st
from stock import stockScraping
from stock.serializers import *
import pandas as pd
from stock import backtest
from stock import marketUpdate

def mu(request):
    marketUpdate.readMarket()
    return HttpResponse("market Update")

@api_view(['POST'])
def backtestapi(request):
    if request.method == 'POST':
        backT = backtest.Backtest(request.data)
        backT.targetStock()
        backT.backTesting()
        return HttpResponse(backT.haveStock)

@api_view(['GET'])
def kospiYearList(request):
    if request.method == 'GET':
        today = datetime.today()
        startdate = today + timedelta(days=-365)
        kospiList = Kospi.objects.using("stockDB").filter(date__range = [startdate, today])
        kospiList_serializer = KospiSerializer(kospiList,many = True)
        
        return Response(kospiList_serializer.data)

@api_view(['GET'])
def kosdaqYearList(request):
    if request.method == 'GET':
        today = datetime.today()
        startdate = today + timedelta(days=-365)
        kosdaqList = Kosdaq.objects.using("stockDB").filter(date__range = [startdate, today])
        kosdaqList_serializer = KosdaqSerializer(kosdaqList,many = True)
        return Response(kosdaqList_serializer.data)
    
@api_view(['GET'])
def kospi200YearList(request):
    if request.method == 'GET':
        today = datetime.today()
        startdate = today + timedelta(days=-365)
        kospi200List = Kospi200.objects.using("stockDB").filter(date__range = [startdate, today])
        kospi200List_serializer = Kospi200Serializer(kospi200List,many = True)
        return Response(kospi200List_serializer.data)




def insertPrice(request):
    df = pd.read_csv("./final_stock.csv", converters={'code': str},thousands = ',')

    stockList_df = df['code']
    dup_df = stockList_df.drop_duplicates()
    dup_df = dup_df.reset_index(drop=True)
    cur = "005930"
    strClass = 'StockX'+cur
    instance = eval(strClass)
    for r in df.itertuples():
        if r.code != cur:
            cur = r.code
            strClass = 'StockX'+cur
            instance = eval(strClass)
            
        stockinfo = instance(
            date = r.date,
            open = r.open,
            high = r.high,
            low = r.low,
            close = r.close,
            volume =r.vol,
        )
        stockinfo.save(using='stockDB')
    return HttpResponse("insert Done")

@api_view(['GET'])
def marketList(request):
    if request.method == 'GET':
        marketList = MarketList.objects.using("stockDB").all()
        marketList_serializer = MarketListSerializer(marketList,many = True)
        return Response(marketList_serializer.data)



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


def insert_per(request):
    stocklist_df = pd.read_excel("C:/Users/Junyong/Desktop/capstone_stockData/stockList.xlsx",dtype=str)
    stocklist = list()
    stocklist = stocklist_df['종목코드']
    # for stock in stocklist:
    #     df=pd.read_csv(f"C:/Users/Junyong/Desktop/capstone_stockData/perdata/{stock}per.csv",dtype=str)
    #     try:
    #         strClass = 'Xstock'+stock
    #         instance = eval(strClass)
    #         for 
    #     except:
    #         continue        
    stocka = stocklist[54:]
    for stockcode in stocka:
        try:
            df=pd.read_csv(f"C:/Users/Junyong/Desktop/capstone_stockData/preper/{stockcode}per.csv",dtype=str)
            strClass = 'StockX'+stockcode
            instance = eval(strClass)
            for r in df.itertuples():
                stockinfo = instance(
                    date = r.date,
                    per = r.PER,
                    pbr = r.PBR
                    )
                stockinfo.save(using='stockDB')
        except:
            continue
        
    return HttpResponse("per,pbr done")
    
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


