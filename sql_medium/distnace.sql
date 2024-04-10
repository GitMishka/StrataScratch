select top 10 user_id,name, sum(distance) from lyft_rides_log l
join  lyft_users u on l.user_id = u.id
group by user_id,name
order by 3 desc