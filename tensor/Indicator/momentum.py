import pandas as pd
import ta.momentum as mom

# Stochastic RSI
def get_srsi(df):
    df_srsi = pd.DataFrame()

    indicator_srsi = mom.stochrsi(close=df['close'])

    df_srsi['srsi'] = indicator_srsi.fillna(0)

    return df_srsi*100

# Relative Strength Index
def get_rsi(df):
    df_rsi = pd.DataFrame()

    indicator_rsi = mom.rsi(close=df['close'])

    df_rsi['rsi'] = indicator_rsi.fillna(0)

    return df_rsi

# True strength index
def get_tsi(df):
    df_tsi = pd.DataFrame()

    indicator_tsi = mom.tsi(close=df['close'])

    df_tsi['tsi'] = indicator_tsi.fillna(-50)

    return df_tsi

# Ultimate Oscillator
def get_uo(df):
    df_uo = pd.DataFrame()

    indicator_uo = mom.ultimate_oscillator(high=df['high'], low=df['low'],
    close=df['close'])

    df_uo['uo'] = indicator_uo.fillna(0)

    return df_uo

# Stochastic Oscillator
def get_sr(df):
    df_sr = pd.DataFrame()
    indicator_sr = mom.StochasticOscillator(high=df['high'], low=df['low'],
    close=df['close'])

    df_sr['sr_signal'] = indicator_sr.stoch_signal()
    df_sr['sr_stoch'] = indicator_sr.stoch()

    return df_sr

# Williams %R
def get_wr(df):
    df_wr = pd.DataFrame()

    indicator_wr = mom.williams_r(high=df['high'], low=df['low'],
    close=df['close'])

    df_wr['wr'] = indicator_wr.fillna(0)

    return df_wr

# Kaufman's Adaptive Moving Average
def get_kama(df):
    df_kama = pd.DataFrame()

    indicator_kama = mom.kama(close=df['close'])

    df_kama['kama'] = indicator_kama
    df_kama['kama'] = df_kama['kama'].fillna(df_kama['kama'][10])

    return df_kama

# Percentage Price Oscillator
def get_ppo(df):
    df_ppo = pd.DataFrame()

    indicator_ppo = mom.ppo(close=df['close'])

    df_ppo['ppo'] = indicator_ppo.fillna(0)

    return df_ppo



# abc = get_ppo(df)

# plt.figure()
# plt.plot(abc)
# plt.show()