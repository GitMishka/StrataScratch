# Import your libraries
import pandas as pd

# Start writing code
worker.head()

april_workers = worker[(worker['joining_date'] >= '2014-04-01' ) & (worker['department'] == 'Admin')]
april_workers.shape[0]