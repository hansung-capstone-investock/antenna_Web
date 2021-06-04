import pandas as pd
import ta.volatility as vola
import matplotlib.pyplot as plt 

# Open, High, Low, Volume, Close
xy = pd.read_csv('C:/Users/hansung/Capstone/tensorflow/LG_chemical.csv')
xy = xy.to_numpy()

df = pd.DataFrame(xy, columns=['open','high', 'low','volume','close'])

# Average True Range
def get_atr(df):
    df_atr = pd.DataFrame()

    indicator_atr = vola.average_true_range(high=df['high'], low=df['low'],
    close=df['close'])

    df_atr['atr'] = indicator_atr

    return df_atr


def get_bolinger(df):
    df_bolinger = pd.DataFrame()
    # Initialize Bollinger Bands Indicator
    indicator_bb = vola.BollingerBands(close=df["close"], window=20, window_dev=2)

    # Add Bollinger Bands features
    df_bolinger['bb_bbm'] = indicator_bb.bollinger_mavg()
    df_bolinger = df_bolinger.fillna(df['close'][0])
    
    return df_bolinger

# Keltner Channel
def get_kc(df):
    df_kc = pd.DataFrame()


    indicator_kc = vola.KeltnerChannel(high=df['high'], low=df['low'],
    close=df['close'])

    df_kc['kc_lb'] = indicator_kc.keltner_channel_lband()

    return df_kc

# Donchian Channel
def get_dc(df):
    df_dc = pd.DataFrame()

    indicator_dc = vola.DonchianChannel(high=df['high'], low=df['low'],
    close=df['close'])

    df_dc['dc_mb'] = indicator_dc.donchian_channel_mband()
    df_dc['dc_mb'] = df_dc['dc_mb'].fillna(df_dc['dc_mb'][20])

    return df_dc

# Ulcer Index
def get_ui(df):
    df_ui = pd.DataFrame()

    indicator_ui = vola.ulcer_index(close=df['close'])

    df_ui['ui'] = indicator_ui.fillna(0)

    return df_ui

# abc = get_ui(df)

# plt.figure()
# plt.plot(abc)
# plt.show()