-- select * from users;

-- select * from users u
-- join friends f on u.user_id = f.user_id
-- where user_name in ('Karl','Hans') and friend_id 

with cte as(SELECT friend_id FROM friends
WHERE user_id IN (SELECT user_id FROM users WHERE user_name = 'Karl')
INTERSECT
SELECT friend_id FROM friends
WHERE user_id IN (SELECT user_id FROM users WHERE user_name = 'Hans'))

SELECT friend_id, user_name
FROM cte join users ON friend_id = user_id