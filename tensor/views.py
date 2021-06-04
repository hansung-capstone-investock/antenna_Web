from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import pandas as pd
import urllib.request as req
import requests
import json
from datetime import datetime, timedelta
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import tensorflow as tf 
import numpy as np 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from .Indicator import trend as trend
from .Indicator import volatiliy as vola
from .Indicator import volume as vol
from .Indicator import momentum as mom
from .Indicator import diff as diff
from stock.serializers import *

@api_view(['POST'])
def antenna_api(request):
    if request.method == 'POST':
        # 종목
        companyName = request.data['종목']
        # 7, 14, 21, 28일
        predictDate = request.data['예측날짜']
        # 보조지표
        indicator = request.data['보조지표']

        stockData = StockList.objects.using("stockDB").get(company = companyName)
        stock_serializer = StockSeirializer(stockData, many=True)
        code = stock_serializer.data['code']

        result = antenna_tensor(code, indicator, predictDate)

        return HttpResponse(result, content="image/png")

def get_stockdata(code):
    code = int(code)
    code = '{0:06d}'.format(code)
    nowDate = (datetime.now()-timedelta(1)).strftime('%Y-%m-%d')
    exeStr = 'StockX{0}.objects.using("stockDB").filter(date__range=["2018-01-01", "{1}"])'.format(code, nowDate)
    stockData = eval(exeStr)        
    stockData_serializer = StockSeirializer(stockData, many=True)
    return Response(stockData_serializer.data)

def antenna_tensor(code, indicator, predictDate):
    # train Parameters
    seqLength = 7 # window size 
    days_to_predict = predictDate
    batchsize = 16 
    iterations = 150
    indicator_count = len(indicator)

    xy_json = get_stockdata(code)
    # xy_json = json.load(xy_json)

    xy = pd.DataFrame(xy_json)
    del xy['date']
    df = xy.dropna()
    df['close'] = df['close'].shift(-days_to_predict)

    tf.random.set_seed(777)

    # 보조지표
    # 전일비, 등락률
    df_diff, df_diffrate = diff.get_diff(df)

    # Volume
    df_vpt = vol.get_vpt(df)        # 정상성  낫배드
    df_cmf = vol.get_cmf(df)        # 정상성
    df_eom = vol.get_eom(df)        # 정상성
    df_fi = vol.get_forceindex(df) # 정상성
    df_adi = vol.get_adi(df)        # 비정상성
    df_vwap = vol.get_vwap(df)       # 비정상성  굿

    # Volatility
    df_dc = vola.get_dc(df)        # 비정상성  낫배드
    df_kc = vola.get_kc(df)        # 비정상성    낫배드

    # # Momentum
    df_ppo = mom.get_ppo(df)        # 정상성
    df_rsi = mom.get_rsi(df)        # 정상성
    df_srsi = mom.get_srsi(df)       # 정상성
    df_tsi = mom.get_tsi(df)        # 정상성
    df_uo = mom.get_uo(df)         # 정상성
    df_wr = mom.get_wr(df)         # 정상성
    df_kama = mom.get_kama(df)       # 비정상성    굿

    # # Trend
    df_cci = trend.get_cci(df)      # 정상성
    df_dpo = trend.get_dpo(df)      # 정상성
    df_kst = trend.get_kst(df)      # 정상성
    df_stc = trend.get_stc(df)      # 정상성
    df_trix = trend.get_trix(df)     # 정상성
    df_macd = trend.get_macd(df)     # 정상성    
    df_wma = trend.get_wma(df)      # 비정상성    굿
    df_ema = trend.get_ema(df)      # 비정상성    굿

    df_input = pd.concat([indicator], axis=1)

    # 볼린저밴드
    df_bolinger = vola.get_bolinger(df)
    # df_bolinger = bolinger.get_bolinger(df)
    df_output = pd.DataFrame()
    # 정상성 데이터 = 종가 - 이동평균선
    # 비정상성 데이터의 정상성 데이터화
    df_output['data'] = df['close'] - df_bolinger['bb_bbm']

    # 입력변수 넣기
    input_data = df_input.to_numpy()
    # 출력변수
    output_data = df_output.to_numpy()            # 종가 - 볼린저밴드


    # train, test 크기 설정
    trainSize = int(len(input_data)*0.7)
    train_x = input_data[0:trainSize]
    test_x = input_data[trainSize-seqLength:]

    # y 값 출력변수
    trainSet = output_data[0:trainSize]
    testSet = output_data[trainSize-seqLength:]

    # 나중에 예측가에 다시 더해야할 값
    bolinger_y = df_bolinger[trainSize-seqLength:]
    bolinger_y = bolinger_y['bb_bbm'].to_numpy()
    bol_len = len(bolinger_y)
    bolinger_y = bolinger_y.reshape((bol_len,1))

    # 종가 - 볼린저밴드일 경우
    train_y = trainSet
    test_y = testSet

    # 훈련 데이터
    scalerX = MinMaxScaler()
    train_x = scalerX.fit_transform(train_x)
    test_x = scalerX.fit_transform(test_x)

    scalerY = MinMaxScaler()
    train_y = scalerY.fit_transform(train_y)
    test_y = scalerY.fit_transform(test_y)

    # build datasets
    def buildDataSetX(timeSeries, seqLength):
        data = []
        for i in range(0, len(timeSeries)-seqLength):
            tx = timeSeries[i:i+seqLength,:]
            data.append(tx)
        return np.array(data)

    def buildDataSetY(timeSeries, seqLength):
        data = []
        for i in range(0, len(timeSeries)-seqLength):
            ty = timeSeries[i+seqLength,[-1]]
            data.append(ty)
        return np.array(data)

    trainX = buildDataSetX(train_x, seqLength)
    testX = buildDataSetX(test_x, seqLength) 

    trainY = buildDataSetY(train_y, seqLength)
    testY = buildDataSetY(test_y, seqLength)


    from tensorflow import keras
    from tensorflow.keras import layers

    ########
    # LSTM #
    ########
    model = keras.Sequential()

    model.add(layers.LSTM(units=10, 
                                activation='relu',
                                input_shape=[7,indicator_count]))

    model.add(layers.Dense(1))
    model.summary()
    # 모델 학습과정 설정 
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    # 모델 트레이닝 
    hist = model.fit(trainX, trainY, epochs=iterations, batch_size=batchsize)

    yhat = model.predict(testX)

    predict = scalerY.inverse_transform(yhat)
    actual = scalerY.inverse_transform(testY)

    # 보정
    bolinger_y[-days_to_predict:] = bolinger_y[-days_to_predict-1]
    sum = predict[0] - actual[0]
    
    # 예측 결과, 실제 값
    predict = predict - sum + bolinger_y[seqLength:]
    actual = actual + bolinger_y[seqLength:]

    predict_list = predict.tolist()
    actual_list = actual.tolist()
    predict_dict = dict(zip(range(len(predict_list)), predict_list))
    actual_dict = dict(zip(range(len(actual_list)), actual_list))

    res_dict = {}

    res_dict['predict'] = predict_dict
    res_dict['actual'] = actual_dict

    # print(res_dict)
    predict_json = json.dumps(res_dict)

    return predict_json