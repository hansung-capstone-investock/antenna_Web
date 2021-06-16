from datetime import datetime,date 
from .models import *
from django.db.models import Q
import operator

def is_weekend():
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    d = date(year,month,day)
    return d.weekday() > 4

def getTopStock():
    if is_weekend() is True:
        return
    
    today = datetime.today()
    stocklist = StockList.objects.using('stockDB').all()
    
    codelist = list()
    for c in stocklist:
        codelist.append(c.code)
    indexCap = dict()
    indexPrice =dict()
    for code in codelist:
        strClass = 'StockX'+code
        try:
            instance = eval(strClass)
        except:
            continue
        
        Query=instance.objects.using("stockDB").order_by('-date')
        todayQ = Query[0]
        yQuery = Query[1]
        indexCap[code] = todayQ.cap
        indexPrice[code] = [todayQ.close,yQuery.close]
    
    