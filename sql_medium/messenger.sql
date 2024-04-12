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