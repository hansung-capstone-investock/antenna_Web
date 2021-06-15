from datetime import datetime, time, timedelta, date
from django.http.response import HttpResponse
from pandas.core.frame import DataFrame
from .models import *
import pandas as pd
from django.db.models import Q
from stock.serializers import *

class Backtest1:
    haveStock = dict()
    backTestLog_df = pd.DataFrame(columns=['ticker','buy_date','buy_price','sell_date','sell_price','profit'])
    gapDict = dict()
    
    def __init__(self, backTestInfo):
        self.tester = backTestInfo['id']
        self.gapDict['total'] = 0
        self.companyNum = 10
        self.start = date(int(backTestInfo['start'].split('-')[0]),int(backTestInfo['start'].split('-')[1]),int(backTestInfo['start'].split('-')[2]))
        self.end = date(int(backTestInfo['end'].split('-')[0]),int(backTestInfo['end'].split('-')[1]),int(backTestInfo['end'].split('-')[2]))
        self.targetDate = self.start
        self.strTarget = self.targetDate.strftime("%Y-%m-%d")
        #['per','pbr']
        self.sorts = list()
        
        #{'per':min,max,'pbr':min,max}
        self.condition = dict()
        
        for i in backTestInfo['conditions']:
            for key,value in i.items():
                self.condition[key] = [float(value[0]),float(value[1])]
                self.sorts.insert(value[2],key)
        
        self.sellConditionHigh = float(backTestInfo['sellCondition'][1])
        self.sellConditionLow = float(backTestInfo['sellCondition'][0])
        
        self.marketList = backTestInfo['market']
        self.sectorList = backTestInfo['sector']
        a = [1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015]
        if 1027 in self.sectorList:
            for b in a:
                self.sectorList.append(b)
        
        stockInfo = StockX000020.objects.using("stockDB").filter(
                date__range=[self.start, self.end]
            )
        self.datelist =list()
        for st in stockInfo:
            self.datelist.append(st.date)
        self.stock_df = pd.DataFrame(index= self.datelist)
        
        
        self.targetList = StockList.objects.using("stockDB").filter(
            Q(market__in = self.marketList) &
            Q(sectorcode__in = self.sectorList)
        )
        
        
    def is_weekend(self,d):
        isWeek = date(d.year,d.month,d.day)
        return isWeek.weekday() > 4
    
    def getData(self):
        self.close_df = pd.DataFrame(index = self.datelist)
        self.per_df = pd.DataFrame( index = self.datelist)
        self.pbr_df = pd.DataFrame( index = self.datelist)
        self.psr_df = pd.DataFrame( index = self.datelist)
        self.roe_df = pd.DataFrame( index = self.datelist)
        self.roa_df = pd.DataFrame( index = self.datelist)
        
        idx =0
        for ticker in self.targetList:
            strClass = 'StockX'+ticker.code
            instance = eval(strClass)
            stockInfo = instance.objects.using("stockDB").filter(
                date__range=[self.start, self.end]
            )

            close_list = list()
            date_list = list()
            per_list=list()
            pbr_list=list()
            psr_list=list()
            roe_list=list()
            roa_list=list()
            
            for dayStock in stockInfo:
                date_list.append(dayStock.date)
                close_list.append(dayStock.close)
                per_list.append(dayStock.per)
                pbr_list.append(dayStock.pbr)
                psr_list.append(dayStock.psr)
                roe_list.append(dayStock.roe)
                roa_list.append(dayStock.roa) 
                
            try:
                self.close_df[f'{ticker.code}'] = close_list
            except:
                pass
            try:
                self.per_df[f'{ticker.code}'] = per_list
            except:
                pass
            try:
                self.pbr_df[f'{ticker.code}'] = pbr_list
            except:
                pass
            try:
                self.psr_df[f'{ticker.code}'] = psr_list
            except:
                pass
            try:
                self.roe_df[f'{ticker.code}'] = roe_list
            except:
                pass
            try:
                self.roa_df[f'{ticker.code}'] = roa_list
            except:
                pass
    
    def buyingStock(self,buyStockNum):
        idx =0
        buyflag=0

        #sorting
        df = pd.DataFrame()
        df['close'] = self.close_df.loc[self.targetDate]
        df['per'] = self.per_df.loc[self.targetDate]
        df['pbr'] = self.pbr_df.loc[self.targetDate]
        df['psr'] = self.psr_df.loc[self.targetDate]
        df['roe'] = self.roe_df.loc[self.targetDate]
        df['roa'] = self.roa_df.loc[self.targetDate]
        df.to_csv("dftest.csv")
        
        for con in self.sorts:
            con1 = df[con]> self.condition[con][0]
            con2 = df[con]< self.condition[con][1]
            df =df[con1&con2]
            
        sort_daily_df = df.sort_values(by=self.sorts,ascending=True)
        sort_daily_df['ticker']=sort_daily_df.index
        sort_daily_df.reset_index(drop=True,inplace=True)
        length = sort_daily_df.shape[0]
        
        while buyflag < buyStockNum:
            if length<=idx:
                break
            if sort_daily_df.loc[idx]['ticker'] in self.haveStock:
                idx+=1
                continue
            new_data = {
                'ticker' : sort_daily_df.loc[idx]['ticker'],
                'buy_date' : self.targetDate,
                'buy_price' : sort_daily_df.loc[idx]['close']
            }
            self.haveStock[new_data["ticker"]] = [self.targetDate, new_data['buy_price']]
            buyflag +=1
        
    def sellingStock(self):
        
        if not self.haveStock:
            return 10
        
        sellingNum =0
        delStock= list()
        
        for key,value in self.haveStock.items():
            todayPrice = self.close_df.loc[self.targetDate][key]
            boughtPrice = value[1]
            gap = todayPrice - boughtPrice
            gapPercent = gap/boughtPrice*100
            
            if self.sellConditionLow < gapPercent <self.sellConditionHigh:
                continue
            sellInfo = {
                'ticker':key,
                'buy_date':value[0],
                'buy_price':value[1],
                'sell_date':self.targetDate,
                'sell_price':todayPrice,
                'profit':gapPercent
            }
            self.backTestLog_df = self.backTestLog_df.append(sellInfo,ignore_index=True)
            delStock.append(key)
            sellingNum +=1
            self.gapDict[self.strTarget]+=gapPercent
            
        for l in delStock:
            del self.haveStock[l]
        
        return sellingNum
    
    def sellingStockAll(self):
        for key,value in self.haveStock.items():
            todayPrice = self.close_df.loc[self.targetDate][key]
            boughtPrice = value[1]
            gap = todayPrice - boughtPrice
            gapPercent = gap/boughtPrice*100
            sellInfo = {
                'ticker':key,
                'buy_date':value[0],
                'buy_price':value[1],
                'sell_date':self.targetDate,
                'sell_price':todayPrice,
                'profit':gapPercent
            }
            self.backTestLog_df = self.backTestLog_df.append(sellInfo,ignore_index=True)
            self.gapDict[self.strTarget]+=gapPercent

    def dailyTesting(self):
        
        buyStockNum = 10
        self.gapDict[self.strTarget] =0
        
        if self.targetDate !=self.start:
            buyStockNum = self.sellingStock()
        
        if buyStockNum == 0:
            return

        
        #조건에 맞는 주식 구매
        self.buyingStock(buyStockNum)
        
        return True

        
    def backTesting(self):
        if len(self.targetList) == 0:
            return 
        self.getData()
        
        while self.targetDate != self.end:
            if self.targetDate not in self.datelist:
                self.targetDate += timedelta(days=1)
                continue
            
            self.strTarget = self.targetDate.strftime("%Y-%m-%d")
            
            if self.is_weekend(self.targetDate) == True:
                self.targetDate += timedelta(days=1)
                continue
                        
            if self.dailyTesting() == False:
                self.targetDate += timedelta(days=1)
                continue
            
            self.gapDict['total']+=self.gapDict[self.strTarget]
            self.targetDate += timedelta(days=1)

        while self.targetDate not in self.datelist:
            self.targetDate -= timedelta(days=1)

        self.sellingStockAll()
        self.gapDict['total']+=self.gapDict[self.strTarget]
        # self.backTestLog_df.to_csv("backtestLog.csv")
        return 100
    