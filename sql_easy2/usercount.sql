select count(distinct(user_id)), account_id from sf_events 
where year(date) = 2021 
and month(date) = 1
group by account_id