-- select * from entertainment_catalog

-- with flight101 as (
-- select * from flight_schedule
-- where flight_id = 101
-- )

-- Select flight_id, movie_id, duration from entertainment_catalog ec
-- join flight_schedule fs on fs.flight_duration >= ec.duration

WITH flight101 AS (
  SELECT * FROM flight_schedule
  WHERE flight_id = 101
)
SELECT
  fs.flight_id,
  ec.movie_id,
  ec.duration
FROM
  entertainment_catalog ec
JOIN
  flight101 fs ON fs.flight_duration >= ec.duration;