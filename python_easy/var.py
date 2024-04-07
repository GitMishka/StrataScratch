import pandas as pd
import numpy as np

p1 = winemag_p1['variety']
p2 = winemag_p2['variety']
result = pd.concat([p1,p2],axis = 0).drop_duplicates()