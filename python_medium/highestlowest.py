# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries.head()

total = sf_public_salaries[sf_public_salaries['totalpay'] > 0].groupby(["jobtitle"])['totalpay'].agg(min_pay='min', max_pay='max').reset_index()
total['difference'] = total['max_pay'] - total['min_pay']
total['ratio'] = total['max_pay'] / (total['min_pay'])
result = total.sort_values('ratio', ascending=False)