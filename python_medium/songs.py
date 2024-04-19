# Import your libraries
import pandas as pd

# Start writing code
billboard_top_100_year_end.head()

# Assuming 'billboard_top_100_year_end' is a pandas DataFrame already defined
billboard_top_100_year_end = billboard_top_100_year_end[
    (billboard_top_100_year_end['year_rank'] == 1) &
    (billboard_top_100_year_end['year'] <= 2024) &
    (billboard_top_100_year_end['year'] >= 2004)
]
billboard_top_100_year_end[['song_name']].drop_duplicates()