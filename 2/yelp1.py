# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()

#bus_unique = yelp_reviews['business_name'].unique()


df_1 = yelp_reviews.groupby('stars').size().to_frame('count').reset_index().sort_values('count')