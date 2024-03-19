import pandas as pd
import numpy as np

airbnb_guests['rank'] = airbnb_guests['age'].rank(method='min', ascending = False)
result = airbnb_guests[['guest_id','rank']].sort_values('rank',ascending = True)