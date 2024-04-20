# Import your libraries
import pandas as pd

# Start writing code
worker.head()
result = worker.groupby('department').count().reset_index()
result[['department','worker_id']]