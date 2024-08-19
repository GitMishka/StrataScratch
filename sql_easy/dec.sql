WITH UserCounts AS (
    SELECT 
        account_id,
        COUNT(DISTINCT CASE WHEN DATEPART(month, date) = 12 AND DATEPART(year, date) = 2020 THEN user_id END) AS dec_users,
        COUNT(DISTINCT CASE WHEN DATEPART(month, date) = 1 AND DATEPART(year, date) = 2021 THEN user_id END) AS jan_users
    FROM 
        sf_events
    WHERE 
        DATEPART(year, date) = 2020 OR DATEPART(year, date) = 2021
    GROUP BY 
        account_id
)
SELECT 
    account_id,
    CASE 
        WHEN dec_users > 0 THEN CAST(jan_users AS FLOAT) / dec_users 
        ELSE NULL 
    END AS growth_rate
FROM 
    UserCounts
ORDER BY 
    account_id;
