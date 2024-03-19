# Import your libraries
import pandas as pd

# Start writing code
worker.head()
start = '2014-06-01'
end = '2014-06-30'
worker['joining_date'] = pd.to_datetime(worker['joining_date'])
df = worker[(worker['joining_date'] >= start) & (worker['joining_date'] <= end) & (worker['worker_id'] % 2 == 0)]
df

