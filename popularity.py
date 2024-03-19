# Import your libraries
import pandas as pd

# Start writing code
facebook_employees.head()
merged_df = pd.merge(facebook_employees, facebook_hack_survey, left_on = 'id', right_on = 'employee_id')
df = merged_df.groupby('location')['popularity'].mean().reset_index()