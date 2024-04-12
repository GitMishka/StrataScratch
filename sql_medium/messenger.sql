WITH sq AS (
    SELECT username, 
        SUM(msg_count) AS total_msg_count,
        RANK() OVER (ORDER BY SUM(msg_count) DESC) AS rank
    FROM (
        SELECT user1 AS username, msg_count
        FROM fb_messages
        
        UNION ALL 
        
        SELECT user2 AS username, msg_count
        FROM fb_messages
    ) a
    GROUP BY username
)
SELECT username, total_msg_count 
FROM sq
WHERE rank <= 10
ORDER BY total_msg_count DESC;

WITH SentMessages AS (
    SELECT user1 AS username, SUM(msg_count) AS sent_count
    FROM fb_messages
    GROUP BY user1
),
ReceivedMessages AS (
    SELECT user2 AS username, SUM(msg_count) AS received_count
    FROM fb_messages
    GROUP BY user2
),
CombinedCounts AS (
    SELECT
        ISNULL(s.username, r.username) AS username, 
        ISNULL(s.sent_count, 0) AS sent_count,
        ISNULL(r.received_count, 0) AS received_count
    FROM SentMessages s
    FULL OUTER JOIN ReceivedMessages r ON s.username = r.username
)
SELECT TOP 10
    username,
    (sent_count + received_count) AS total_messages
FROM CombinedCounts
ORDER BY total_messages DESC;
