# Import your libraries
import pandas as pd

# Start writing code
sales_performance.head()
sam = sales_performance[sales_performance['salesperson'].isin(['Samantha','Lisa'])]
result = sam['sales_revenue'].sum()