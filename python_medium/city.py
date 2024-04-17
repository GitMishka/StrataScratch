import pandas as pd
import numpy as np

# Start writing code
zillow_transactions.head()

df_city = zillow_transactions.groupby('city')['mkt_price'].mean().reset_index(name='avg_price_by_city')
df_avg_price = zillow_transactions['mkt_price'].mean()
df1 = df_city[df_city['avg_price_by_city'] > df_avg_price].sort_values('city')
result = df1[['city']]