import pandas as pd
import numpy as np

merge = pd.merge(customers, orders, left_on ='id',right_on = 'cust_id')
merge = merge.groupby(['cust_id','first_name'])['order_cost'].sum().reset_index()
result = merge.sort_values(by='first_name', ascending=True)