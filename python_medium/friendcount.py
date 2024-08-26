# Import your libraries
import pandas as pd

# Start writing code
user_posts.head()

friendships = friendships.drop_duplicates()
likes = likes.drop_duplicates()
user_posts = user_posts.rename(columns={"user_name": "poster_name"})
friendships
friendships_reversed = friendships.rename(columns={"user_name1": "user_name2", "user_name2": "user_name1"})
all_friendships = pd.concat([friendships, friendships_reversed]).drop_duplicates()
merged_likes = pd.merge(likes, user_posts, on="post_id")
final_df = pd.merge(merged_likes, all_friendships, left_on=["user_name", "poster_name"], right_on=["user_name1", "user_name2"])