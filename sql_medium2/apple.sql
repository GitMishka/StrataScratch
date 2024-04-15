SELECT 
  language,
  COUNT(DISTINCT CASE WHEN device IN ('macbook pro', 'iphone 5s', 'ipad air') THEN u.user_id ELSE NULL END) AS n,
  COUNT(DISTINCT u.user_id) AS n_total
FROM playbook_events e 
JOIN playbook_users u 
  ON e.user_id = u.user_id
GROUP BY language
ORDER BY n_total DESC
