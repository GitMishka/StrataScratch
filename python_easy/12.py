# Import your libraries
import pandas as pd

# Start writing code
uber_advertising.head()

df = uber_advertising[(uber_advertising['money_spent'] >= 100000) & (uber_advertising['year'] == 2019)][['advertising_channel']]