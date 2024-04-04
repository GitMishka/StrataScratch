WITH RankedUsage AS (
    SELECT
        device_type,
        start_timestamp,
        end_timestamp,
        SUM(user_count) AS total_user_count,
        RANK() OVER (PARTITION BY device_type ORDER BY SUM(user_count) DESC) AS rank
    FROM
        user_activity
    GROUP BY
        device_type, start_timestamp, end_timestamp
)
SELECT
    device_type,
    convert(nvarchar(50),start_timestamp) + ' to ' + convert(nvarchar(50), end_timestamp),
    total_user_count
FROM
    RankedUsage
WHERE
    rank = 1;