from django.db import models

# Create your models here.
class stockList(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    category = models.IntegerField()

class stockInfo(models.Model):
    code = models.ForeignKey(stockList, related_name="")
    date = models.DateTimeField()
    closingPrice = models.FloatField()  #종가
    openPrice = models.FloatField()     #시가
    highPrice =models.FloatField()      #고가
    lowPrice = models.FloatField()      #저가
    marketCap = models.FloatField()     #시가총액
    tradingVolume = models.FloatField() #거래량
    

class marketInfo(models.Models):
    name = models.CharField(max_length=20)
    score = models.FloatField()
    tradingVolume = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    