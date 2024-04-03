select user_id,sum(listen_duration)/60,count(distinct(song_id)) from listening_habits
group by user_id