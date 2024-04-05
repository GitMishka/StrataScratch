SELECT DISTINCT country
FROM winemag_p1
WHERE country IS NOT NULL AND country NOT IN (
  SELECT country FROM winemag_p2
)
ORDER BY country ASC;