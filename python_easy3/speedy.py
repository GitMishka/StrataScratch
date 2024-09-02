# Import your libraries
import pandas as pd

# Start writing code
shopify_orders.head()
df = shopify_orders.merge(shopify_carriers, left_on='carrier_id', right_on ='id')
result = df[df['name'].str.lower() == 'speedy express'].shape[0]