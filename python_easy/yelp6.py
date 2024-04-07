# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

yelp_business['rank'] = yelp_business['review_count'].rank(ascending=False)
yelp_business = yelp_business[yelp_business['rank'] <= 5][['name','review_count']].sort_values(by = 'review_count', ascending=False)