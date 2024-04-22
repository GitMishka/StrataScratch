# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

df = yelp_business[yelp_business['stars'] == 5].groupby(['city'])['stars'].count().to_frame('n').reset_index()
df['rank'] = df['n'].rank(method = 'min', ascending = False)
df = df.sort_values('rank', ascending=True)
result = df[df['rank'] <= 5][['city', 'n']].sort_values('n', ascending = False)
