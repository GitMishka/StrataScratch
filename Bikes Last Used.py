# Import your libraries
import pandas as pd

# Start writing code
dc_bikeshare_q1_2012.head()
dc_bikeshare_q1_2012 = dc_bikeshare_q1_2012.groupby(['bike_number'])['end_time'].max()