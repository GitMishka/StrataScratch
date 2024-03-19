# Import your libraries
import pandas as pd

# Start writing code
housing_units_completed_us.head()

df = housing_units_completed_us.groupby(['year'])['south','west','midwest','northeast'].sum().reset_index()
df['total'] = df['south'] + df['west'] + df['midwest'] + df['northeast']
df = df[['year','total']]