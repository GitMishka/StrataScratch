WITH AggregatedProfits AS (
    SELECT 
        company, 
        SUM(profits) AS total_profits
    FROM 
        forbes_global_2010_2014
    GROUP BY 
        company
),  top3 as (
SELECT top 3
    ---RANK() OVER (ORDER BY total_profits DESC) AS profit_rank,
    company,
    total_profits
FROM 
    AggregatedProfits
    
order by total_profits desc)

select company, total_profits from top3