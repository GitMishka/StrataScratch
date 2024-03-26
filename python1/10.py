# Import your libraries
import pandas as pd

# Start writing code
uber_advertising.head()

bus = uber_advertising[uber_advertising['advertising_channel'].str.contains('bus')]
result = bus.groupby(['advertising_channel', 'year']).apply(lambda x: x['money_spent'].sum() / x['customers_acquired'].sum()).reset_index()