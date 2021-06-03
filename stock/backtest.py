from datetime import datetime, time, timedelta, date
from .models import *
import pandas as pd
from django.db.models import Q

class Backtest:
    maxStock = 10
    haveStock = list()
    stock_df = pd.DataFrame(columns=['ticker','buy_date','sell_date'])
    
    def __init__(self, backTestInfo):
        self.companyNum = 10
        self.sectorList = backTestInfo['sector']
        self.start = datetime.strptime(backTestInfo['start'], "%Y-%m-%d")
        self.end = datetime.strptime(backTestInfo['end'], "%Y-%m-%d")
        self.targetDate = self.start
        self.sorts = backTestInfo['sort']
        
        self.condition = dict()
        for i in self.sorts:
            self.condition[i] = [backTestInfo[f'{i}Min'],backTestInfo[f'{i}Max']]
        
        self.buyCondition = backTestInfo['buyCondition']
        self.sellCondition = backTestInfo['sellCondition']
        
        self.marketList = backTestInfo['market']
        self.sectorList = backTestInfo['sector']
        
    def targetStock(self):
        self.stockList = StockList.objects.using("stockDB").filter(
            market__in = self.marketList,
            sectorcode__in = self.sectorList
        )
    
    def is_weekend(d):
        isWeek = date(d.year,d.month,d.day)
        return isWeek.weekday() > 4
    
    def sellingStock(self):
        pass
    
    def dailyTesting(self,targetList):
        
        buyStockNum = 10
        if self.targetDate != self.start:
            self.sellingStock()
        
        if buyStockNum == 0:
            return
        
        df = pd.DataFrame(columns=['ticker','close','per','pbr','psr'])
        for ticker in targetList.code:
            strClass = 'xstock_'+ticker
            instance = eval(strClass)
            dateInfo = instance.objects.using("stockDB").get(date==self.targetDate)
            df = df.append(dateInfo,ignore_index=True)
            df.to_csv("testdf.csv")
            break
        df.sort_values(self.sorts,ascending=True)
        
                
    
    def backTesting(self):
        targetList = StockList.objects.using("stockDB").filter(
            Q(sectorcode__in = self.sectorList) & Q(market__in = self.marketList)
        )
        while self.targetDate != self.end:
            self.dailyTesting(targetList)
            
            self.targetDate += timedelta(days=1)
            break
