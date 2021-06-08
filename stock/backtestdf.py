from datetime import datetime, time, timedelta, date
from django.http.response import HttpResponse
from .models import *
import pandas as pd
from django.db.models import Q
from stock.serializers import *

class Backtest1:
    haveStock = dict()
    backTestLog_df = pd.DataFrame(columns=['ticker','buy_date','buy_price','sell_date','sell_price','profit'])
    gapDict = dict()
    
    def __init__(self, backTestInfo):
        self.gapDict['total'] = 0
        self.companyNum = 10
        self.start = date(int(backTestInfo['start'].split('-')[0]),int(backTestInfo['start'].split('-')[1]),int(backTestInfo['start'].split('-')[2]))
        self.end = date(int(backTestInfo['end'].split('-')[0]),int(backTestInfo['end'].split('-')[1]),int(backTestInfo['end'].split('-')[2]))
        self.targetDate = self.start
        self.strTarget = self.targetDate.strftime("%Y-%m-%d")
        self.sorts = list()
        self.condition = dict()
        
        self.test= backTestInfo['conditions']
        for i in self.test:
            for key,value in i.items():
                self.condition[key] = [value[0],value[1]]
                self.sorts.insert(value[2],key)
        
        self.sellConditionHigh = backTestInfo['sellCondition'][1]
        self.sellConditionLow = backTestInfo['sellCondition'][0]
        
        self.marketList = backTestInfo['market']
        self.sectorList = backTestInfo['sector']
    
    def is_weekend(self,d):
        isWeek = date(d.year,d.month,d.day)
        return isWeek.weekday() > 4
    
    def getData(self,targetList):
        for ticker in targetList:
            strClass = 'StockX'+ticker.code
            print(strClass)
            instance = eval(strClass)
            stockInfo = instance.objects.using("stockDB").filter(
                date__range=[f"{self.start}", f"{self.end}"]
            )
            stockInfo_serializer = BackTestSerializer(stockInfo)
            print(stockInfo_serializer)
            return
    def backTesting(self):
        targetList = StockList.objects.using("stockDB").filter(
            market__in = self.marketList,
            sectorcode__in = self.sectorList
        )
        self.getData(targetList)
            
        