# Import your libraries
import pandas as pd

# Start writing code
uber_ride_requests.head()

df = uber_ride_requests.groupby('request_status')['monetary_cost'].mean()