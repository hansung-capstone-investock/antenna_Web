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


def read_naver(request):
    pages_to_fetch =1
    codes = dict()
    codes = StockList.objects.values('code','company')
    
    stockList_df = pd.DataFrame(codes)
    # update_daily_price
    for code in stockList_df.code:
        #read_naver
        
        url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
        
        html = BeautifulSoup(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
        pgrr = html.find("td", class_="pgRR")
        if pgrr is None:
            return HttpResponse(f"pgrr is None = {code}")
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
        df.to_excel('stock.xlsx')
        df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close',
                                                                'diff', 'open', 'high', 'low',
                                                                'volume']].astype(int)
        df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]

        codeFK = StockList.objects.get(code=code)
        for r in df.itertuples():
            strDate = r.date[:4]+'-'+r.date[5:7]+'-'+r.date[8:]
            stockinfo = StockInfo(
                code = codeFK,
                date = strDate,
                open = r.open,
                high = r.high,
                low = r.low,
                close = r.close,
                diff = r.diff,
                volume =r.volume
            )
            stockinfo.save()
    return HttpResponse('finish')

