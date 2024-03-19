# Import your libraries
import pandas as pd

# Start writing code
airbnb_hosts.head()
merged_df = pd.merge(airbnb_hosts,airbnb_apartments,left_on = 'host_id', right_on = 'host_id')
filtered_df = merged_df[merged_df['nationality'] != merged_df['country']]
result  = filtered_df['host_id'].nunique()