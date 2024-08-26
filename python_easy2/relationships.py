import pandas as pd
import numpy as np

facebook_friends['user1_not_in_relationship'] = ((facebook_friends.user1 != 1) & (facebook_friends.user2 != 1)) .astype(int)
result = facebook_friends['user1_not_in_relationship'].sum()