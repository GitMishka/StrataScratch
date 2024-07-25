SELECT DISTINCT a.user_id
FROM loans a
JOIN loans b
ON a.user_id = b.user_id
WHERE a.type = 'Refinance'
AND b.type = 'InSchool';


SELECT user_id
FROM loans
WHERE type IN ('Refinance', 'InSchool')
GROUP BY user_id
HAVING COUNT(DISTINCT type) = 2;
