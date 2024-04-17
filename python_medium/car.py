import pandas as pd
import numpy as np
from datetime import datetime

df_2020 = car_launches[car_launches['year'].astype(str) == '2020']
df_2019 = car_launches[car_launches['year'].astype(str) == '2019']
df = pd.merge(df_2020, df_2019, how='outer', on=[
    'company_name'], suffixes=['_2020', '_2019']).fillna(0)
df = df[df['product_name_2020'] != df['product_name_2019']]
df = df.groupby(['company_name']).agg(
    {'product_name_2020': 'nunique', 'product_name_2019': 'nunique'}).reset_index()
df['net_new_products'] = df['product_name_2020'] - df['product_name_2019']
result = df[['company_name', 'net_new_products']]
