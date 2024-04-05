select 
guest_id,
rank () over (order by age desc)  as rank
from airbnb_guests;