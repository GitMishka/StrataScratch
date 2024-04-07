# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

df_1 = yelp_business.groupby(['state'])['stars'].mean().reset_index()