-- You are given a dataset from Amazon that tracks and aggregates user activity on their platform in certain time periods. For each device type, find the time period with the highest number of active users.

-- The output should contain 'user_count', 'time_period', and 'device_type', where 'time_period' is a concatenation of 'start_timestamp' and 'end_timestamp', like ; "start_timestamp to end_timestamp".

with ranked_user_activity AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY device_type ORDER BY user_count DESC) AS rank
        ,start_timestamp || ' to ' || end_timestamp AS time_period

    FROM
        user_activity
)
SELECT
    user_count,
  time_period,
    device_type
FROM
    ranked_user_activity
WHERE
    rank = 1;