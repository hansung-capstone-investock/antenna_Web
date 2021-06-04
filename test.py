import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from kiwipiepy import Kiwi, Option

code = int("000020")
code = '{0:06d}'.format(code)

nowDate = (datetime.now()-timedelta(1)).strftime('%Y-%m-%d')
exeStr = 'StockX{0}.objects.filter(date__range=["2018-01-01", "{1}"]'.format(code, nowDate)
exec(exeStr)