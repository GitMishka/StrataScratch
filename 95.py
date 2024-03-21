# Import your libraries
import pandas as pd

# Start writing code
winemag_p1.head()
# df = winemag_p1.groupby('winery')['points'].sum().reset_index()
# result = df[df['points'] >= 95]
result = winemag_p1[winemag_p1['points'] >= 95][['winery']].drop_duplicates()