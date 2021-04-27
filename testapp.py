import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
from bs4 import BeautifulSoup
import requests
import json

# https://finance.naver.com/news/news_list.nhn

url = 'https://finance.naver.com/news/news_list.nhn'

for i in range(1, 5):
    page_url = '{}&page={}'.format(url, i)
    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser",from_encoding='euc-kr')
    # articleList = soup.select("#contentarea_left > ul > li.newsList.top > dl")
    titleList = soup.select("#contentarea_left > ul > li.newsList.top > dl > .articleSubject > a")
    summaryList = soup.select("#contentarea_left > ul > li.newsList.top > dl > .articleSummary")
    linkList = soup.select("#contentarea_left > ul > li.newsList.top > dl > .articleSubject > a")
    for title, summary, link in zip(titleList, summaryList, linkList):
        link = link.attrs['href']
        links = url[0:25] + link[0:55]
        print("title= ", title.text)
        print("summary = ", summary.text.strip().split('..')[0])
        print("link = ", links)
        print("=" * 30)
    print("*" * 30)

    # for article in articleList:    
    #     title = soup.select_one(".articleSubject > a").get_text()
    #     summary = soup.select_one(".articleSummary").get_text().strip().split('..')[0]
    #     link = soup.select_one(".articleSubject > a").attrs['href']
    #     links = url[0:25] + link[0:55]
    #     print("title = ", title)
    #     print("summary = ", summary)
    #     print("links = ", links)
    

    # for article in articleList:
    #     #contentarea_left > ul > li.newsList.top > dl > dd:nth-child(2)
    #     title = article.select_one("li.newsList_top > dl > dd.articleSubject > a").get_text()
    #     summaryList = article.select_one("li.newsList_top > dl > dd.articleSummary").get_text().strip().split('..')[0]
    #     linkList = article.select_one("li.newsList_top > dl > dd.articleSubject > a")
    #     links = url
    #     links += linkList.attrs['href']

    #     print(title)
    #     print(summaryList)
    #     print(links)
    #     print('='*40)

    # print('*' * 40)

    # for article in articleList:
    #     title = article.select_one("li.newsList > dl > dd.articleSubject > a").get_text()
    #     summaryList = article.select_one("li.newsList > dl > dd.articleSummary").get_text().strip().split('..')[0]
    #     linkList = article.select_one("li.newsList > dl > dd.articleSubject > a")
    #     links = url
    #     links += linkList.attrs['href']

    #     print(title)
    #     print(summaryList)
    #     print(links)
    #     print('='*40)
    
