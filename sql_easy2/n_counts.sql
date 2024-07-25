select user_id, sum(number_of_comments) from fb_comments_count  
where created_at between dateadd(day, -30, '2020-02-10') and '2020-02-10' 
group by user_id