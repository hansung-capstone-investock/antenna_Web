import pandas as pd
import ta.volume as vol

# Force Index
def get_forceindex(df):
    df_fi = pd.DataFrame()

    indicator_fi = vol.ForceIndexIndicator(close=df['close'], volume=df['volume'])

    df_fi['fi'] = indicator_fi.force_index().fillna(0)

    return df_fi

# Money Flow Index
def get_mfi(df):
    df_mfi = pd.DataFrame()

    indicator_mfi = vol.money_flow_index(high=df['high'], low=df['low'],
    close=df['close'], volume=df['volume'])

    df_mfi['mfi'] = indicator_mfi.fillna(0)

    return df_mfi

# Accumulation/Distribution Index
def get_adi(df):
    df_adi = pd.DataFrame()

    indicator_adi = vol.acc_dist_index(high=df['high'], low=df['low'],
    close=df['close'], volume=df['volume'])

    df_adi['adi'] = indicator_adi

    return df_adi

# On-Balace Volume
def get_obv(df):
    df_obv = pd.DataFrame()

    indicator_obv = vol.on_balance_volume(close=df['close'], volume=df['volume'])

    df_obv['obv'] = indicator_obv

    return df_obv

# Chaikin Money Flow
def get_cmf(df):
    df_cmf = pd.DataFrame()

    indicator_cmf = vol.chaikin_money_flow(high=df['high'], low=df['low'], 
    close=df['close'], volume=df['volume'])

    df_cmf['cmf'] = indicator_cmf.fillna(0)

    return df_cmf

# Ease of Movement
def get_eom(df):
    df_eom = pd.DataFrame()

    indicator_eom = vol.ease_of_movement(high=df['high'], low=df['low'], 
    volume=df['volume'])

    df_eom['eom'] = indicator_eom.fillna(0)

    return df_eom

# Volume-price Trend
def get_vpt(df):
    df_vpt = pd.DataFrame()

    indicator_vpt = vol.volume_price_trend(close=df['close'], volume=df['volume'])

    df_vpt['vpt'] = indicator_vpt

    return df_vpt

# Negative Volume Index
def get_nvi(df):
    df_nvi = pd.DataFrame()

    indicator_nvi = vol.negative_volume_index(close=df['close'], volume=df['volume'])

    df_nvi['nvi'] = indicator_nvi

    return df_nvi

# Volume Weighted Average Price
def get_vwap(df):
    df_vwap = pd.DataFrame()

    indicator_vwap = vol.volume_weighted_average_price(high=df['high'], low=df['low'], 
    close=df['close'], volume=df['volume'])

    df_vwap['vwap'] = indicator_vwap
    df_vwap['vwap'] = df_vwap['vwap'].fillna(df_vwap['vwap'][13])

    return df_vwap

# abc = get_mfi(df)

# plt.figure()
# plt.plot(abc)
# plt.show()