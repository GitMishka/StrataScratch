-- WITH rnk AS (
--     SELECT 
--         name, 
--         sport, 
--         team, 
--         games, 
--         medal,
--         RANK() OVER (PARTITION BY sport ORDER BY medal DESC) as n
--     FROM 
--         olympics_athletes_events
-- )
-- -- SELECT * FROM rnk;
-- select 
-- name, 
-- team,
-- games, 
-- sport,
-- medal 
-- from rnk where n >1


SELECT
    name, 
    team,
    games, 
    sport,
    medal
FROM olympics_athletes_events
WHERE 
    team LIKE '%/%'