WITH friendships_clean AS (
    SELECT DISTINCT user_name1, user_name2
    FROM friendships
),
friendships_expanded AS (
    SELECT user_name1, user_name2 FROM friendships_clean
    UNION ALL
    SELECT user_name2 AS user_name1, user_name1 AS user_name2 FROM friendships_clean
),
likes_posts_joined AS (
    SELECT 
        l.user_name, 
        l.post_id, 
        l.date_liked,
        p.user_name AS poster_name
    FROM likes l
    JOIN user_posts p ON l.post_id = p.post_id
    WHERE l.date_liked IS NOT NULL
),
friends_likes AS (
    SELECT lp.user_name, lp.post_id, lp.date_liked, lp.poster_name
    FROM likes_posts_joined lp
    JOIN friendships_expanded fe ON lp.user_name = fe.user_name1 AND lp.poster_name = fe.user_name2
),
friday_likes AS (
    SELECT post_id, date_liked
    FROM friends_likes
    WHERE DATEPART(WEEKDAY, date_liked) = 6
)
SELECT date_liked, COUNT(post_id) AS likes
FROM friday_likes
GROUP BY date_liked
ORDER BY date_liked;