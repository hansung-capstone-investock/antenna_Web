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
        fields = ('id',
                'name',
                'group',
                'company1',
                'company2',
                'company3',
                'company4',
                'company5',
                'company6',
                'company7',
                'company8',
                'company9',
                'company10',
                )