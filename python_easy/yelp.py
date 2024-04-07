import pandas as pd
import numpy as np

result = yelp_reviews[yelp_reviews['cool'] ==yelp_reviews['cool'].max()][['business_name','review_text']]