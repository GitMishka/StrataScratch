import pandas as pd
import numpy as np

merged_df = pd.merge(airbnb_hosts, airbnb_apartments,  how='left', left_on=['host_id'], right_on = ['host_id'])
total_beds = merged_df.groupby(['nationality'])['n_beds'].sum().reset_index().sort_values('n_beds',ascending = False)
result = total_beds.rename(columns={"n_beds": "total_beds_available"})