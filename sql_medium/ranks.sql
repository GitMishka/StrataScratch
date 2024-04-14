with topcity as 
(select city,
count(*)  as cnt ,
rank() over (order by count(*) desc) as rnk
from yelp_business where stars = 5 group by city)

select city, cnt
from topcity
where rnk <= 5
ORDER BY cnt DESC