# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment.head()
df = (amazon_shipment.groupby('shipment_id')['weight'].sum().to_frame('total_weight').reset_index())
df['rank'] = df['total_weight'].rank(method='dense', ascending=False)
result = df[['shipment_id','total_weight']][df['rank'] == 3]