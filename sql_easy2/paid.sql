SELECT COUNT(DISTINCT(c.user_id))
FROM rc_calls c
JOIN rc_users u ON c.user_id = u.user_id
WHERE c.date LIKE '2020-04-%'
AND status = 'paid';
