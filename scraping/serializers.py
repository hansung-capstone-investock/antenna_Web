from rest_framework import serializers
from .models import *

class MainNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainNews
        fields = ('title',
                'summary',
                'publishDay',
                'link')

class DcSerializer(serializers.ModelSerializer):
    class Meta:
        model = dcData
        fields = ('title',
                'count')

class FmkorSerializer(serializers.ModelSerializer):
    class Meta:
        model = fmkorData
        fields = ('title',
                'count')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = companyData
        fields = ('name',
                'code')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = accountData
        fields = ('id',
                'password')