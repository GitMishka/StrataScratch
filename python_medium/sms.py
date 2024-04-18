import pandas as pd
import numpy as np

df = fb_sms_sends[["ds","type","phone_number"]]
df1 = df[df["type"] == 'message']
df1_grouped = df1.groupby('ds')['phone_number'].count().reset_index(name='count')
df1_grouped_0804 = df1_grouped[df1_grouped['ds']=='08-04-2020']
df2 = fb_confirmers[["date","phone_number"]]
df3 = pd.merge(df1,df2, how ='left',left_on =["phone_number","ds"], right_on = ["phone_number","date"])
df3_grouped = df3.groupby('date')['phone_number'].count().reset_index(name='confirmed_count')
df3_grouped_0804 = df3_grouped[df3_grouped['date']=='08-04-2020']
result = (float(df3_grouped_0804['confirmed_count'])/df1_grouped_0804['count'])*100
