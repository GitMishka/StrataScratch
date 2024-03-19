import pandas as pd

# Find the user IDs for Karl and Hans
karl_id = users[users['user_name'] == 'Karl']['user_id'].iloc[0]
hans_id = users[users['user_name'] == 'Hans']['user_id'].iloc[0]

# Find friends of Karl and Hans
karl_friends = friends[friends['user_id'] == karl_id]['friend_id'].tolist()
hans_friends = friends[friends['user_id'] == hans_id]['friend_id'].tolist()

# Find mutual friends' IDs
mutual_friends_ids = list(set(karl_friends).intersection(hans_friends))

# Get mutual friends' user names
mutual_friends = users[users['user_id'].isin(mutual_friends_ids)]

mutual_friends