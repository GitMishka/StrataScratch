# Import your libraries
import pandas as pd

# Start writing code
airbnb_contacts.head()
df = airbnb_contacts.groupby(['id_guest'])['n_messages'].sum().to_frame('n').sort_values('n',ascending=False).reset_index()

df['ranking'] = df['n'].rank(method='dense',ascending=False)

df