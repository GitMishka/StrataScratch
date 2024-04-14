with merged as (select u.*, h.age, h.nationality from airbnb_hosts h join airbnb_units u on h.host_id = u.host_id)

select nationality, count(distinct unit_id) from merged where unit_type = 'apartment' and age < 30
group by nationality
order by 2 desc