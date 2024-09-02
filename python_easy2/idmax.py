import pandas as pd

# Create a Pandas Series
data = pd.Series([1, 3, 7, 2, 5])

# Find the index of the maximum value
index_of_max = data.idxmax()

print(index_of_max)
import pandas as pd

# Create a Pandas DataFrame
data = pd.DataFrame({
    'worker_id': [1, 2, 3, 4, 5],
    'login_timestamp': pd.to_datetime([
        '2023-08-01 08:00:00', 
        '2023-08-01 09:00:00', 
        '2023-08-01 10:00:00', 
        '2023-08-01 11:00:00', 
        '2023-08-01 12:00:00'])
})

# Suppose we want the row index of the latest login
index_of_latest_login = data['login_timestamp'].idxmax()

print(index_of_latest_login)  # Output: 4 (because the last timestamp is the maximum)
