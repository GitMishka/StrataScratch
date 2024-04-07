# Import your libraries
import pandas as pd

# Start writing code
result = oscar_nominees[oscar_nominees['nominee'] == 'Abigail Breslin']['movie'].nunique()
unique_movie_counts = oscar_nominees.groupby('nominee')['movie'].nunique()
