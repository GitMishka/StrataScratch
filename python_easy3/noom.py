# Import your libraries
import pandas as pd

# Start writing code
noom_signups.head()
noom_signups['started_at_month'] = noom_signups['started_at'].dt.to_period('M')
df = noom_signups.groupby(by = 'started_at_month').size().reset_index()