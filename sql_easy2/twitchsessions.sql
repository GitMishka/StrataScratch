SELECT
    session_type,
    AVG(DATEDIFF(second, session_start, session_end)) AS avg_duration
FROM twitch_sessions
GROUP BY session_type