# Import your libraries
import pandas as pd

# Start writing code
airbnb_apartments.head()

df = pd.merge(airbnb_apartments,airbnb_hosts, on = 'host_id')

df = df.groupby(['nationality'])['n_beds'].sum().to_frame('n').sort_values('n',ascending = False).reset_index()
