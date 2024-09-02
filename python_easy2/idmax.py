import pandas as pd

# Create a Pandas Series
data = pd.Series([1, 3, 7, 2, 5])

# Find the index of the maximum value
index_of_max = data.idxmax()

print(index_of_max)