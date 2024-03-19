# Import your libraries
import pandas as pd

# Start writing code
google_competition_participants.head()
merged_df = pd.merge(google_competition_participants,google_competition_scores, left_on = 'member_id', right_on = 'member_id')
scores_df = merged_df.groupby('team_id')['member_score'].mean().to_frame('score').reset_index()
sorted_df = scores_df.sort_values(by='score', ascending=False)