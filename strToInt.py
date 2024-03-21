# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()
yelp_reviews['stars'].unique()
yelp_reviews = yelp_reviews[yelp_reviews['stars'] != '?']
yelp_reviews.loc[:,('stars')] = yelp_reviews.loc[:,('stars')].astype(int)
yelp_reviews = yelp_reviews