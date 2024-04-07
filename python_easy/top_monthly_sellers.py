# Import your libraries
import pandas as pd

# Start writing code
#sales_data.head()

sales_data['month'] = pd.to_datetime(sales_data['month'])
january_sales = sales_data[sales_data['month'].dt.month == 1]
top_sellers_by_category = january_sales.groupby('product_category').apply(
    lambda x: x.nlargest(3, 'total_sales', keep = 'all')).reset_index(drop=True)
top_sellers_by_category

#sales_data['total_sales'].agg(['sum', 'mean'])