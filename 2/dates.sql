WITH filtered_orders AS (
    SELECT 
    week,
      --  DATE_TRUNC('week', week::date) AS week_start,
        quantity 
    FROM 
        orders_analysis
    WHERE 
        EXTRACT(QUARTER FROM week::date) = 1 AND
        EXTRACT(YEAR FROM week::date) = 2023
)
SELECT 
    week AS week, 
    SUM(quantity) AS total_quantity
FROM 
    filtered_orders
GROUP BY 
    week
ORDER BY 
    week;