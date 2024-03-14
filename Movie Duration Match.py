# Import your libraries
import pandas as pd

# Start writing code
entertainment_catalog.head()
flight_movies_cross = pd.merge(
    flight_schedule.assign(key=1), 
    entertainment_catalog.assign(key=1), 
    on='key'
)#.drop('key', axis=1)
flight_movies_cross
# suitable_movies = flight_movies_cross[flight_movies_cross['duration'] <= flight_movies_cross['flight_duration']]
# suitable_movies_sorted = suitable_movies.sort_values(by=['flight_id', 'duration'], ascending=[True, True])

# result = suitable_movies_sorted[['flight_id', 'movie_id', 'duration']]
# result.rename(columns={'duration': 'movie_duration'}, inplace=True)

# result[result['flight_id'] == 101]