airbnb_guests.head()
import pandas as pd
df = pd.merge(airbnb_reviews,airbnb_guests, left_on = 'from_user', right_on = 'guest_id', how = 'inner')

df = df[df['from_type'] == 'guest']
df = df.groupby('gender')['review_score'].mean().reset_index()
max_review_score = df[df['review_score'] == df['review_score'].max()]
