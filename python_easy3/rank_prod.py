# Import your libraries
import pandas as pd

# Start writing code
online_orders.head()
online_orders['ym'] = online_orders['date'].dt.to_period('M')
df = online_orders[(online_orders['ym'] >= '2022-01') & (online_orders['ym'] <= '2022-06')]
df['total_revenue'] = df['cost_in_dollars'] * df['units_sold']
product_revenue = df.groupby('product_id')['total_revenue'].sum().reset_index()
top_products = product_revenue.sort_values(by='total_revenue', ascending=False).head(5)