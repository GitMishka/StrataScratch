# Import your libraries
import pandas as pd

# Start writing code
playbook_events.head()
df = pd.merge(playbook_events,playbook_users, right_on = 'user_id', left_on = 'user_id')
non_english = df[(df['language'] != 'spanish') & (df['location'] == 'Argentina') & (df['device'] == 'macbook pro')]
final = non_english.groupby(['company_id','language'])['event_name'].count().reset_index()
final