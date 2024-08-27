import pandas as pd
import numpy as np

heart = facebook_reactions[facebook_reactions['reaction'] == 'heart'][['post_id']]
result = pd.merge(heart,facebook_posts,on='post_id').drop_duplicates(subset = 'post_id')