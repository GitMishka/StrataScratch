# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment.head()
df = (amazon_shipment.groupby('shipment_id')['weight'].sum().to_frame('total_weight').reset_index())