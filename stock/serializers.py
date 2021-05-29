from rest_framework import serializers
from .models import *

class StockSeirializer(serializers.Serializer):
    date= serializers.DateField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()
    volume = serializers.FloatField()
    
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