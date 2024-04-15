import pandas as pd
import numpy as np

df = pd.merge(lyft_users, lyft_rides_log, left_on='id', right_on='user_id')
result = df.groupby(['user_id', 'name'])['distance'].sum().to_frame().sort_values(by = 'distance', ascending = False).reset_index()
result['rank'] = result['distance'].rank(ascending = False)
result[result['rank']<=10][['user_id', 'name', 'distance']]