# Import your libraries
import pandas as pd

# Start writing code
playbook_events.head()

merged = pd.merge(playbook_events, playbook_users, right_on = 'user_id', left_on = 'user_id')

result = merged.groupby(['location','language'])["user_id"].nunique().to_frame('n_speakers').reset_index()
final = result.sort_values(by = 'location', ascending = True)