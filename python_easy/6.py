# Import your libraries
import pandas as pd

# Start writing code
lyft_rides.head()

df = lyft_rides[(lyft_rides['hour'] <= 12) & (lyft_rides['weather'] == 'rainy')]
#Find all Lyft rides which happened on rainy days before noon.