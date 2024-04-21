# Import your libraries
import pandas as pd

# Start writing code
worker.head()

worker['lower_case'] = worker['first_name'].str.lower()

a = worker[worker['lower_case'].str.contains('a')]

a = a.drop('lower_case', axis=1)