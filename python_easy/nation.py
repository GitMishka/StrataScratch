# Import your libraries
import pandas as pd

# Start writing code
airbnb_hosts.head() 

df = airbnb_hosts.merge(airbnb_units, on='host_id')
df = df[(df['age'] < 30) & (df['unit_type'] == 'Apartment')]
df = df.groupby(['nationality'])['unit_id'].nunique().to_frame('apartment_count').reset_index().sort_values('apartment_count', ascending = False)