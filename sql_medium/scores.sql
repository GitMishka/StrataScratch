with cte1 as (select 
rank() over (order by score asc)  as rnks
, *

from los_angeles_restaurant_health_inspections

where facility_address like '%Hollywood%')

select facility_name, min(score) as mins from cte1 group by facility_name 
order by 2 desc