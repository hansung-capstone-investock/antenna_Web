from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from rest_framework.views import APIView
from datetime import datetime, timedelta
from .models import *
from scraping.models import *
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
from scraping.serializers import *
import pandas as pd
from stock import backtest
from stock import backtestdf
from stock import marketUpdate

import time

def mu(request):
    marketUpdate.readMarket()
    return HttpResponse("market Update")

@api_view(['POST'])
def backtestapi(request):
    if request.method == 'POST':
        backT = backtestdf.Backtest(request.data)
        a = backT.backTesting()
        
        return HttpResponse(a)

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
def stockSearchData(request):
    if request.method == 'POST':
        companyCode = request.data['companyCode']
        nowDate = (datetime.now()-timedelta(1)).strftime('%Y-%m-%d')
        exeStr = 'StockX{0}.objects.using("stockDB").filter(date__range=["2020-01-01", "{1}"])'.format(companyCode, nowDate)
        stockData = eval(exeStr)
        stockData_serializer = StockSeirializer(stockData, many=True)

        stockName = StockList.objects.using("stockDB").filter(code = companyCode)
        stockName_serializer = StockListSerializer(stockName, many=True)
        companyName = stockName_serializer.data[0]['company']

        newsData = MainNews.objects.filter(summary__contains=companyName)
        news_serializer = MainNewsSerializer(newsData, many=True)

        res_dict = dict()
        
        res_dict['stockData'] = stockData_serializer.data
        res_dict['newsData'] = news_serializer.data
        
        res_json = json.dumps(res_dict, ensure_ascii=False)

        return HttpResponse(res_json)