# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

df = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['streams'] >= 3000000]
df = df[['trackname','artist','streams']].sort_values('streams', ascending = False)

Find songs that have more than 3 million streams.
Output the track name, artist, and the corresponding streams.
Sort records based on streams in descending order.