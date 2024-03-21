# Import your libraries
import pandas as pd

# Start writing code
yelp_checkin.head()
df = yelp_checkin.groupby(['business_id'])['checkins'].sum().to_frame('n').reset_index()
df_2 = df[df['n'].rank(method='min', ascending = False) <= 5]
#df_1 = yelp_checkin.rank(method='average')