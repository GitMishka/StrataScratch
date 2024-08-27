# Import your libraries
import pandas as pd

# Start writing code
facebook_friends.head()
df = facebook_friends[(facebook_friends['user1'] != 1) & (facebook_friends['user2'] != 1)]
count_not_part_of = df.shape[0]