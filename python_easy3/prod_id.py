# Import your libraries
import pandas as pd

# Start writing code
fct_customer_sales.head()
df = fct_customer_sales.merge(dim_product, on='prod_sku_id', how='right')
result = df[df['order_id'].isna()][['prod_sku_id', 'market_name']]