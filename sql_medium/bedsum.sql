WITH bedsum AS (
  SELECT 
    host_id,
    SUM(n_beds) AS total_beds
  FROM airbnb_apartments
  GROUP BY host_id
)

SELECT *,
  DENSE_RANK() OVER (ORDER BY total_beds DESC) AS rank
FROM bedsum
