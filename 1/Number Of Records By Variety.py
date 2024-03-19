# Import your libraries
import pandas as pd

# Start writing code
iris.head()

df = iris.groupby(['variety']).size().to_frame('sepal_length').reset_index()