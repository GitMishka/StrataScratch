SELECT DISTINCT a.user_id
FROM loans a
JOIN loans b
ON a.user_id = b.user_id
WHERE a.type = 'Refinance'
AND b.type = 'InSchool';
