SELECT u.user_id, u.user_name
FROM users u
JOIN (
    SELECT f1.friend_id
    FROM friends f1
    WHERE f1.user_id = (SELECT user_id FROM users WHERE user_name = 'Karl')
    INTERSECT
    SELECT f2.friend_id
    FROM friends f2
    WHERE f2.user_id = (SELECT user_id FROM users WHERE user_name = 'Hans')
) AS mutual_friends ON u.user_id = mutual_friends.friend_id;
