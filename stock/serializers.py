from rest_framework import serializers
from .models import *

class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = stockList
        fields = ('code',
                'name',
                'last_update'
                )

class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = stockInfo
        fields = ('code',
                'date',
                'closingPrice',
                'openPrice',
                'highPrice',
                'lowPrice',
                'marketCap',
                'tradingVolume'
                )

class marketInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = marketInfo
        fields = ('name',
                'score',
                'tradingVolume',
                'high',
                'low'
                )

class marketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = marketList
        fiels = ("name"
                )        
