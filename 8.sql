with counts as (select count(appointmentid) as n, gender from medical_appointments group by gender order by 1 desc)
SELECT 
    gender, 
    n AS number_of_appointments 
FROM 
    counts 
    limit 1