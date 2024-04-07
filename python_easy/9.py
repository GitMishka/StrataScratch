bus = uber_advertising[uber_advertising['advertising_channel'].str.contains('bus')]
result = bus.groupby(['advertising_channel', 'year']).apply(lambda x: x['money_spent'].sum() / x['customers_acquired'].sum()).reset_index()

#Find the cost per customer for each advertising channel and year combination . Include only channels that are advertised via public transport (advertising channel includes "bus" substring).

The cost per customer is equal to the total spent money divided by the total number of acquired customers through that advertising channel. Output advertising channel and its cost per customer.