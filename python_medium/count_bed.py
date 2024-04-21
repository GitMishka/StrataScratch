# Import your libraries
import pandas as pd

# Start writing code
airbnb_apartments.head()

df = airbnb_apartments.groupby('host_id')['n_beds'].sum().to_frame('n').reset_index()

df['rank'] = df['n'].rank(method = 'dense',ascending = False)
df.sort_values('rank',ascending = True)
