# Import your libraries
import pandas as pd

# Start writing code
sales_data.head()
sales_data['month'] = sales_data['month'].astype(str)
january_sales = sales_data[sales_data['month'].str.startswith('2024-01')]
top_sellers_by_category = january_sales.groupby('product_category').apply(
    lambda x: x.nlargest(3, 'total_sales', keep='all')).reset_index(drop=True)

# Display the result
top_sellers_by_category