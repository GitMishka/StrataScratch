SELECT 
    inspection_type,
    
    sum(CASE 
        WHEN risk_category IS NULL THEN 1 ELSE 0
        END
    ) AS no_risk_results,
    
    sum(CASE 
        WHEN risk_category = 'Low Risk' THEN 1 ELSE 0
        END
    ) AS low_risk_results,
    
    
    sum(CASE 
        WHEN risk_category = 'Moderate Risk' THEN 1 ELSE 0
        END
    ) AS medium_risk_results,
    
    sum(CASE 
        WHEN risk_category = 'High Risk' THEN 1 ELSE 0
        END
    ) AS high_risk_results,
    
    count(*) AS total_inspections
FROM sf_restaurant_health_violations
GROUP BY 
    inspection_type
ORDER BY
    total_inspections DESC