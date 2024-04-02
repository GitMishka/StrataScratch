# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.head()

df = forbes_global_2010_2014.groupby('profits').max().reset_index().sort_values('profits', ascending = False)[['company','profits']].head(3)