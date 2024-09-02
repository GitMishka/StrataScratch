# Import your libraries
import pandas as pd

# Start writing code
amazon_sales.head()
amazon_sales = amazon_sales[amazon_sales['order_date'].dt.year == 2021]['order_total'].sum()