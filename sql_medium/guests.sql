select 
id_guest,
sum(n_messages),
dense_rank() over (order by sum(n_messages) desc)
from airbnb_contacts
group by id_guest