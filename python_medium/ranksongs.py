# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

df = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position'] == 1]
df = df.groupby(['trackname']).size().to_frame('n1').reset_index().sort_values('n1',ascending = False)