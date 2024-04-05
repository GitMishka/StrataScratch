select top 1 gender, avg(cast(review_score as float))
from airbnb_reviews r 
join airbnb_guests g on r.from_user = g.guest_id where from_type = 'guest'
group by gender
order by avg(cast(review_score as float)) desc