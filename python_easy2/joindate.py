# Import your libraries
import pandas as pd

# Start writing code
worker.head()

april = worker[worker['joining_date']>='2014-04-01'].groupby('department').count().reset_index().sort_values('worker_id', ascending=False)
april[['department','worker_id']]