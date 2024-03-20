# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()
df_1 = yelp_reviews[(yelp_reviews['business_name'] == "Lo-Lo's Chicken & Waffles") & (yelp_reviews['stars'] == '5')] 
df_1['stars'].count()
