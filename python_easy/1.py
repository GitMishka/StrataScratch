# Import your libraries
import pandas as pd

# Start writing code
yearly_summary = uber_advertising.groupby('year').agg(
    total_money_spent=pd.NamedAgg(column='money_spent', aggfunc='sum'),
    total_customers_acquired=pd.NamedAgg(column='customers_acquired', aggfunc='sum')
).reset_index()

