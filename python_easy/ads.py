# Import your libraries
import pandas as pd

# Start writing code
google_adwords_earnings.head()

df = google_adwords_earnings.groupby(['business_type']).sum('adwords_earnings').reset_index()
df = df[['business_type', 'adwords_earnings']]