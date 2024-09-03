# Import your libraries
import pandas as pd

# Start writing code
dim_customer.head()
aggregated_df = dim_customer.groupby('cust_id').size().rename('n_occurences').reset_index()
result = aggregated_df[aggregated_df['n_occurences'] > 1]