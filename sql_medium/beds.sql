with cte1 as (select nationality, n_beds from airbnb_apartments a 
join airbnb_hosts h on a.host_id = h.host_id)

select nationality, sum(n_beds) from cte1 group by nationality order by 2 desc

