import pandas as pd
import numpy as np

result = sf_crime_incidents_2014_01.groupby(['day_of_week']).size().to_frame('n_occurences').reset_index().sort_values('n_occurences', ascending = False)