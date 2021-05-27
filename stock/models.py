from django.db import models

class SectorList(models.Model):
    sectorcode= models.CharField(max_length=10,primary_key=True)
    sector = models.CharField(max_length=100)

class ThemaList(models.Model):
    themacode= models.CharField(max_length=10,primary_key=True)
    thema = models.CharField(max_length=100)

class MarketList(models.Model):
    id = models.AutoField(primary_key=True)
    market = models.CharField(max_length=20,unique=True)

class StockList(models.Model):
    code= models.CharField(max_length=10,primary_key=True)
    company = models.CharField(max_length=50)
    market = models.ForeignKey(MarketList,to_field='id', on_delete=models.CASCADE)
    sectorcode = models.ForeignKey(SectorList, to_field='sectorcode', on_delete= models.CASCADE)
    themacode = models.ForeignKey(ThemaList, to_field='themacode', on_delete=models.CASCADE)
    last_update = models.DateField()


class Kospi(models.Model):
    date = models.DateTimeField(primary_key=True)
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    tradingVolume = models.FloatField()
    tradingPrice = models.FloatField()

class Kosdaq(models.Model):
    date = models.DateTimeField(primary_key=True)
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    tradingVolume = models.FloatField()
    tradingPrice = models.FloatField()

class Kospi200(models.Model):
    date = models.DateTimeField(primary_key=True)
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    tradingVolume = models.FloatField()
    tradingPrice = models.FloatField()


class dailyMarketIndex(models.Model):
    id = models.AutoField(primary_key=True)
    market = models.ForeignKey(MarketList,to_field='id', on_delete=models.CASCADE)
    date = models.DateTimeField()
    index = models.FloatField() #현재가
    changeNum = models.CharField(max_length=30)
    changePer = models.CharField(max_length=30)


class StockX000020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000020'


class StockX000040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000040'


class StockX000050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000050'


class StockX000060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000060'


class StockX000070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000070'


class StockX000080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000080'


class StockX000100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000100'


class StockX000120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000120'


class StockX000140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000140'


class StockX000150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000150'


class StockX000180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000180'


class StockX000210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000210'


class StockX000220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000220'


class StockX000230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000230'


class StockX000240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000240'


class StockX000250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000250'


class StockX000270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000270'


class StockX000300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000300'


class StockX000320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000320'


class StockX000370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000370'


class StockX000390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000390'


class StockX000400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000400'


class StockX000430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000430'


class StockX000440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000440'


class StockX000480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000480'


class StockX000490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000490'


class StockX000500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000500'


class StockX000520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000520'


class StockX000540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000540'


class StockX000590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000590'


class StockX000640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000640'


class StockX000650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000650'


class StockX000660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000660'


class StockX000670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000670'


class StockX000680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000680'


class StockX000700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000700'


class StockX000720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000720'


class StockX000760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000760'


class StockX000810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000810'


class StockX000850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000850'


class StockX000860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000860'


class StockX000880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000880'


class StockX000890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000890'


class StockX000910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000910'


class StockX000950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000950'


class StockX000970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000970'


class StockX000990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x000990'


class StockX001000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001000'


class StockX001020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001020'


class StockX001040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001040'


class StockX001060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001060'


class StockX001070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001070'


class StockX001080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001080'


class StockX001120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001120'


class StockX001130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001130'


class StockX001140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001140'


class StockX001200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001200'


class StockX001210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001210'


class StockX001230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001230'


class StockX001250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001250'


class StockX001260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001260'


class StockX001270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001270'


class StockX001290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001290'


class StockX001340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001340'


class StockX001360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001360'


class StockX001380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001380'


class StockX001390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001390'


class StockX001420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001420'


class StockX001430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001430'


class StockX001440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001440'


class StockX001450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001450'


class StockX001460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001460'


class StockX001470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001470'


class StockX001500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001500'


class StockX001510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001510'


class StockX001520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001520'


class StockX001530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001530'


class StockX001540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001540'


class StockX001550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001550'


class StockX001560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001560'


class StockX001570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001570'


class StockX001620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001620'


class StockX001630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001630'


class StockX001680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001680'


class StockX001720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001720'


class StockX001740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001740'


class StockX001750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001750'


class StockX001770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001770'


class StockX001780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001780'


class StockX001790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001790'


class StockX001800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001800'


class StockX001810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001810'


class StockX001820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001820'


class StockX001840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001840'


class StockX001880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001880'


class StockX001940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x001940'


class StockX002020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002020'


class StockX002030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002030'


class StockX002070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002070'


class StockX002100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002100'


class StockX002140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002140'


class StockX002150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002150'


class StockX002170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002170'


class StockX002200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002200'


class StockX002210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002210'


class StockX002220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002220'


class StockX002230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002230'


class StockX002240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002240'


class StockX002270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002270'


class StockX002290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002290'


class StockX002310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002310'


class StockX002320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002320'


class StockX002350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002350'


class StockX002360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002360'


class StockX002380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002380'


class StockX002390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002390'


class StockX002410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002410'


class StockX002420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002420'


class StockX002450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002450'


class StockX002460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002460'


class StockX002600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002600'


class StockX002620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002620'


class StockX002630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002630'


class StockX002680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002680'


class StockX002690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002690'


class StockX002700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002700'


class StockX002710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002710'


class StockX002720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002720'


class StockX002760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002760'


class StockX002780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002780'


class StockX002790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002790'


class StockX002800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002800'


class StockX002810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002810'


class StockX002820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002820'


class StockX002840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002840'


class StockX002870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002870'


class StockX002880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002880'


class StockX002900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002900'


class StockX002920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002920'


class StockX002960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002960'


class StockX002990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x002990'


class StockX003000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003000'


class StockX003010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003010'


class StockX003030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003030'


class StockX003060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003060'


class StockX003070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003070'


class StockX003080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003080'


class StockX003090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003090'


class StockX003100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003100'


class StockX003120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003120'


class StockX003160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003160'


class StockX003200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003200'


class StockX003220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003220'


class StockX003230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003230'


class StockX003240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003240'


class StockX003280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003280'


class StockX003300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003300'


class StockX003310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003310'


class StockX003350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003350'


class StockX003380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003380'


class StockX003410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003410'


class StockX003460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003460'


class StockX003470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003470'


class StockX003480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003480'


class StockX003490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003490'


class StockX003520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003520'


class StockX003530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003530'


class StockX003540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003540'


class StockX003550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003550'


class StockX003560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003560'


class StockX003570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003570'


class StockX003580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003580'


class StockX003610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003610'


class StockX003620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003620'


class StockX003650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003650'


class StockX003670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003670'


class StockX003680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003680'


class StockX003690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003690'


class StockX003720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003720'


class StockX003780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003780'


class StockX003800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003800'


class StockX003830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003830'


class StockX003850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003850'


class StockX003920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003920'


class StockX003960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x003960'


class StockX004000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004000'


class StockX004020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004020'


class StockX004060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004060'


class StockX004080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004080'


class StockX004090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004090'


class StockX004100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004100'


class StockX004140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004140'


class StockX004150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004150'


class StockX004170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004170'


class StockX004250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004250'


class StockX004270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004270'


class StockX004310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004310'


class StockX004360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004360'


class StockX004370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004370'


class StockX004380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004380'


class StockX004410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004410'


class StockX004430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004430'


class StockX004440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004440'


class StockX004450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004450'


class StockX004490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004490'


class StockX004540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004540'


class StockX004560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004560'


class StockX004590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004590'


class StockX004650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004650'


class StockX004690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004690'


class StockX004700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004700'


class StockX004710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004710'


class StockX004720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004720'


class StockX004770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004770'


class StockX004780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004780'


class StockX004800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004800'


class StockX004830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004830'


class StockX004840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004840'


class StockX004870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004870'


class StockX004890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004890'


class StockX004910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004910'


class StockX004920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004920'


class StockX004960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004960'


class StockX004970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004970'


class StockX004980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004980'


class StockX004990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x004990'


class StockX005010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005010'


class StockX005030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005030'


class StockX005070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005070'


class StockX005090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005090'


class StockX005110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005110'


class StockX005160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005160'


class StockX005180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005180'


class StockX005250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005250'


class StockX005290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005290'


class StockX005300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005300'


class StockX005320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005320'


class StockX005360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005360'


class StockX005380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005380'


class StockX005390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005390'


class StockX005420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005420'


class StockX005430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005430'


class StockX005440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005440'


class StockX005490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005490'


class StockX005500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005500'


class StockX005610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005610'


class StockX005670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005670'


class StockX005680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005680'


class StockX005690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005690'


class StockX005710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005710'


class StockX005720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005720'


class StockX005740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005740'


class StockX005750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005750'


class StockX005800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005800'


class StockX005810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005810'


class StockX005820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005820'


class StockX005830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005830'


class StockX005850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005850'


class StockX005860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005860'


class StockX005870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005870'


class StockX005880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005880'


class StockX005930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005930'


class StockX005940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005940'


class StockX005950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005950'


class StockX005960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005960'


class StockX005990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x005990'


class StockX006040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006040'


class StockX006050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006050'


class StockX006060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006060'


class StockX006090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006090'


class StockX006110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006110'


class StockX006120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006120'


class StockX006140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006140'


class StockX006200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006200'


class StockX006220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006220'


class StockX006260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006260'


class StockX006280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006280'


class StockX006340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006340'


class StockX006360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006360'


class StockX006370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006370'


class StockX006380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006380'


class StockX006390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006390'


class StockX006400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006400'


class StockX006490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006490'


class StockX006570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006570'


class StockX006580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006580'


class StockX006620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006620'


class StockX006650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006650'


class StockX006660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006660'


class StockX006730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006730'


class StockX006740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006740'


class StockX006800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006800'


class StockX006840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006840'


class StockX006880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006880'


class StockX006890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006890'


class StockX006910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006910'


class StockX006920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006920'


class StockX006980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x006980'


class StockX007070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007070'


class StockX007110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007110'


class StockX007120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007120'


class StockX007160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007160'


class StockX007210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007210'


class StockX007280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007280'


class StockX007310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007310'


class StockX007330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007330'


class StockX007340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007340'


class StockX007370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007370'


class StockX007390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007390'


class StockX007460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007460'


class StockX007530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007530'


class StockX007540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007540'


class StockX007570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007570'


class StockX007590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007590'


class StockX007610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007610'


class StockX007630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007630'


class StockX007660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007660'


class StockX007680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007680'


class StockX007690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007690'


class StockX007700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007700'


class StockX007720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007720'


class StockX007770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007770'


class StockX007810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007810'


class StockX007820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007820'


class StockX007860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007860'


class StockX007980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x007980'


class StockX008040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008040'


class StockX008060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008060'


class StockX008110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008110'


class StockX008250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008250'


class StockX008260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008260'


class StockX008290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008290'


class StockX008350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008350'


class StockX008370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008370'


class StockX008420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008420'


class StockX008470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008470'


class StockX008490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008490'


class StockX008500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008500'


class StockX008560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008560'


class StockX008600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008600'


class StockX008700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008700'


class StockX008730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008730'


class StockX008770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008770'


class StockX008800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008800'


class StockX008830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008830'


class StockX008870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008870'


class StockX008930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008930'


class StockX008970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x008970'


class StockX009070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009070'


class StockX009140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009140'


class StockX009150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009150'


class StockX009160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009160'


class StockX009180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009180'


class StockX009190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009190'


class StockX009200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009200'


class StockX009240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009240'


class StockX009270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009270'


class StockX009290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009290'


class StockX009300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009300'


class StockX009310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009310'


class StockX009320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009320'


class StockX009410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009410'


class StockX009420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009420'


class StockX009440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009440'


class StockX009450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009450'


class StockX009460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009460'


class StockX009470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009470'


class StockX009520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009520'


class StockX009540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009540'


class StockX009580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009580'


class StockX009620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009620'


class StockX009680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009680'


class StockX009730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009730'


class StockX009770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009770'


class StockX009780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009780'


class StockX009810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009810'


class StockX009830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009830'


class StockX009900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009900'


class StockX009970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x009970'


class StockX010040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010040'


class StockX010050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010050'


class StockX010060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010060'


class StockX010100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010100'


class StockX010120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010120'


class StockX010130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010130'


class StockX010140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010140'


class StockX010170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010170'


class StockX010240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010240'


class StockX010280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010280'


class StockX010400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010400'


class StockX010420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010420'


class StockX010470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010470'


class StockX010580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010580'


class StockX010600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010600'


class StockX010620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010620'


class StockX010640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010640'


class StockX010660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010660'


class StockX010690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010690'


class StockX010770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010770'


class StockX010780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010780'


class StockX010820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010820'


class StockX010950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010950'


class StockX010960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x010960'


class StockX011000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011000'


class StockX011040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011040'


class StockX011070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011070'


class StockX011080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011080'


class StockX011090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011090'


class StockX011150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011150'


class StockX011170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011170'


class StockX011200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011200'


class StockX011210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011210'


class StockX011230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011230'


class StockX011280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011280'


class StockX011300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011300'


class StockX011320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011320'


class StockX011330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011330'


class StockX011370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011370'


class StockX011390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011390'


class StockX011420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011420'


class StockX011500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011500'


class StockX011560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011560'


class StockX011690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011690'


class StockX011700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011700'


class StockX011760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011760'


class StockX011780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011780'


class StockX011790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011790'


class StockX011810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011810'


class StockX011930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x011930'


class StockX012030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012030'


class StockX012160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012160'


class StockX012170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012170'


class StockX012200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012200'


class StockX012280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012280'


class StockX012320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012320'


class StockX012330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012330'


class StockX012340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012340'


class StockX012450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012450'


class StockX012510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012510'


class StockX012600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012600'


class StockX012610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012610'


class StockX012620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012620'


class StockX012630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012630'


class StockX012690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012690'


class StockX012700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012700'


class StockX012750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012750'


class StockX012790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012790'


class StockX012800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012800'


class StockX012860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x012860'


class StockX013000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013000'


class StockX013030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013030'


class StockX013120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013120'


class StockX013310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013310'


class StockX013360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013360'


class StockX013520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013520'


class StockX013570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013570'


class StockX013580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013580'


class StockX013700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013700'


class StockX013720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013720'


class StockX013810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013810'


class StockX013870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013870'


class StockX013890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013890'


class StockX013990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x013990'


class StockX014100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014100'


class StockX014130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014130'


class StockX014160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014160'


class StockX014190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014190'


class StockX014200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014200'


class StockX014280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014280'


class StockX014440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014440'


class StockX014470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014470'


class StockX014530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014530'


class StockX014570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014570'


class StockX014580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014580'


class StockX014620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014620'


class StockX014680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014680'


class StockX014710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014710'


class StockX014790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014790'


class StockX014820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014820'


class StockX014830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014830'


class StockX014910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014910'


class StockX014940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014940'


class StockX014970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014970'


class StockX014990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x014990'


class StockX015020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015020'


class StockX015230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015230'


class StockX015260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015260'


class StockX015350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015350'


class StockX015360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015360'


class StockX015540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015540'


class StockX015590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015590'


class StockX015710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015710'


class StockX015750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015750'


class StockX015760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015760'


class StockX015860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015860'


class StockX015890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x015890'


class StockX016090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016090'


class StockX016100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016100'


class StockX016250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016250'


class StockX016360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016360'


class StockX016380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016380'


class StockX016450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016450'


class StockX016580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016580'


class StockX016590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016590'


class StockX016600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016600'


class StockX016610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016610'


class StockX016670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016670'


class StockX016710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016710'


class StockX016740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016740'


class StockX016790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016790'


class StockX016800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016800'


class StockX016880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016880'


class StockX016920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x016920'


class StockX017000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017000'


class StockX017040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017040'


class StockX017180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017180'


class StockX017250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017250'


class StockX017370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017370'


class StockX017390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017390'


class StockX017480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017480'


class StockX017510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017510'


class StockX017550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017550'


class StockX017650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017650'


class StockX017670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017670'


class StockX017800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017800'


class StockX017810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017810'


class StockX017890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017890'


class StockX017900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017900'


class StockX017940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017940'


class StockX017960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x017960'


class StockX018000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018000'


class StockX018120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018120'


class StockX018250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018250'


class StockX018260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018260'


class StockX018290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018290'


class StockX018310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018310'


class StockX018470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018470'


class StockX018500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018500'


class StockX018620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018620'


class StockX018670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018670'


class StockX018680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018680'


class StockX018700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018700'


class StockX018880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x018880'


class StockX019010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019010'


class StockX019170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019170'


class StockX019180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019180'


class StockX019210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019210'


class StockX019440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019440'


class StockX019490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019490'


class StockX019540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019540'


class StockX019550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019550'


class StockX019570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019570'


class StockX019590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019590'


class StockX019660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019660'


class StockX019680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019680'


class StockX019770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019770'


class StockX019990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x019990'


class StockX020000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020000'


class StockX020120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020120'


class StockX020150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020150'


class StockX020180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020180'


class StockX020400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020400'


class StockX020560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020560'


class StockX020710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020710'


class StockX020760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x020760'


class StockX021040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021040'


class StockX021050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021050'


class StockX021080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021080'


class StockX021240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021240'


class StockX021320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021320'


class StockX021650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021650'


class StockX021820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021820'


class StockX021880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x021880'


class StockX022100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x022100'


class StockX022220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x022220'


class StockX023000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023000'


class StockX023150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023150'


class StockX023160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023160'


class StockX023350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023350'


class StockX023410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023410'


class StockX023440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023440'


class StockX023450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023450'


class StockX023460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023460'


class StockX023530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023530'


class StockX023590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023590'


class StockX023600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023600'


class StockX023760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023760'


class StockX023770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023770'


class StockX023790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023790'


class StockX023800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023800'


class StockX023810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023810'


class StockX023900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023900'


class StockX023910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023910'


class StockX023960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x023960'


class StockX024060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024060'


class StockX024070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024070'


class StockX024090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024090'


class StockX024110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024110'


class StockX024120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024120'


class StockX024720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024720'


class StockX024740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024740'


class StockX024800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024800'


class StockX024810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024810'


class StockX024830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024830'


class StockX024840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024840'


class StockX024850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024850'


class StockX024880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024880'


class StockX024890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024890'


class StockX024900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024900'


class StockX024910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024910'


class StockX024940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024940'


class StockX024950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x024950'


class StockX025000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025000'


class StockX025320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025320'


class StockX025440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025440'


class StockX025530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025530'


class StockX025540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025540'


class StockX025550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025550'


class StockX025560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025560'


class StockX025620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025620'


class StockX025750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025750'


class StockX025770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025770'


class StockX025820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025820'


class StockX025860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025860'


class StockX025870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025870'


class StockX025880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025880'


class StockX025890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025890'


class StockX025900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025900'


class StockX025950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025950'


class StockX025980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x025980'


class StockX026040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x026040'


class StockX026150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x026150'


class StockX026890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x026890'


class StockX026910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x026910'


class StockX026940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x026940'


class StockX026960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x026960'


class StockX027040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027040'


class StockX027050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027050'


class StockX027360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027360'


class StockX027410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027410'


class StockX027580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027580'


class StockX027710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027710'


class StockX027740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027740'


class StockX027830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027830'


class StockX027970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x027970'


class StockX028050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x028050'


class StockX028080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x028080'


class StockX028100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x028100'


class StockX028150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x028150'


class StockX028260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x028260'


class StockX028300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x028300'


class StockX028670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x028670'


class StockX029460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x029460'


class StockX029480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x029480'


class StockX029530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x029530'


class StockX029780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x029780'


class StockX029960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x029960'


class StockX030000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030000'


class StockX030190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030190'


class StockX030200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030200'


class StockX030210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030210'


class StockX030350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030350'


class StockX030520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030520'


class StockX030530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030530'


class StockX030610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030610'


class StockX030720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030720'


class StockX030790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030790'


class StockX030960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x030960'


class StockX031310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031310'


class StockX031330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031330'


class StockX031390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031390'


class StockX031430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031430'


class StockX031440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031440'


class StockX031510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031510'


class StockX031820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031820'


class StockX031860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031860'


class StockX031980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x031980'


class StockX032080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032080'


class StockX032190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032190'


class StockX032280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032280'


class StockX032300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032300'


class StockX032350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032350'


class StockX032500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032500'


class StockX032540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032540'


class StockX032560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032560'


class StockX032580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032580'


class StockX032620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032620'


class StockX032640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032640'


class StockX032680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032680'


class StockX032750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032750'


class StockX032790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032790'


class StockX032800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032800'


class StockX032820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032820'


class StockX032830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032830'


class StockX032850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032850'


class StockX032860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032860'


class StockX032940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032940'


class StockX032960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032960'


class StockX032980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x032980'


class StockX033050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033050'


class StockX033100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033100'


class StockX033110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033110'


class StockX033130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033130'


class StockX033160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033160'


class StockX033170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033170'


class StockX033180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033180'


class StockX033200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033200'


class StockX033230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033230'


class StockX033240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033240'


class StockX033250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033250'


class StockX033270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033270'


class StockX033290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033290'


class StockX033310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033310'


class StockX033320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033320'


class StockX033340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033340'


class StockX033430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033430'


class StockX033500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033500'


class StockX033530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033530'


class StockX033540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033540'


class StockX033560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033560'


class StockX033600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033600'


class StockX033640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033640'


class StockX033660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033660'


class StockX033780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033780'


class StockX033790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033790'


class StockX033830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033830'


class StockX033920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x033920'


class StockX034020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034020'


class StockX034120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034120'


class StockX034220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034220'


class StockX034230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034230'


class StockX034300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034300'


class StockX034310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034310'


class StockX034590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034590'


class StockX034730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034730'


class StockX034810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034810'


class StockX034830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034830'


class StockX034940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034940'


class StockX034950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x034950'


class StockX035000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035000'


class StockX035080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035080'


class StockX035150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035150'


class StockX035200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035200'


class StockX035250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035250'


class StockX035290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035290'


class StockX035420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035420'


class StockX035460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035460'


class StockX035510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035510'


class StockX035600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035600'


class StockX035610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035610'


class StockX035620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035620'


class StockX035720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035720'


class StockX035760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035760'


class StockX035810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035810'


class StockX035890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035890'


class StockX035900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x035900'


class StockX036000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036000'


class StockX036010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036010'


class StockX036030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036030'


class StockX036090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036090'


class StockX036120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036120'


class StockX036170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036170'


class StockX036180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036180'


class StockX036190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036190'


class StockX036200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036200'


class StockX036420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036420'


class StockX036460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036460'


class StockX036480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036480'


class StockX036490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036490'


class StockX036530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036530'


class StockX036540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036540'


class StockX036560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036560'


class StockX036570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036570'


class StockX036580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036580'


class StockX036620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036620'


class StockX036630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036630'


class StockX036640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036640'


class StockX036670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036670'


class StockX036690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036690'


class StockX036710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036710'


class StockX036800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036800'


class StockX036810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036810'


class StockX036830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036830'


class StockX036890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036890'


class StockX036930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x036930'


class StockX037030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037030'


class StockX037070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037070'


class StockX037230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037230'


class StockX037270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037270'


class StockX037330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037330'


class StockX037350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037350'


class StockX037370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037370'


class StockX037400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037400'


class StockX037440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037440'


class StockX037460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037460'


class StockX037560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037560'


class StockX037710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037710'


class StockX037760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037760'


class StockX037950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x037950'


class StockX038010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038010'


class StockX038060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038060'


class StockX038070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038070'


class StockX038110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038110'


class StockX038160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038160'


class StockX038290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038290'


class StockX038340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038340'


class StockX038390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038390'


class StockX038460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038460'


class StockX038500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038500'


class StockX038530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038530'


class StockX038540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038540'


class StockX038620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038620'


class StockX038680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038680'


class StockX038870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038870'


class StockX038880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038880'


class StockX038950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x038950'


class StockX039010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039010'


class StockX039020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039020'


class StockX039030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039030'


class StockX039130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039130'


class StockX039200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039200'


class StockX039230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039230'


class StockX039240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039240'


class StockX039290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039290'


class StockX039310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039310'


class StockX039340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039340'


class StockX039420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039420'


class StockX039440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039440'


class StockX039490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039490'


class StockX039560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039560'


class StockX039570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039570'


class StockX039610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039610'


class StockX039670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039670'


class StockX039740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039740'


class StockX039830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039830'


class StockX039840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039840'


class StockX039860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039860'


class StockX039980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x039980'


class StockX040160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x040160'


class StockX040300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x040300'


class StockX040350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x040350'


class StockX040420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x040420'


class StockX040610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x040610'


class StockX040910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x040910'


class StockX041020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041020'


class StockX041140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041140'


class StockX041190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041190'


class StockX041440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041440'


class StockX041460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041460'


class StockX041510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041510'


class StockX041520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041520'


class StockX041590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041590'


class StockX041650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041650'


class StockX041830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041830'


class StockX041910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041910'


class StockX041920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041920'


class StockX041930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041930'


class StockX041960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x041960'


class StockX042000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042000'


class StockX042040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042040'


class StockX042110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042110'


class StockX042370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042370'


class StockX042420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042420'


class StockX042500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042500'


class StockX042510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042510'


class StockX042520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042520'


class StockX042600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042600'


class StockX042660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042660'


class StockX042670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042670'


class StockX042700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042700'


class StockX042940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x042940'


class StockX043090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043090'


class StockX043100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043100'


class StockX043150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043150'


class StockX043200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043200'


class StockX043220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043220'


class StockX043260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043260'


class StockX043290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043290'


class StockX043340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043340'


class StockX043360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043360'


class StockX043370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043370'


class StockX043590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043590'


class StockX043610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043610'


class StockX043650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043650'


class StockX043710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043710'


class StockX043910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x043910'


class StockX044060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044060'


class StockX044180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044180'


class StockX044340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044340'


class StockX044380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044380'


class StockX044450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044450'


class StockX044480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044480'


class StockX044490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044490'


class StockX044780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044780'


class StockX044820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044820'


class StockX044960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x044960'


class StockX045060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045060'


class StockX045100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045100'


class StockX045300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045300'


class StockX045340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045340'


class StockX045390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045390'


class StockX045510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045510'


class StockX045520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045520'


class StockX045660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045660'


class StockX045890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045890'


class StockX045970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x045970'


class StockX046070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046070'


class StockX046110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046110'


class StockX046120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046120'


class StockX046140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046140'


class StockX046210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046210'


class StockX046310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046310'


class StockX046390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046390'


class StockX046440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046440'


class StockX046890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046890'


class StockX046940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046940'


class StockX046970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x046970'


class StockX047040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047040'


class StockX047050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047050'


class StockX047080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047080'


class StockX047310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047310'


class StockX047400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047400'


class StockX047560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047560'


class StockX047770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047770'


class StockX047810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047810'


class StockX047820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047820'


class StockX047920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x047920'


class StockX048260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048260'


class StockX048410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048410'


class StockX048430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048430'


class StockX048470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048470'


class StockX048530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048530'


class StockX048550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048550'


class StockX048770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048770'


class StockX048830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048830'


class StockX048870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048870'


class StockX048910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x048910'


class StockX049070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049070'


class StockX049080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049080'


class StockX049120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049120'


class StockX049180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049180'


class StockX049430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049430'


class StockX049470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049470'


class StockX049480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049480'


class StockX049520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049520'


class StockX049550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049550'


class StockX049630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049630'


class StockX049720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049720'


class StockX049770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049770'


class StockX049800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049800'


class StockX049830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049830'


class StockX049950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049950'


class StockX049960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x049960'


class StockX050090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050090'


class StockX050110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050110'


class StockX050120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050120'


class StockX050320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050320'


class StockX050540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050540'


class StockX050760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050760'


class StockX050860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050860'


class StockX050890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050890'


class StockX050960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x050960'


class StockX051160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051160'


class StockX051360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051360'


class StockX051370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051370'


class StockX051380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051380'


class StockX051390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051390'


class StockX051490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051490'


class StockX051500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051500'


class StockX051600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051600'


class StockX051630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051630'


class StockX051780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051780'


class StockX051900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051900'


class StockX051910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051910'


class StockX051980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x051980'


class StockX052020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052020'


class StockX052190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052190'


class StockX052220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052220'


class StockX052260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052260'


class StockX052300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052300'


class StockX052330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052330'


class StockX052400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052400'


class StockX052420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052420'


class StockX052460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052460'


class StockX052600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052600'


class StockX052670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052670'


class StockX052690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052690'


class StockX052710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052710'


class StockX052770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052770'


class StockX052790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052790'


class StockX052860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052860'


class StockX052900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x052900'


class StockX053030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053030'


class StockX053050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053050'


class StockX053060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053060'


class StockX053080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053080'


class StockX053110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053110'


class StockX053160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053160'


class StockX053210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053210'


class StockX053260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053260'


class StockX053270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053270'


class StockX053280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053280'


class StockX053290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053290'


class StockX053300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053300'


class StockX053350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053350'


class StockX053450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053450'


class StockX053580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053580'


class StockX053590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053590'


class StockX053610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053610'


class StockX053620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053620'


class StockX053660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053660'


class StockX053690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053690'


class StockX053700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053700'


class StockX053800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053800'


class StockX053950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053950'


class StockX053980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x053980'


class StockX054040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054040'


class StockX054050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054050'


class StockX054090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054090'


class StockX054180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054180'


class StockX054210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054210'


class StockX054220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054220'


class StockX054300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054300'


class StockX054410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054410'


class StockX054450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054450'


class StockX054540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054540'


class StockX054620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054620'


class StockX054630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054630'


class StockX054670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054670'


class StockX054780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054780'


class StockX054800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054800'


class StockX054920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054920'


class StockX054930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054930'


class StockX054940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054940'


class StockX054950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x054950'


class StockX055490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x055490'


class StockX055550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x055550'


class StockX056000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x056000'


class StockX056080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x056080'


class StockX056090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x056090'


class StockX056190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x056190'


class StockX056360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x056360'


class StockX056700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x056700'


class StockX056730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x056730'


class StockX057030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x057030'


class StockX057050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x057050'


class StockX057540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x057540'


class StockX057680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x057680'


class StockX057880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x057880'


class StockX058110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058110'


class StockX058220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058220'


class StockX058400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058400'


class StockX058420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058420'


class StockX058430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058430'


class StockX058450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058450'


class StockX058470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058470'


class StockX058530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058530'


class StockX058610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058610'


class StockX058630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058630'


class StockX058650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058650'


class StockX058730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058730'


class StockX058820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058820'


class StockX058850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058850'


class StockX058860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x058860'


class StockX059090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x059090'


class StockX059100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x059100'


class StockX059120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x059120'


class StockX059210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x059210'


class StockX059270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x059270'


class StockX060150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060150'


class StockX060230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060230'


class StockX060240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060240'


class StockX060250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060250'


class StockX060260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060260'


class StockX060280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060280'


class StockX060300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060300'


class StockX060310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060310'


class StockX060370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060370'


class StockX060380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060380'


class StockX060480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060480'


class StockX060540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060540'


class StockX060560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060560'


class StockX060570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060570'


class StockX060590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060590'


class StockX060720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060720'


class StockX060850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060850'


class StockX060900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060900'


class StockX060980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x060980'


class StockX061040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x061040'


class StockX061250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x061250'


class StockX061970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x061970'


class StockX062860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x062860'


class StockX062970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x062970'


class StockX063080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x063080'


class StockX063160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x063160'


class StockX063170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x063170'


class StockX063440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x063440'


class StockX063570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x063570'


class StockX063760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x063760'


class StockX064090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064090'


class StockX064240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064240'


class StockX064260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064260'


class StockX064290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064290'


class StockX064350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064350'


class StockX064480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064480'


class StockX064510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064510'


class StockX064520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064520'


class StockX064550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064550'


class StockX064760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064760'


class StockX064800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064800'


class StockX064820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064820'


class StockX064850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064850'


class StockX064960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x064960'


class StockX065060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065060'


class StockX065130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065130'


class StockX065150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065150'


class StockX065170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065170'


class StockX065350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065350'


class StockX065370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065370'


class StockX065420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065420'


class StockX065440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065440'


class StockX065450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065450'


class StockX065500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065500'


class StockX065510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065510'


class StockX065530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065530'


class StockX065560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065560'


class StockX065570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065570'


class StockX065620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065620'


class StockX065650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065650'


class StockX065660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065660'


class StockX065680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065680'


class StockX065690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065690'


class StockX065710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065710'


class StockX065770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065770'


class StockX065950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x065950'


class StockX066110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066110'


class StockX066130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066130'


class StockX066310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066310'


class StockX066360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066360'


class StockX066410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066410'


class StockX066430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066430'


class StockX066570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066570'


class StockX066590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066590'


class StockX066620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066620'


class StockX066670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066670'


class StockX066700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066700'


class StockX066790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066790'


class StockX066900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066900'


class StockX066910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066910'


class StockX066970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066970'


class StockX066980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x066980'


class StockX067000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067000'


class StockX067010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067010'


class StockX067080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067080'


class StockX067160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067160'


class StockX067170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067170'


class StockX067280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067280'


class StockX067290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067290'


class StockX067310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067310'


class StockX067390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067390'


class StockX067570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067570'


class StockX067630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067630'


class StockX067730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067730'


class StockX067770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067770'


class StockX067830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067830'


class StockX067900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067900'


class StockX067920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067920'


class StockX067990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x067990'


class StockX068050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068050'


class StockX068240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068240'


class StockX068270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068270'


class StockX068290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068290'


class StockX068330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068330'


class StockX068400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068400'


class StockX068760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068760'


class StockX068790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068790'


class StockX068930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068930'


class StockX068940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x068940'


class StockX069080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069080'


class StockX069110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069110'


class StockX069140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069140'


class StockX069260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069260'


class StockX069330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069330'


class StockX069410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069410'


class StockX069460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069460'


class StockX069510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069510'


class StockX069540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069540'


class StockX069620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069620'


class StockX069640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069640'


class StockX069730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069730'


class StockX069920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069920'


class StockX069960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x069960'


class StockX070300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x070300'


class StockX070590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x070590'


class StockX070960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x070960'


class StockX071050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071050'


class StockX071090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071090'


class StockX071200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071200'


class StockX071280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071280'


class StockX071320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071320'


class StockX071460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071460'


class StockX071670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071670'


class StockX071840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071840'


class StockX071850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071850'


class StockX071950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071950'


class StockX071970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x071970'


class StockX072020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072020'


class StockX072130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072130'


class StockX072470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072470'


class StockX072520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072520'


class StockX072710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072710'


class StockX072770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072770'


class StockX072870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072870'


class StockX072950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072950'


class StockX072990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x072990'


class StockX073010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073010'


class StockX073070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073070'


class StockX073110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073110'


class StockX073190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073190'


class StockX073240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073240'


class StockX073490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073490'


class StockX073540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073540'


class StockX073560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073560'


class StockX073570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073570'


class StockX073640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x073640'


class StockX074430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x074430'


class StockX074600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x074600'


class StockX074610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x074610'


class StockX075130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x075130'


class StockX075180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x075180'


class StockX075580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x075580'


class StockX075970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x075970'


class StockX076080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x076080'


class StockX076610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x076610'


class StockX077360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x077360'


class StockX077500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x077500'


class StockX077970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x077970'


class StockX078000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078000'


class StockX078020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078020'


class StockX078070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078070'


class StockX078130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078130'


class StockX078140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078140'


class StockX078150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078150'


class StockX078160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078160'


class StockX078340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078340'


class StockX078350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078350'


class StockX078520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078520'


class StockX078590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078590'


class StockX078600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078600'


class StockX078650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078650'


class StockX078860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078860'


class StockX078890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078890'


class StockX078930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078930'


class StockX078940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x078940'


class StockX079000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079000'


class StockX079160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079160'


class StockX079170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079170'


class StockX079190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079190'


class StockX079370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079370'


class StockX079430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079430'


class StockX079550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079550'


class StockX079650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079650'


class StockX079810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079810'


class StockX079940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079940'


class StockX079950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079950'


class StockX079960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079960'


class StockX079970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079970'


class StockX079980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x079980'


class StockX080000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080000'


class StockX080010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080010'


class StockX080160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080160'


class StockX080220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080220'


class StockX080420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080420'


class StockX080440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080440'


class StockX080470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080470'


class StockX080520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080520'


class StockX080530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080530'


class StockX080580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080580'


class StockX080720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x080720'


class StockX081000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x081000'


class StockX081150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x081150'


class StockX081580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x081580'


class StockX081660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x081660'


class StockX082210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082210'


class StockX082270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082270'


class StockX082640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082640'


class StockX082660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082660'


class StockX082740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082740'


class StockX082800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082800'


class StockX082850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082850'


class StockX082920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x082920'


class StockX083310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083310'


class StockX083420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083420'


class StockX083450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083450'


class StockX083470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083470'


class StockX083500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083500'


class StockX083550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083550'


class StockX083640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083640'


class StockX083650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083650'


class StockX083660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083660'


class StockX083790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083790'


class StockX083930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x083930'


class StockX084010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084010'


class StockX084110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084110'


class StockX084180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084180'


class StockX084370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084370'


class StockX084650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084650'


class StockX084670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084670'


class StockX084680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084680'


class StockX084690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084690'


class StockX084730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084730'


class StockX084850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084850'


class StockX084870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084870'


class StockX084990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x084990'


class StockX085310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x085310'


class StockX085370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x085370'


class StockX085620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x085620'


class StockX085660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x085660'


class StockX085670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x085670'


class StockX085810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x085810'


class StockX085910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x085910'


class StockX086040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086040'


class StockX086060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086060'


class StockX086250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086250'


class StockX086280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086280'


class StockX086390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086390'


class StockX086450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086450'


class StockX086520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086520'


class StockX086670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086670'


class StockX086710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086710'


class StockX086790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086790'


class StockX086820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086820'


class StockX086890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086890'


class StockX086900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086900'


class StockX086960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086960'


class StockX086980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x086980'


class StockX087010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x087010'


class StockX087260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x087260'


class StockX087600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x087600'


class StockX087730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x087730'


class StockX088130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x088130'


class StockX088290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x088290'


class StockX088350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x088350'


class StockX088390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x088390'


class StockX088790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x088790'


class StockX088800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x088800'


class StockX088910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x088910'


class StockX089010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089010'


class StockX089030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089030'


class StockX089140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089140'


class StockX089150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089150'


class StockX089230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089230'


class StockX089470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089470'


class StockX089530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089530'


class StockX089590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089590'


class StockX089600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089600'


class StockX089790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089790'


class StockX089850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089850'


class StockX089890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089890'


class StockX089970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089970'


class StockX089980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x089980'


class StockX090080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090080'


class StockX090150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090150'


class StockX090350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090350'


class StockX090360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090360'


class StockX090370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090370'


class StockX090410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090410'


class StockX090430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090430'


class StockX090460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090460'


class StockX090470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090470'


class StockX090710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090710'


class StockX090740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090740'


class StockX090850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x090850'


class StockX091090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091090'


class StockX091120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091120'


class StockX091340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091340'


class StockX091440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091440'


class StockX091580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091580'


class StockX091590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091590'


class StockX091700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091700'


class StockX091810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091810'


class StockX091970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091970'


class StockX091990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x091990'


class StockX092040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092040'


class StockX092070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092070'


class StockX092130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092130'


class StockX092190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092190'


class StockX092200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092200'


class StockX092220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092220'


class StockX092230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092230'


class StockX092300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092300'


class StockX092440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092440'


class StockX092460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092460'


class StockX092600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092600'


class StockX092730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092730'


class StockX092780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092780'


class StockX092870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x092870'


class StockX093050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093050'


class StockX093190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093190'


class StockX093230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093230'


class StockX093240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093240'


class StockX093320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093320'


class StockX093370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093370'


class StockX093380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093380'


class StockX093520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093520'


class StockX093640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093640'


class StockX093920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x093920'


class StockX094170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094170'


class StockX094280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094280'


class StockX094360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094360'


class StockX094480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094480'


class StockX094820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094820'


class StockX094840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094840'


class StockX094850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094850'


class StockX094860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094860'


class StockX094940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094940'


class StockX094970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x094970'


class StockX095190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095190'


class StockX095270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095270'


class StockX095340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095340'


class StockX095500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095500'


class StockX095570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095570'


class StockX095610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095610'


class StockX095660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095660'


class StockX095700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095700'


class StockX095720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095720'


class StockX095910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x095910'


class StockX096040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096040'


class StockX096240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096240'


class StockX096350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096350'


class StockX096530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096530'


class StockX096610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096610'


class StockX096630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096630'


class StockX096640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096640'


class StockX096690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096690'


class StockX096760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096760'


class StockX096770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096770'


class StockX096870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x096870'


class StockX097230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x097230'


class StockX097520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x097520'


class StockX097780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x097780'


class StockX097800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x097800'


class StockX097870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x097870'


class StockX097950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x097950'


class StockX098120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x098120'


class StockX098460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x098460'


class StockX098660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x098660'


class StockX099190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x099190'


class StockX099220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x099220'


class StockX099320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x099320'


class StockX099410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x099410'


class StockX099440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x099440'


class StockX099520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x099520'


class StockX099750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x099750'


class StockX100030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100030'


class StockX100090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100090'


class StockX100120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100120'


class StockX100130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100130'


class StockX100220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100220'


class StockX100250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100250'


class StockX100590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100590'


class StockX100660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100660'


class StockX100700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100700'


class StockX100790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100790'


class StockX100840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x100840'


class StockX101000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101000'


class StockX101060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101060'


class StockX101140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101140'


class StockX101160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101160'


class StockX101170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101170'


class StockX101240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101240'


class StockX101330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101330'


class StockX101360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101360'


class StockX101390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101390'


class StockX101400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101400'


class StockX101490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101490'


class StockX101530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101530'


class StockX101670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101670'


class StockX101680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101680'


class StockX101730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101730'


class StockX101930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x101930'


class StockX102120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x102120'


class StockX102260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x102260'


class StockX102280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x102280'


class StockX102460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x102460'


class StockX102710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x102710'


class StockX102940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x102940'


class StockX103140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x103140'


class StockX103230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x103230'


class StockX103590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x103590'


class StockX103840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x103840'


class StockX104040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104040'


class StockX104200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104200'


class StockX104460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104460'


class StockX104480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104480'


class StockX104540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104540'


class StockX104620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104620'


class StockX104700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104700'


class StockX104830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x104830'


class StockX105330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x105330'


class StockX105550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x105550'


class StockX105560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x105560'


class StockX105630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x105630'


class StockX105740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x105740'


class StockX105840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x105840'


class StockX106080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x106080'


class StockX106190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x106190'


class StockX106240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x106240'


class StockX106520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x106520'


class StockX107590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x107590'


class StockX108230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x108230'


class StockX108320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x108320'


class StockX108380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x108380'


class StockX108490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x108490'


class StockX108670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x108670'


class StockX108860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x108860'


class StockX109070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x109070'


class StockX109080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x109080'


class StockX109610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x109610'


class StockX109740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x109740'


class StockX109820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x109820'


class StockX109860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x109860'


class StockX109960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x109960'


class StockX110020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x110020'


class StockX110790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x110790'


class StockX110990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x110990'


class StockX111110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x111110'


class StockX111710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x111710'


class StockX111770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x111770'


class StockX111820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x111820'


class StockX111870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x111870'


class StockX112040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x112040'


class StockX112610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x112610'


class StockX113810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x113810'


class StockX114090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x114090'


class StockX114120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x114120'


class StockX114190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x114190'


class StockX114450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x114450'


class StockX114570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x114570'


class StockX114630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x114630'


class StockX114810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x114810'


class StockX115160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115160'


class StockX115180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115180'


class StockX115310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115310'


class StockX115390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115390'


class StockX115440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115440'


class StockX115450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115450'


class StockX115480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115480'


class StockX115500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115500'


class StockX115530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115530'


class StockX115570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115570'


class StockX115610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115610'


class StockX115960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x115960'


class StockX117580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x117580'


class StockX117670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x117670'


class StockX117730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x117730'


class StockX118000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x118000'


class StockX118990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x118990'


class StockX119500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x119500'


class StockX119610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x119610'


class StockX119650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x119650'


class StockX119830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x119830'


class StockX119850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x119850'


class StockX119860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x119860'


class StockX120030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x120030'


class StockX120110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x120110'


class StockX120240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x120240'


class StockX121440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x121440'


class StockX121600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x121600'


class StockX121800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x121800'


class StockX121850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x121850'


class StockX121890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x121890'


class StockX122310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122310'


class StockX122350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122350'


class StockX122450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122450'


class StockX122640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122640'


class StockX122690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122690'


class StockX122870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122870'


class StockX122900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122900'


class StockX122990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x122990'


class StockX123010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123010'


class StockX123040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123040'


class StockX123330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123330'


class StockX123410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123410'


class StockX123420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123420'


class StockX123570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123570'


class StockX123690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123690'


class StockX123700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123700'


class StockX123750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123750'


class StockX123840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123840'


class StockX123860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123860'


class StockX123890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x123890'


class StockX124500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x124500'


class StockX124560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x124560'


class StockX125210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x125210'


class StockX126340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x126340'


class StockX126560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x126560'


class StockX126600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x126600'


class StockX126640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x126640'


class StockX126700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x126700'


class StockX126870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x126870'


class StockX126880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x126880'


class StockX127120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x127120'


class StockX127160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x127160'


class StockX127710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x127710'


class StockX128540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x128540'


class StockX128660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x128660'


class StockX128820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x128820'


class StockX128940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x128940'


class StockX129260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x129260'


class StockX129890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x129890'


class StockX130500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x130500'


class StockX130580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x130580'


class StockX130660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x130660'


class StockX130740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x130740'


class StockX131030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131030'


class StockX131090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131090'


class StockX131100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131100'


class StockX131180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131180'


class StockX131220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131220'


class StockX131290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131290'


class StockX131370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131370'


class StockX131390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131390'


class StockX131400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131400'


class StockX131760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131760'


class StockX131970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x131970'


class StockX133750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x133750'


class StockX133820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x133820'


class StockX134060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x134060'


class StockX134380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x134380'


class StockX134580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x134580'


class StockX134790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x134790'


class StockX136480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x136480'


class StockX136490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x136490'


class StockX136510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x136510'


class StockX136540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x136540'


class StockX137400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x137400'


class StockX137940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x137940'


class StockX137950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x137950'


class StockX138040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138040'


class StockX138070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138070'


class StockX138080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138080'


class StockX138250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138250'


class StockX138360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138360'


class StockX138490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138490'


class StockX138580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138580'


class StockX138610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138610'


class StockX138690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138690'


class StockX138930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x138930'


class StockX139050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x139050'


class StockX139130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x139130'


class StockX139480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x139480'


class StockX139670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x139670'


class StockX140070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x140070'


class StockX140410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x140410'


class StockX140520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x140520'


class StockX140670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x140670'


class StockX140860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x140860'


class StockX141000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x141000'


class StockX141020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x141020'


class StockX141070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x141070'


class StockX141080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x141080'


class StockX142210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x142210'


class StockX142280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x142280'


class StockX142760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x142760'


class StockX143160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x143160'


class StockX143210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x143210'


class StockX143240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x143240'


class StockX143540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x143540'


class StockX144510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x144510'


class StockX144620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x144620'


class StockX144960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x144960'


class StockX145020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x145020'


class StockX145210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x145210'


class StockX145720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x145720'


class StockX145990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x145990'


class StockX147760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x147760'


class StockX147830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x147830'


class StockX148140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x148140'


class StockX148150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x148150'


class StockX148250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x148250'


class StockX149950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x149950'


class StockX149980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x149980'


class StockX150840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x150840'


class StockX150900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x150900'


class StockX151860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x151860'


class StockX151910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x151910'


class StockX153460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x153460'


class StockX153490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x153490'


class StockX153710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x153710'


class StockX154030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x154030'


class StockX154040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x154040'


class StockX155650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x155650'


class StockX155660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x155660'


class StockX156100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x156100'


class StockX158310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x158310'


class StockX158430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x158430'


class StockX159580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x159580'


class StockX159910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x159910'


class StockX160550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x160550'


class StockX160600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x160600'


class StockX160980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x160980'


class StockX161000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x161000'


class StockX161390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x161390'


class StockX161570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x161570'


class StockX161580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x161580'


class StockX161890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x161890'


class StockX163560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x163560'


class StockX163730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x163730'


class StockX164060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x164060'


class StockX166090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x166090'


class StockX166480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x166480'


class StockX168330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x168330'


class StockX169330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x169330'


class StockX170030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x170030'


class StockX170790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x170790'


class StockX170900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x170900'


class StockX170920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x170920'


class StockX171010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x171010'


class StockX171090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x171090'


class StockX171120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x171120'


class StockX173130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x173130'


class StockX173940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x173940'


class StockX174880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x174880'


class StockX174900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x174900'


class StockX175140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x175140'


class StockX175250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x175250'


class StockX175330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x175330'


class StockX176440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x176440'


class StockX177350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x177350'


class StockX177830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x177830'


class StockX178320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x178320'


class StockX178780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x178780'


class StockX178920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x178920'


class StockX179290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x179290'


class StockX179900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x179900'


class StockX180400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x180400'


class StockX180640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x180640'


class StockX181340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x181340'


class StockX181710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x181710'


class StockX182360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x182360'


class StockX182400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x182400'


class StockX182690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x182690'


class StockX183190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x183190'


class StockX183300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x183300'


class StockX183490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x183490'


class StockX184230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x184230'


class StockX185490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x185490'


class StockX185750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x185750'


class StockX186230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x186230'


class StockX187220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x187220'


class StockX187270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x187270'


class StockX187420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x187420'


class StockX187790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x187790'


class StockX187870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x187870'


class StockX189300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x189300'


class StockX189330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x189330'


class StockX189690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x189690'


class StockX189860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x189860'


class StockX189980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x189980'


class StockX190510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x190510'


class StockX190650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x190650'


class StockX191410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x191410'


class StockX191420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x191420'


class StockX192080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192080'


class StockX192250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192250'


class StockX192390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192390'


class StockX192400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192400'


class StockX192410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192410'


class StockX192440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192440'


class StockX192650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192650'


class StockX192820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x192820'


class StockX193250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x193250'


class StockX194370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x194370'


class StockX194480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x194480'


class StockX194700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x194700'


class StockX195440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x195440'


class StockX195500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x195500'


class StockX195870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x195870'


class StockX195990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x195990'


class StockX196170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x196170'


class StockX196300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x196300'


class StockX196450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x196450'


class StockX196490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x196490'


class StockX196700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x196700'


class StockX197140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x197140'


class StockX198080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x198080'


class StockX198440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x198440'


class StockX199820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x199820'


class StockX200130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x200130'


class StockX200230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x200230'


class StockX200470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x200470'


class StockX200670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x200670'


class StockX200710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x200710'


class StockX200780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x200780'


class StockX200880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x200880'


class StockX201490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x201490'


class StockX203450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x203450'


class StockX203650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x203650'


class StockX203690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x203690'


class StockX204020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x204020'


class StockX204270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x204270'


class StockX204320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x204320'


class StockX204620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x204620'


class StockX204630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x204630'


class StockX204840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x204840'


class StockX205100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x205100'


class StockX205470(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x205470'


class StockX205500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x205500'


class StockX206400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x206400'


class StockX206560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x206560'


class StockX206640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x206640'


class StockX206650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x206650'


class StockX207760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x207760'


class StockX207940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x207940'


class StockX208140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x208140'


class StockX208340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x208340'


class StockX208350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x208350'


class StockX208370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x208370'


class StockX208640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x208640'


class StockX208710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x208710'


class StockX208860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x208860'


class StockX210540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x210540'


class StockX210980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x210980'


class StockX211270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x211270'


class StockX212560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x212560'


class StockX213090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x213090'


class StockX213420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x213420'


class StockX213500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x213500'


class StockX214150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214150'


class StockX214180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214180'


class StockX214260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214260'


class StockX214270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214270'


class StockX214310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214310'


class StockX214320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214320'


class StockX214330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214330'


class StockX214370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214370'


class StockX214390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214390'


class StockX214420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214420'


class StockX214430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214430'


class StockX214450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214450'


class StockX214610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214610'


class StockX214680(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214680'


class StockX214870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x214870'


class StockX215000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215000'


class StockX215090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215090'


class StockX215100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215100'


class StockX215200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215200'


class StockX215360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215360'


class StockX215380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215380'


class StockX215480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215480'


class StockX215600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215600'


class StockX215790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x215790'


class StockX216050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x216050'


class StockX216080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x216080'


class StockX217190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217190'


class StockX217270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217270'


class StockX217330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217330'


class StockX217480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217480'


class StockX217500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217500'


class StockX217600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217600'


class StockX217620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217620'


class StockX217730(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217730'


class StockX217820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x217820'


class StockX218150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x218150'


class StockX218410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x218410'


class StockX219130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x219130'


class StockX219420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x219420'


class StockX219550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x219550'


class StockX219750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x219750'


class StockX220100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x220100'


class StockX220180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x220180'


class StockX220260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x220260'


class StockX220630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x220630'


class StockX221610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x221610'


class StockX221840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x221840'


class StockX221980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x221980'


class StockX222040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x222040'


class StockX222080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x222080'


class StockX222110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x222110'


class StockX222420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x222420'


class StockX222800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x222800'


class StockX222810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x222810'


class StockX222980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x222980'


class StockX223250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x223250'


class StockX223310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x223310'


class StockX224060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x224060'


class StockX224110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x224110'


class StockX225190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x225190'


class StockX225220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x225220'


class StockX225330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x225330'


class StockX225430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x225430'


class StockX225530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x225530'


class StockX225570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x225570'


class StockX225590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x225590'


class StockX226320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226320'


class StockX226330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226330'


class StockX226340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226340'


class StockX226350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226350'


class StockX226360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226360'


class StockX226400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226400'


class StockX226440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226440'


class StockX226950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x226950'


class StockX227100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x227100'


class StockX227610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x227610'


class StockX227840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x227840'


class StockX227950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x227950'


class StockX228340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x228340'


class StockX228670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x228670'


class StockX228760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x228760'


class StockX228850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x228850'


class StockX229000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x229000'


class StockX229640(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x229640'


class StockX230240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x230240'


class StockX230360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x230360'


class StockX230980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x230980'


class StockX232140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x232140'


class StockX234080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x234080'


class StockX234100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x234100'


class StockX234300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x234300'


class StockX234340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x234340'


class StockX234690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x234690'


class StockX234920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x234920'


class StockX235980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x235980'


class StockX236200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x236200'


class StockX236810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x236810'


class StockX237690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x237690'


class StockX237750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x237750'


class StockX237820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x237820'


class StockX237880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x237880'


class StockX238090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x238090'


class StockX238120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x238120'


class StockX238200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x238200'


class StockX238490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x238490'


class StockX239340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x239340'


class StockX239610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x239610'


class StockX239890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x239890'


class StockX240810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x240810'


class StockX241520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241520'


class StockX241560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241560'


class StockX241590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241590'


class StockX241690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241690'


class StockX241710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241710'


class StockX241770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241770'


class StockX241790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241790'


class StockX241820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241820'


class StockX241840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x241840'


class StockX242040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x242040'


class StockX243070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x243070'


class StockX243840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x243840'


class StockX244460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x244460'


class StockX244920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x244920'


class StockX245620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x245620'


class StockX246690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x246690'


class StockX246710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x246710'


class StockX246720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x246720'


class StockX246960(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x246960'


class StockX247540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x247540'


class StockX247660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x247660'


class StockX248070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x248070'


class StockX248170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x248170'


class StockX249420(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x249420'


class StockX250000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x250000'


class StockX250060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x250060'


class StockX250930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x250930'


class StockX251270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x251270'


class StockX251370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x251370'


class StockX251630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x251630'


class StockX251970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x251970'


class StockX252500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x252500'


class StockX252990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x252990'


class StockX253450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x253450'


class StockX253590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x253590'


class StockX253840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x253840'


class StockX254120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x254120'


class StockX255220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x255220'


class StockX255440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x255440'


class StockX256150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x256150'


class StockX256630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x256630'


class StockX256840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x256840'


class StockX256940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x256940'


class StockX257370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x257370'


class StockX258610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x258610'


class StockX258790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x258790'


class StockX258830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x258830'


class StockX259630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x259630'


class StockX260660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x260660'


class StockX260930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x260930'


class StockX261200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x261200'


class StockX262260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x262260'


class StockX262840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x262840'


class StockX263020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263020'


class StockX263050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263050'


class StockX263540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263540'


class StockX263600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263600'


class StockX263690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263690'


class StockX263700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263700'


class StockX263720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263720'


class StockX263750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263750'


class StockX263770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263770'


class StockX263800(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263800'


class StockX263810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263810'


class StockX263860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263860'


class StockX263920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x263920'


class StockX264450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x264450'


class StockX264660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x264660'


class StockX264850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x264850'


class StockX264900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x264900'


class StockX265520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x265520'


class StockX265560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x265560'


class StockX265740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x265740'


class StockX267250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267250'


class StockX267260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267260'


class StockX267270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267270'


class StockX267290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267290'


class StockX267320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267320'


class StockX267790(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267790'


class StockX267850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267850'


class StockX267980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x267980'


class StockX268280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x268280'


class StockX268600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x268600'


class StockX269620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x269620'


class StockX270520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x270520'


class StockX270870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x270870'


class StockX271560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x271560'


class StockX271980(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x271980'


class StockX272110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x272110'


class StockX272210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x272210'


class StockX272290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x272290'


class StockX272450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x272450'


class StockX272550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x272550'


class StockX273060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x273060'


class StockX274090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x274090'


class StockX275630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x275630'


class StockX277070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x277070'


class StockX277410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x277410'


class StockX277810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x277810'


class StockX277880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x277880'


class StockX278280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x278280'


class StockX278650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x278650'


class StockX279600(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x279600'


class StockX280360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x280360'


class StockX281740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x281740'


class StockX281820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x281820'


class StockX282330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x282330'


class StockX282690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x282690'


class StockX282880(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x282880'


class StockX284620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x284620'


class StockX284740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x284740'


class StockX285130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x285130'


class StockX285490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x285490'


class StockX286750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x286750'


class StockX286940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x286940'


class StockX287410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x287410'


class StockX288330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x288330'


class StockX288620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x288620'


class StockX289010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x289010'


class StockX289080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x289080'


class StockX289220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x289220'


class StockX290120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290120'


class StockX290270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290270'


class StockX290380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290380'


class StockX290510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290510'


class StockX290520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290520'


class StockX290550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290550'


class StockX290650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290650'


class StockX290660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290660'


class StockX290670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290670'


class StockX290690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290690'


class StockX290720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290720'


class StockX290740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x290740'


class StockX291230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x291230'


class StockX291650(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x291650'


class StockX293480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x293480'


class StockX293490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x293490'


class StockX293580(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x293580'


class StockX293780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x293780'


class StockX294090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x294090'


class StockX294140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x294140'


class StockX294570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x294570'


class StockX294630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x294630'


class StockX294870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x294870'


class StockX297090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x297090'


class StockX297570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x297570'


class StockX297890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x297890'


class StockX298000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298000'


class StockX298020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298020'


class StockX298040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298040'


class StockX298050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298050'


class StockX298060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298060'


class StockX298380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298380'


class StockX298540(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298540'


class StockX298690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x298690'


class StockX299030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x299030'


class StockX299170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x299170'


class StockX299660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x299660'


class StockX299900(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x299900'


class StockX299910(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x299910'


class StockX300080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x300080'


class StockX300120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x300120'


class StockX300720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x300720'


class StockX301300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x301300'


class StockX302430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x302430'


class StockX302440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x302440'


class StockX302550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x302550'


class StockX303030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x303030'


class StockX304100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x304100'


class StockX304840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x304840'


class StockX305090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x305090'


class StockX306040(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x306040'


class StockX306200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x306200'


class StockX306620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x306620'


class StockX307070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307070'


class StockX307160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307160'


class StockX307180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307180'


class StockX307280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307280'


class StockX307750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307750'


class StockX307870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307870'


class StockX307930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307930'


class StockX307950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x307950'


class StockX308100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x308100'


class StockX308170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x308170'


class StockX309930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x309930'


class StockX310200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x310200'


class StockX310840(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x310840'


class StockX310870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x310870'


class StockX311270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x311270'


class StockX311390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x311390'


class StockX311690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x311690'


class StockX312610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x312610'


class StockX313750(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x313750'


class StockX313760(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x313760'


class StockX314130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x314130'


class StockX314930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x314930'


class StockX316140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x316140'


class StockX317030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317030'


class StockX317120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317120'


class StockX317240(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317240'


class StockX317320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317320'


class StockX317330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317330'


class StockX317400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317400'


class StockX317530(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317530'


class StockX317690(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317690'


class StockX317770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317770'


class StockX317830(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317830'


class StockX317850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317850'


class StockX317870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x317870'


class StockX318000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x318000'


class StockX318010(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x318010'


class StockX318020(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x318020'


class StockX318410(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x318410'


class StockX319400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x319400'


class StockX319660(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x319660'


class StockX320000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x320000'


class StockX321260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x321260'


class StockX321550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x321550'


class StockX321820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x321820'


class StockX322000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x322000'


class StockX322180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x322180'


class StockX322310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x322310'


class StockX322510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x322510'


class StockX322780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x322780'


class StockX323210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x323210'


class StockX323230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x323230'


class StockX323280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x323280'


class StockX323940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x323940'


class StockX323990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x323990'


class StockX326030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x326030'


class StockX327260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x327260'


class StockX328380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x328380'


class StockX329560(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x329560'


class StockX330350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x330350'


class StockX330860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x330860'


class StockX330990(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x330990'


class StockX331380(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x331380'


class StockX331520(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x331520'


class StockX331920(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x331920'


class StockX332290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x332290'


class StockX332370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x332370'


class StockX332570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x332570'


class StockX332710(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x332710'


class StockX333050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x333050'


class StockX333430(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x333430'


class StockX333620(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x333620'


class StockX334970(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x334970'


class StockX335810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x335810'


class StockX335870(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x335870'


class StockX335890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x335890'


class StockX336060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x336060'


class StockX336260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x336260'


class StockX336370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x336370'


class StockX336570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x336570'


class StockX337450(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x337450'


class StockX337930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x337930'


class StockX338220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x338220'


class StockX339770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x339770'


class StockX339950(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x339950'


class StockX340120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x340120'


class StockX340350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x340350'


class StockX340360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x340360'


class StockX340440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x340440'


class StockX340570(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x340570'


class StockX340930(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x340930'


class StockX341160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x341160'


class StockX342550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x342550'


class StockX343510(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x343510'


class StockX344050(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x344050'


class StockX344820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x344820'


class StockX347000(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x347000'


class StockX347140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x347140'


class StockX347700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x347700'


class StockX347740(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x347740'


class StockX347770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x347770'


class StockX347860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x347860'


class StockX347890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x347890'


class StockX348030(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x348030'


class StockX348150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x348150'


class StockX348210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x348210'


class StockX348350(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x348350'


class StockX349720(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x349720'


class StockX351320(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x351320'


class StockX351330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x351330'


class StockX351340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x351340'


class StockX352480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x352480'


class StockX352700(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x352700'


class StockX352770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x352770'


class StockX352820(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x352820'


class StockX352940(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x352940'


class StockX353060(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x353060'


class StockX353070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x353070'


class StockX353190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x353190'


class StockX353200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x353200'


class StockX353490(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x353490'


class StockX353810(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x353810'


class StockX354200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x354200'


class StockX355150(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x355150'


class StockX356860(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x356860'


class StockX356890(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x356890'


class StockX357230(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x357230'


class StockX357550(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x357550'


class StockX357780(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x357780'


class StockX359090(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x359090'


class StockX361390(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x361390'


class StockX361610(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x361610'


class StockX361670(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x361670'


class StockX363260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x363260'


class StockX363280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x363280'


class StockX365590(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x365590'


class StockX366330(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x366330'


class StockX367340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x367340'


class StockX367360(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x367360'


class StockX367460(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x367460'


class StockX367480(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x367480'


class StockX368770(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x368770'


class StockX369370(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x369370'


class StockX372290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x372290'


class StockX373200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x373200'


class StockX373340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x373340'


class StockX375500(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x375500'


class StockX377400(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x377400'


class StockX377630(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x377630'


class StockX378850(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x378850'


class StockX380440(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x380440'


class StockX383220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x383220'


class StockX900070(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900070'


class StockX900080(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900080'


class StockX900100(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900100'


class StockX900110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900110'


class StockX900120(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900120'


class StockX900140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900140'


class StockX900250(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900250'


class StockX900260(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900260'


class StockX900270(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900270'


class StockX900280(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900280'


class StockX900290(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900290'


class StockX900300(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900300'


class StockX900310(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900310'


class StockX900340(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x900340'


class StockX950110(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950110'


class StockX950130(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950130'


class StockX950140(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950140'


class StockX950160(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950160'


class StockX950170(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950170'


class StockX950180(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950180'


class StockX950190(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950190'


class StockX950200(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950200'


class StockX950210(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950210'


class StockX950220(models.Model):
    
    date = models.DateField(blank=True, primary_key = True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'stock_x950220'
