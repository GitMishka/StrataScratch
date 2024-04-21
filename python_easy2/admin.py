# Import your libraries
import pandas as pd

# Start writing code
worker_ws.head()

worker_ws = worker_ws[worker_ws['department'].str.contains('dmin')]