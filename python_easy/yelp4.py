# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

df = yelp_business[yelp_business['is_open'] == 1]
df_count = len(df)