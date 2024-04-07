# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

df = yelp_business[yelp_business['stars'] == 1]
df_2 = df.groupby(['name','review_count']).size().to_frame().reset_index()[['name','review_count']]