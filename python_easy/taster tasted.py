# Import your libraries
import pandas as pd

# Start writing code
winemag_p2.head()

not_null = winemag_p2[winemag_p2['taster_name'].notnull()]
df = not_null.groupby(['taster_name','variety']).size().to_frame('n').reset_index().sort_values(by = 'n',ascending = False)