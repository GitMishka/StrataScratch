WITH WeeklyOrders AS (
    SELECT 
        DATEADD(week, DATEDIFF(week, 0, week), 0) AS week_start,
        quantity
    FROM 
        orders_analysis
    WHERE 
        week >= '2023-01-01' 
        AND week < '2023-04-01'
)
SELECT 
    week_start, 
    SUM(quantity) AS total_quantity
FROM 
    WeeklyOrders
GROUP BY 
    week_start
ORDER BY 
    week_start;
