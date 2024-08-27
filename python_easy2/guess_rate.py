import pandas as pd

df = airbnb_reviews.groupby('from_type')['review_score'].mean().reset_index(name='avg_score')

df['avg_score'] = df['avg_score'].round(2)

result = df[df['avg_score'] == df['avg_score'].max()]

print(result)
