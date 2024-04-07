# Import your libraries
import pandas as pd

# Start writing code
winemag_p1.head()
    
df = winemag_p1[(winemag_p1['price'] >= 5) & (winemag_p1['price'] <= 20)]['variety'].unique()
#or
filtered_df = winemag_p1[winemag_p1['price'].between(5, 20)]['variety'].unique()