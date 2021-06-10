import pandas as pd
import ta.trend as trend

# Exponential Moving Average
def get_ema(df):
    df_ema = pd.DataFrame()

    indicator_ema = trend.ema_indicator(close=df['close'])

    df_ema['ema'] = indicator_ema
    df_ema['ema'] = df_ema['ema'].fillna(df_ema['ema'][11])

    return df_ema

# Weighted Moving Average
def get_wma(df):
    df_wma = pd.DataFrame()

    indicator_wma = trend.wma_indicator(close=df['close'])

    df_wma['wma'] = indicator_wma
    df_wma['wma'] = df_wma['wma'].fillna(df_wma['wma'][10])

    return df_wma

# Moving Average Convergence Divergence
def get_macd(df):
    df_macd = pd.DataFrame()

    indicator_macd = trend.macd(close=df['close'])

    df_macd['macd'] = indicator_macd
    df_macd['macd'] = df_macd['macd'].fillna(df_macd['macd'][25])

    return df_macd

# Average Directional Movement Index
def get_adx(df):
    df_adx = pd.DataFrame()

    indicator_adx = trend.adx(high=df['high'], low=df['low'], 
    close=df['close'])

    df_adx['adx'] = indicator_adx

    return df_adx

# Vortex Indicator
def get_vi(df):
    df_vi = pd.DataFrame()

    indicator_vi = trend.VortexIndicator(high=df['high'], low=df['low'], 
    close=df['close'])

    df_vi['vi_pos'] = indicator_vi.vortex_indicator_pos().fillna(0)

    return df_vi

# Trix
def get_trix(df):
    df_trix = pd.DataFrame()

    indicator_trix = trend.trix(close=df['close'])

    df_trix['trix'] = indicator_trix.fillna(0)

    return df_trix

# Mass Index
def get_mi(df):
    df_mi = pd.DataFrame()

    indicator_mi = trend.mass_index(high=df['high'], low=df['low'])

    df_mi['mi'] = indicator_mi.fillna(25)

    return df_mi

# Commodity Channel Index
def get_cci(df):
    df_cci = pd.DataFrame()

    indicator_cci = trend.cci(high=df['high'], low=df['low'], 
    close=df['close'])

    df_cci['cci'] = indicator_cci.fillna(0)

    return df_cci

# Detrended Price Oscillator
def get_dpo(df):
    df_dpo = pd.DataFrame()

    indicator_dpo = trend.dpo(close=df['close'])

    df_dpo['dpo'] = indicator_dpo.fillna(0)

    return df_dpo

# KST Oscillator
def get_kst(df):
    df_kst = pd.DataFrame()

    indicator_kst = trend.KSTIndicator(close=df['close'])

    df_kst['kst'] = indicator_kst.kst().fillna(0)

    return df_kst


# Schaff Trend Cycle
def get_stc(df):
    df_stc = pd.DataFrame()

    indicator_stc = trend.STCIndicator(close=df['close'])

    df_stc['stc'] = indicator_stc.stc().fillna(0)

    return df_stc


# abc = get_stc(df)

# plt.figure()
# plt.plot(abc)
# plt.show()