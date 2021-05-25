from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import pandas as pd
import datetime as dt
import urllib.request as req
from urllib import parse
import requests
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from stock.serializers import *

@api_view(['POST'])
def backtesting_api(request):
    if request.method == 'POST':
        # 입력조건
        request.data['운용자금']
        request.data['운용기간 시작']
        request.data['운용기간 끝']
        request.data['시장']
        # kospi, kosdaq
        request.data['업종']
        # "업종" : ["it", "철강", "석유"]
        max = request.data['최대 종목 보유수']

        # 매수조건 / 우선순위
        request.data['체크박스']
        
        주가데이터 = stockData.objects.filter(date__range = ["운용기간 시작", "운용기간 끝"],
                                            date__day = "01"
        ) & 지표데이터.objects.filter(per__range = ["1", "10"], pbr__range = ["0.3", "1"]
        ) & stockList.objects.filter(시장 = "kospi"
        ) & sectorList.objects.filter(업종 = ["화학", "기계", "의약품"]
        ).order_by('date_joined')[:max]
        # 오름차순


        주가데이터_serializer = 주가Serializer(주가데이터, many=True)
        # id = 주가데이터_serializer.data[0]['id']

        # 수익률 계산

        # 3월 시작이라면, 3월01일 가격과 4월01의 가격을 비교
        # 수익률을 각 종목마다 딕셔너리 형태로 저장

        return JsonResponse(주가데이터_serializer)


@api_view(['POST'])
def tensorflow_api(request):
    if request.method == 'POST':
        # 입력조건
        종목 = request.data['종목']
        예측날짜 = request.data['예측날짜']
        # 7일, 15일, 30일

        request.data['모델']
        # RNN, LSTM, GRU

        request.data['지표 체크박스']
        
        종목데이터 = stockList.objects.get(종목명 = 종목)

        종목데이터_serializer = 주가Serializer(종목데이터, many=True)
        code = 종목데이터_serializer.data[0]['code']

        result = tensorflow(code, 예측날짜)
        # 이미지 파일로 받아서

        return HttpResponse(result, content="image/png")