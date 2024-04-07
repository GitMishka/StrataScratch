# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()

#df = yelp_reviews['business_name'].str.contains("Lo-Lo's Chicken & Waffles").reset_index()

df_1 = yelp_reviews[yelp_reviews['business_name'] == "Lo-Lo's Chicken & Waffles"]
df_2 = df_1.groupby(['stars']).size().reset_index().sort_values('stars')