# Import your libraries
import pandas as pd

# Start writing code
hotel_reviews.head()

df = hotel_reviews[hotel_reviews['hotel_name']=='Hotel Arena'].reset_index()
df = df.groupby(['reviewer_score','hotel_name']).size().to_frame('n_reviews').reset_index()