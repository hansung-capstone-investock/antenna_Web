from datetime import datetime, time, timedelta, date
from django.http.response import HttpResponse
from .models import *
import pandas as pd
from django.db.models import Q
from stock.serializers import *

class Backtest:
    haveStock = dict()
    backTestLog_df = pd.DataFrame(columns=['ticker','buy_date','buy_price','sell_date','sell_price','profit'])
    gapDict = dict()
    
    def __init__(self, backTestInfo):
        self.gapDict['total'] = 0
        self.companyNum = 10
        self.start = datetime.strptime(backTestInfo['start'], "%Y-%m-%d")
        self.end = datetime.strptime(backTestInfo['end'], "%Y-%m-%d")
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
    
    # 매도 조건에 맞는 주식 판매
    def sellingStock(self,dailyAll_df):
        if not self.haveStock:
            return 10
        # key = ticker, value = 산 가격
        sellingNum =0
        delStock= list()
        for key,value in self.haveStock.items():
            todayRow = dailyAll_df['ticker'] == key
            
            todayPrice = dailyAll_df[todayRow]['close']
            todayPrice = todayPrice.tolist()[0]
            
            boughtPrice = value[1]
            gap = boughtPrice - todayPrice
            
            gapPercent = gap/boughtPrice*100
            
            
            # 조건에 맞으면 판매
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
            print(self.gapDict[self.strTarget])
        for l in delStock:
            del self.haveStock[l]
        
        return sellingNum
        
    # 조건에 맞는 주식 구매
    def buyingStock(self,targetlist_df,buyStockNum):
        idx =0
        buyflag=0
        length = targetlist_df.shape[0]
        while buyflag < buyStockNum:
            if length<=idx:
                break
            if targetlist_df.loc[idx]['ticker'] in self.haveStock:
                idx+=1
                continue
            new_data = {
                'ticker' : targetlist_df.loc[idx]['ticker'],
                'buy_date' : self.targetDate,
                'buy_price' : targetlist_df.loc[idx]['close']
            }
            self.haveStock[new_data["ticker"]] = [self.targetDate, new_data['buy_price']]
            buyflag +=1
            
    # 매수 조건 알고리즘으로 
    def classification(self,new_data):
        for con in self.sorts:
            if new_data[f"{con}"] is None:
                return False
            if self.condition[con][0] > new_data[f"{con}"] or self.condition[con][1] < new_data[f"{con}"]:
                return False
        return True
    
    
    def dailyTesting(self,targetList):
        
        daily_df = pd.DataFrame(columns=['ticker','close','PER','PBR','PSR','ROE','ROA'])
        dailyAll_df = pd.DataFrame(columns=['ticker','close'])
        #그날에 맞는 주식 객체 정보 리스트(코스피, 테마 조건 부합하는 것)
        for ticker in targetList:
            strClass = 'StockX'+ticker.code
            instance = eval(strClass)
            try:
                dateInfo = instance.objects.using("stockDB").get(date=self.targetDate)
            except:
                return False
            dateInfo_serializer = BackTestSerializer(dateInfo)

            new_data = {
                'ticker' : ticker.code,
                'close' : dateInfo_serializer.data["close"],    
            }
            
            dailyAll_df = dailyAll_df.append(new_data,ignore_index=True)
            
            for c in self.sorts:
                lowerC = c.lower()
                new_data[f'{c}']= dateInfo_serializer.data[f"{lowerC}"]
            
            if self.classification(new_data):
                daily_df = daily_df.append(new_data,ignore_index=True)
            else:
                continue
        
        buyStockNum = 10        
        self.gapDict[self.strTarget] =0
        #매도 조건에 맞는 주식 판매(손절, 익절)
        if self.targetDate !=self.start:
            buyStockNum = self.sellingStock(dailyAll_df)
        
        if buyStockNum == 0:
            return
        #우선 순위에 의해 ordering
        sort_daily_df = daily_df.sort_values(by=self.sorts,ascending=True)
        sort_daily_df.reset_index(drop=True,inplace=True)
        
        #조건에 맞는 주식 구매
        self.buyingStock(sort_daily_df,buyStockNum)
        return True
        
    ## 백테스트 실행 함수
    def backTesting(self):
        targetList = StockList.objects.using("stockDB").filter(
            market__in = self.marketList,
            sectorcode__in = self.sectorList
        )

        while self.targetDate != self.end:
            self.strTarget = self.targetDate.strftime("%Y-%m-%d")
            
            if self.is_weekend(self.targetDate) == True:
                self.targetDate += timedelta(days=1)
                continue
            
            if self.dailyTesting(targetList) == False:
                self.targetDate += timedelta(days=1)
                continue
            self.gapDict['total']+=self.gapDict[self.strTarget]
            
            self.targetDate += timedelta(days=1)
        
        return self.gapDict['total']
        # self.backTestLog_df.to_csv("backtestLog.csv")