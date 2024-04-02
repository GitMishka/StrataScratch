import pandas as pd 
import datetime as dt
import numpy as np

df = pd.merge(facebook_web_log.loc[facebook_web_log['action'] == 'page_load', ['user_id', 'timestamp']],
            facebook_web_log.loc[facebook_web_log['action'] == 'page_exit', ['user_id', 'timestamp']],
            how='left', on='user_id', suffixes=['_load', '_exit']).dropna()


df['date_load'] = pd.to_datetime(df['timestamp_load']).dt.date
df = df[df['timestamp_load'] < df['timestamp_exit']]
df = df.groupby(['user_id', 'date_load']).agg({'timestamp_load': 'max', 'timestamp_exit': 'min'}).reset_index()

df['duration'] = df['timestamp_exit'] - df['timestamp_load']
df = df[df['duration'] > '0 days']
result = df.groupby('user_id')['duration'].agg(lambda x: np.mean(x)).reset_index()
