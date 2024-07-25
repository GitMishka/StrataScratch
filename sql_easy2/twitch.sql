select  distinct(a.user_id) from twitch_sessions a
join twitch_sessions b on a.user_id = b.user_id
where a.session_type = 'streamer' and b.session_type = 'viewer'