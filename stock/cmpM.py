import datetime
from .models import *
from django.db.models import Q
import operator

def b3m():
    today = datetime.datetime.today() - datetime.timedelta(days=1)
    
    if today.weekday() == 5:
        today-datetime.timedelta(days=1)
    elif today.weekday() ==6:
        today-datetime.timedelta(days=2)
        
    before3m = today-datetime.timedelta(weeks=12)
    
    stocklist = StockList.objects.using('stockDB').filter(
        Q(market = 1) | Q(market =2)
    )
    
    gapdict = dict()
    codelist = list()
    for c in stocklist:
        codelist.append(c.code)

    for code in codelist:
        strClass = 'StockX'+code
        try:
            instance = eval(strClass)
        except:
            continue
        
        try:
            todayInfo = instance.objects.using("stockDB").filter(
                Q(date=today) | Q(date=before3m))
            gapPrice = todayInfo[0].close-todayInfo[1].close
            gapPercent = (gapPrice/todayInfo[0].close)
            gapdict[code] = round(gapPercent*100,2)
        except:
            continue
        
    gapdict = sorted(gapdict.items(), key=lambda x: x[1], reverse=True)

    idx=0
    keylist=list()
    vlist = list()
    for t in gapdict:
        if idx == 10:
            break
        keylist.append(t[0])
        vlist.append(t[1])
        idx+=1
    
    cpModel = CompareMonth.objects.using('stockDB').create(
        date = today,
        stockcode1 = keylist[0],
        gap1 = vlist[0],
        stockcode2 = keylist[1],
        gap2 = vlist[1],
        stockcode3 = keylist[2],
        gap3 = vlist[2],
        stockcode4 = keylist[3],
        gap4 = vlist[3],
        stockcode5 = keylist[4],
        gap5 = vlist[4],
        stockcode6 = keylist[5],
        gap6 = vlist[5],
        stockcode7 = keylist[6],
        gap7 = vlist[6],
        stockcode8 = keylist[7],
        gap8 = vlist[7],
        stockcode9 = keylist[8],
        gap9 = vlist[8],
        stockcode10 = keylist[9],
        gap10 = vlist[9],
    )
    cpModel.save(using='stockDB')
    