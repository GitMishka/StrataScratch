# Import your libraries
import pandas as pd

# Start writing code
worker.head()

start = '2014-02-01'
end = '2014-02-28'
worker['joining_date'] = pd.to_datetime(worker['joining_date'])

result = worker[(worker['joining_date'] >= start) & (worker['joining_date'] <= end) & (worker['worker_id'] % 2 != 0)]


