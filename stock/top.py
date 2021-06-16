from datetime import datetime,date 
from .models import *
from django.db.models import Q
import operator
import math

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
    
    codelist = dict()
    for c in stocklist:
        codelist[c.code] = c.company
        
    indexCap = dict()
    indexPrice =dict()

    for key in codelist:
        strClass = 'StockX'+key
        try:
            instance = eval(strClass)
        except:
            continue

        Query=instance.objects.using("stockDB").order_by('-date')
        todayQ = Query[0]
        today = Query[0].date
        yesterQ = Query[1]
        gapPrice = todayQ.close - yesterQ.close
        gapPercent = (gapPrice/yesterQ.close)*100
        if not -30 < gapPercent < 30:
            continue
        indexPrice[key] = [gapPercent,todayQ.close]
        if todayQ.cap == 0 or todayQ.cap is None:
            continue
        indexCap[key] = [todayQ.cap,gapPercent,todayQ.close]
    
    
    capDict = sorted(indexCap.items(), key=lambda x: x[1][0], reverse=True)
    priceDict = sorted(indexPrice.items(), key=lambda x: x[1][0],reverse=True)
    
    idx =1
    for t in priceDict:
        if idx == 6:
            break
        tspModel = TopStockPrice.objects.using('stockDB').create(
            date = today,
            stockcode = t[0],
            company = codelist[t[0]],
            rank = idx,
            todayPrice = t[1][1],
            gap = t[1][0],
        )
        tspModel.save(using='stockDB')
        idx+=1
    
    idx =1
    for t in capDict:
        if idx == 6:
            break
        tscModel = TopStockCap.objects.using('stockDB').create(
            date = today,
            stockcode = t[0],
            company = codelist[t[0]],
            rank = idx,
            todayPrice = t[1][2],
            gap = t[1][1]
        )
        tscModel.save(using='stockDB')
        idx+=1
        
