# Import your libraries
import pandas as pd

my_uber_drives.head()
df = my_uber_drives[my_uber_drives['category'] == 'Business'].reset_index()

df = df.groupby('purpose')['miles'].sum().to_frame('n').reset_index().sort_values('n',ascending= False)
df.head(3)
# df_grouped = my_uber_drives[my_uber_drives['category']=="Business"].groupby('purpose')['miles'].sum().reset_index()