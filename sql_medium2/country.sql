select count(distinct u.user_id), language, location from playbook_events e 
join playbook_users u on e.user_id = u.user_id
group by location,language order by location asc