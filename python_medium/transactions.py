# Import your libraries
import pandas as pd

# Start writing code
excel_sql_inventory_data.head()

df = pd.merge(excel_sql_inventory_data,excel_sql_transaction_data, on = 'product_id')

df = df.groupby('product_name')['transaction_id'].count()