# Import your libraries
import pandas as pd

# Start writing code
lyft_rides.head()

df = lyft_rides.groupby('hour')['travel_distance'].mean()