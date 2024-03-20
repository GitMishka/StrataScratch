# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()
yelp_reviews['stars'].unique()
result = yelp_reviews[yelp_reviews['stars'] != '?']
yelp_reviews['stars'] = pd.to_numeric(yelp_reviews['stars'], errors='coerce')