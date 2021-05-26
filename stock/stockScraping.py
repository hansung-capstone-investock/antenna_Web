from .models import *
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd
from pykrx import stock as st

def initSet():
    ###
    # table stocklist 종목 코드 저장
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
        stocklist.save(using='stockDB')
        tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    ###
    # sector 저장
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
        sectorlist.save(using='stockDB')

    for key, value in themes.items():
        for code in value:
            stock_instance = StockList.objects.using('stockDB').get(code = code)
            sector_instance = SectorList.objects.using('stockDB').get(sectorcode=key)
            stock_instance.sectorcode = sector_instance
            stock_instance.save(using='stockDB')
    
    ###
    # 테마 저장
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
            themalist.save(using='stockDB')

    for key, value in themaLinkList.items():
        theurl = f"https://finance.naver.com/sise/sise_group_detail.nhn?type=theme&no={value}"
        html = BeautifulSoup(requests.get(theurl,
                                            headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
        themaNames = html.find_all("div", class_="name_area")
        for name in themaNames:
            code = str(name.a["href"].split('=')[-1])
            stock_instance = StockList.objects.using('stockDB').get(code = code)
            thema_instance = ThemaList.objects.using('stockDB').get(themacode = value)
            stock_instance.themacode = thema_instance
            stock_instance.save(using='stockDB')

    ###
    # 주식 market 분류
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
