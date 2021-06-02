import pandas as pd
import datetime
from pykrx import stock as st
from .models import *

def readMarket():
    markets = {'Kospi':'1001','Kosdaq':'2001','Kospi200':'1028'} # 코스피, 코스닥, 코스피200
    today = datetime.datetime.today().strftime('%Y%m%d')
    for key in markets:
        df = st.get_index_ohlcv_by_date("20080101", today, f'{markets[key]}')
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