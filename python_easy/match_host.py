
# Start writing code
import pandas as pd
import numpy as np

merged_df = pd.merge(airbnb_hosts, airbnb_guests,  how='left', left_on=['nationality','gender'], right_on = ['nationality','gender'])
result = merged_df[['host_id','guest_id']].drop_duplicates()