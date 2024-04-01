# Import your libraries
import pandas as pd

# Start writing code
cities_population.head()
cities_population = cities_population[cities_population['area'] != 0]
cities_population['density'] = cities_population['population'] / cities_population['area']
max_df = cities_population[cities_population['density'] == cities_population['density'].max()][['city', 'country', 'density']].round()
min_df = cities_population[cities_population['density'] == cities_population['density'].min()][['city', 'country', 'density']].round()
df = pd.concat([max_df, min_df])
df
You are working on a data analysis project at Deloitte where you need to analyze a dataset containing information

about various cities. Your task is to calculate the population density of these cities, rounded to the nearest integer, and identify the cities with the minimum and maximum densities.

The population density should be calculated as (Population / Area).

The output should contain 'city', 'country', 'density'.