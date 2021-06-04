import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
from bs4 import BeautifulSoup
import requests
from kiwipiepy import Kiwi, Option

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
test = {}
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
                # dcData(title=data, count=wordCounts[data]).save()
                test[data] = wordCounts[data]
                # print(type(test))
# print(test.keys())
# print(test.values())
# for i in test.keys():
#     print(i)
for i, j in zip(test.keys(), test.values()):
    print(i)
    print(j)
    # print(i.keys())
    # print(i.values())