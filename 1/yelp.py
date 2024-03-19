# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

df = yelp_business[yelp_business['categories'].str.contains('pizza', case = False)]
df['categories'].count()