# Import your libraries
import pandas as pd

# Start writing code
winemag_p1.head()

filtered_df = winemag_p1[winemag_p1['country'].isin(['Spain', 'Italy', 'France'])][['price']]
