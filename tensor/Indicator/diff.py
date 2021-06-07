import numpy as np 
import pandas as pd

def get_diff(df):
    df_diff = pd.DataFrame()
    # 전일비
    df_diff['diff'] = df.diff()['close']
    # 증감률
    df_diff['diff_rate'] = df_diff['diff'] / df['close']
    df_diff = df_diff.fillna(0)
    
    return df_diff['diff'], df_diff['diff_rate']