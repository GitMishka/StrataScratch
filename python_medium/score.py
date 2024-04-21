import pandas as pd
import numpy as np

hollywood = los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['facility_address'].str.contains('HOLLYWOOD BLVD')]
result = hollywood.groupby(['facility_name'])['score'].min().to_frame('min_score').reset_index().sort_values(['min_score','facility_name'], ascending = [False, True])