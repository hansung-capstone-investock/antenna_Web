import datetime
from .models import *
from django.db.models import Q
import operator

def b3m():
    today = datetime.date.today() - datetime.timedelta(days=1)
    
    if today.weekday() == 5:
        today -= datetime.timedelta(days=1)
    elif today.weekday() ==6:
        today -= today-datetime.timedelta(days=2)
    
    before3m = today-datetime.timedelta(weeks=12)
    
    stocklist = StockList.objects.using('stockDB').filter(
        Q(market = 1) | Q(market =2)
    )
    
    gapdict = dict()
    codelist = dict()
    for c in stocklist:
        codelist[c.code] = c.company

    for key in codelist:
        strClass = 'StockX'+key
        try:
            instance = eval(strClass)
        except:
            continue
        
        try:
            todayInfo = instance.objects.using("stockDB").filter(
                Q(date=today) | Q(date=before3m))
            gapPrice = todayInfo[0].close-todayInfo[1].close
            gapPercent = (gapPrice/todayInfo[0].close)
            gapdict[key] = round(gapPercent*100,2)
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
    
    for i in range(len(keylist)):
        cpModel = Compare3Month.objects.using('stockDB').create(
            date = today,
            stockcode = keylist[i],
            company = codelist[keylist[i]],
            gap = vlist[i],
            rank  = i+1
        )
        cpModel.save(using='stockDB')
        i+=1