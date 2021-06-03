from .models import *
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from django.utils import timezone
from pykrx import stock as st
from datetime import date

def is_weekend():
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    d = date(year,month,day)
    return d.weekday() > 4

def getDailyMarketIndex():
    if is_weekend() is True:
        return
    url = "https://kr.investing.com/indices/south-korea-indices"
    html = BeautifulSoup(requests.get(url,
                                    headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
    field = [2, 5, 6, 7]
    # kospi , kosdaq, kospi200
    marketid = {'kospi':'pair_37426','kosdaq':'pair_38016','kospi200':'pair_37427'}

    for key, value in marketid.items():
        marketSoup = html.find('tr',{'id':f'{value}'})
        taglist=list()
        idx =0
        # 지수, 등락폭, 등락폭 퍼센트, 시간
        for tag in marketSoup:
            if idx in field:
                taglist.append(tag.text)
            idx+=1
        marketFK = MarketList.objects.using('stockDB').get(market = key)

        dtobj = datetime.strptime(taglist[3],'%H:%M:%S')
        dtobj = dtobj.replace(year=timezone.now().year,month=timezone.now().month,day=timezone.now().day)

        taglist[0] =float(taglist[0].replace(',',''))

        instance = dailyMarketIndex.objects.using('stockDB').create(
            market = marketFK,
            date = dtobj,
            changeNum = taglist[1],
            changePer = taglist[2],
            index = taglist[0],
            )
        instance.save(using='stockDB')

def clearDailyMarket():
    if is_weekend() is True:
        return
    dailyMarketIndex.objects.using('stockDB').all().delete()
    
def readMarket():
    if is_weekend() is True:
        return
    markets = {'Kospi':'1001','Kosdaq':'2001','Kospi200':'1028'} # 코스피, 코스닥, 코스피200
    today = datetime.today().strftime('%Y%m%d')
    for key in markets:
        df = st.get_index_ohlcv_by_date(today, today, f'{markets[key]}')
        df['날짜'] = df.index
        df = df.rename(columns={'날짜': 'date', '고가': 'high', '저가': 'low',
                                '종가': 'close',  '거래량': 'tradingVolume',
                                '거래대금': 'tradingPrice'})
        df = df.dropna()
        
        marketClass = str(key)
        instance = eval(marketClass)
        for r in df.itertuples():
            marketinfo = instance(
                date = r.date,
                high = r.high,
                low = r.low,
                close = r.close,
                tradingVolume = r.tradingVolume,
                tradingPrice = r.tradingPrice
            )
            marketinfo.save(using='stockDB')
