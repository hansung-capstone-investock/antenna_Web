from rest_framework import serializers
from .models import *

class CompareSerializer(serializers.Serializer):
    date = serializers.DateField()
    stockcode1 = serializers.CharField()
    gap1 = serializers.FloatField()
    stockcode2 = serializers.CharField()
    gap2 = serializers.FloatField()
    stockcode3 = serializers.CharField()
    gap3 = serializers.FloatField()
    stockcode4 = serializers.CharField()
    gap4 = serializers.FloatField()
    stockcode5 = serializers.CharField()
    gap5 = serializers.FloatField()
    stockcode6 = serializers.CharField()
    gap6 = serializers.FloatField()
    stockcode7 = serializers.CharField()
    gap7 = serializers.FloatField()
    stockcode8 = serializers.CharField()
    gap8 = serializers.FloatField()
    stockcode9 = serializers.CharField()
    gap9 = serializers.FloatField()
    stockcode10 = serializers.CharField()
    gap10 = serializers.FloatField()

class BackTestSerializer(serializers.Serializer):
    date= serializers.DateField()
    # open = serializers.FloatField()
    # high = serializers.FloatField()
    # low = serializers.FloatField()
    close = serializers.FloatField()
    per = serializers.FloatField()
    pbr = serializers.FloatField()
    psr = serializers.FloatField()
    roe = serializers.FloatField()
    roa = serializers.FloatField()
    
class StockSerializer(serializers.Serializer):
    date= serializers.DateField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()
    per = serializers.FloatField()
    pbr = serializers.FloatField()
    psr = serializers.FloatField()
    roe = serializers.FloatField()
    roa = serializers.FloatField()
    volume = serializers.FloatField()
    cap = serializers.FloatField()

class MarketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketList
        fields = ('id',
                'market')
        
class SectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorList
        fields = ('sectorcode',
                'sector')

class ThemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemaList
        fields = ('themacode',
                'thema')
        
class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockList
        fields = ('code',
                'company',
                'market',
                'sectorcode',
                'themacode',
                'last_update',
                )

class KospiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Kospi
        fields = ('date',
                'close',
                )

class KosdaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kosdaq
        fields = ('date',
                'close',
                )
        
class Kospi200Serializer(serializers.ModelSerializer):
    class Meta:
        model = Kospi200
        fields = ('date',
                'close',
                )