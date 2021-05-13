from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib, calendar, time, json
import urllib.request
from threading import Timer
from pykrx import stock as st
from . import *

# Create your views here.
@api_view(['GET'])
def read_krx_code(request):
    url='http://kind.krx.co.kr/corpgeneral/corpList.do?method=' \
        'download&searchType=13'
    krx = pd.read_html(url, header=0)[0]
    krx = krx[['종목코드', '회사명']]
    krx = krx.rename(columns={'종목코드':'code', '회사명':'company'})
    krx.code = krx.code.map('{:06d}'.format)
    today = datetime.today().strftime('%Y-%m-%d')
    
    for idx in range(len(krx)):
        code = krx.code.values[idx]
        company = krx.company.values[idx]
        stocklist = StockList(
            code = code,
            company = company,
            last_update = today
        )
        stocklist.save()
        tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
    return HttpResponse('krx')

def read_krx_sector(request):
    kospiTickers = st.get_index_ticker_list()
    kosdaqTickers = st.get_index_ticker_list(market='KOSDAQ')
    tickers = kospiTickers + kosdaqTickers
    themes =dict()
    for ticker in tickers:
        if int(ticker)<1005 or int(ticker) >2160:
            continue
        if 1027< int(ticker) <2015:
            continue
        sectorName = st.get_index_ticker_name(ticker)
        themes[ticker] = st.get_index_portfolio_deposit_file(ticker)
        sectorlist = SectorList(
            sectorcode = ticker,
            sector = sectorName
        )
        sectorlist.save()

    for key, value in themes.items():
        for code in value:
            stock_instance = StockList.objects.get(code = code)
            sector_instance = SectorList.objects.get(sectorcode=key)
            stock_instance.sectorcode = sector_instance
            stock_instance.save()
            
    return HttpResponse("sector code update!")

def read_thema(request):
    url = "https://finance.naver.com/sise/theme.nhn"
    html = BeautifulSoup(requests.get(url,
                                        headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
    pgrr = html.find("td", class_="pgRR")
    s = str(pgrr.a["href"]).split('=')
    lastpage = s[-1]
    pages = int(lastpage)
    
    themaLinkList = dict()  #테마이름 : 테마번호
    
    for page in range(1,pages+1):
        themaUrlPage = f"https://finance.naver.com/sise/theme.nhn?&page={page}"
        html = BeautifulSoup(requests.get(themaUrlPage,
                                            headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
        themaUrls= html.find_all("td",class_="col_type1")
        for themaUrl in themaUrls:
            themanum = str(themaUrl.a["href"].split('=')[-1])
            themaName = themaUrl.text
            themaLinkList[themaName] = themanum
            themalist = ThemaList(
                themacode = themanum,
                thema = themaName
            )
            themalist.save()
        
    # 테마이름 : 테마번호
    df = pd.DataFrame(columns=['stock','thema'])
    for key, value in themaLinkList.items():
        theurl = f"https://finance.naver.com/sise/sise_group_detail.nhn?type=theme&no={value}"
        html = BeautifulSoup(requests.get(theurl,
                                            headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
        themaNames = html.find_all("div", class_="name_area")
        for name in themaNames:
            code = str(name.a["href"].split('=')[-1])
            stock_instance = StockList.objects.get(code = code)
            thema_instance = ThemaList.objects.get(themacode = value)
            stock_instance.themacode = thema_instance
            stock_instance.save()
            
    return HttpResponse("finish themalist")

def read_naver(request):
    pages_to_fetch =100
    codes = dict()
    codes = StockList.objects.values('code','company')
    
    stockList_df = pd.DataFrame(codes)
    # update_daily_price
    idx =0
    for code in stockList_df.code:
        #read_naver
        idx+=1
        if idx<333:
            continue
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

            stockinfo.save()
    return HttpResponse('finish')


def read_market(request):
    markets = {'KOSPI':'1001','KOSDAQ':'2001','KOSPI200':'1028'} # 코스피, 코스닥, 코스피200
    for key in markets:
        df = st.get_index_ohlcv_by_date("20210501", "20210505", f'{markets[key]}')
        df = df.rename(columns={'날짜': 'date', '고가': 'high', '저가': 'low',
                                '종가': 'close',  '거래량': 'tradingVolume',
                                '거래대금': 'tradingPrice'})
        df = df.dropna()
        
        marketFK = MarketList.objects.get(market=key)
        for r in df.itertuples():
            marketinfo = MarketList(
                market=marketFK,
                date = r.date,
                high = r.high,
                low = r.low,
                close = r.close,
                tradingVolume = r.tradingVolume,
                tradingPrice = r.tradingPrice
            )
            marketinfo.save()
    
    return HttpResponse('readMarket')

