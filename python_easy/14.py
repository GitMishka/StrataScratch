# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

df = spotify_worldwide_daily_song_ranking.groupby(['artist'])['position'].count().to_frame('n').reset_index().sort_values('n',ascending = False)

Find how many times each artist appeared on the Spotify ranking list
Output the artist name along with the corresponding number of occurrences.
Order records by the number of occurrences in descending order.