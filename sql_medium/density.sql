WITH density AS (
    SELECT 
        city, 
        country, 
        population / NULLIF(area, 0) AS density
    FROM 
        cities_population
    WHERE 
        area > 0
), max_density AS (
    SELECT 
        city, 
        country, 
        density
    FROM 
        density
    WHERE 
        density = (SELECT MAX(density) FROM density)
), min_density AS (
    SELECT 
        city, 
        country, 
        density
    FROM 
        density
    WHERE 
        density = (SELECT MIN(density) FROM density)
)

SELECT city, country, density FROM max_density
UNION ALL
SELECT city, country, density FROM min_density;
