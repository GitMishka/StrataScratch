# Import your libraries
import pandas as pd

# Start writing code
user_activity.head()

df = user_activity.groupby('device_type')['user_count'].max().reset_index()
sorted_df = user_activity.sort_values(['device_type', 'user_count'], ascending=[True, False])

df = sorted_df.groupby('device_type').first().reset_index()
df = df[['user_count','time_period','device_type']]