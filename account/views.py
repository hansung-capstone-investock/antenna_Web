from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
from bs4 import BeautifulSoup
import requests
import json
from kiwipiepy import Kiwi, Option
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.serializers import *


# Create your views here.
@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        account = accountData.objects.all()
        account_serializer = AccountSerializer(account, many=True)
        return Response(account_serializer.data)

    elif request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)
        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)
        return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        userid = request.data['id']
        userpw = request.data['password']

        account = accountData.objects.filter(id=userid, password=userpw)
        account_serializer = AccountSerializer(account, many=True)
        try:
            id = account_serializer.data[0]['id']
            password = account_serializer.data[0]['password']
        except IndexError:
            return JsonResponse({"code": "1001", "msg": "로그인 실패하셨습니다."}, status=200)
        if (id, password) == (userid, userpw):
            return JsonResponse({"code": "0000", "msg": "로그인 성공하셨습니다."}, status=200)

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)

        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse({"code": "0000", "msg": "회원가입 성공하셨습니다."}, status=200)
        else:
            return JsonResponse({"code": "1001", "msg": "회원가입 실패하셨습니다."}, status=200)

@api_view(['POST'])
def interestedstock_Update(request):
    if request.method == 'POST':
        interested_serializer = InterestedstockSerializer(data=request.data)
        
        if interested_serializer.is_valid():
            interested_serializer.save()
            return JsonResponse({"code": "0000", "msg": "관심종목이 추가되었습니다."}, status=200)
        else:
            return JsonResponse({"code": "1002", "msg": "관심종목 추가가 실패하였습니다."}, status=200)

@api_view(['GET'])
def interestedgroup_list(request):
    if request.method == 'GET':
        intersted = interestedstockData.objects.all()
        intersted_serializer = InterestedstockSerializer(intersted, many=True)
        
        return JsonResponse(intersted_serializer.data)