from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountData
        fields = ('id',
                'password')

class InterestedstockSerializer(serializers.ModelSerializer):
    class Meta:
        model = interestedstockData
        fields = ('name',
                'company',
                'group')