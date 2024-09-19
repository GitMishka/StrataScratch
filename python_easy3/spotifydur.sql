import pandas as pd

listening_habits['listen_duration'].fillna(0, inplace=True)

grouped_data = listening_habits.groupby('user_id').agg(
    total_listen_duration=('listen_duration', 'sum'),
    unique_song_count=('song_id','nunique')).reset_index()

grouped_data['total_listen_duration'] = (grouped_data['total_listen_duration'] / 60).round()

grouped_data