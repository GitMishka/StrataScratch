SELECT from_user, 
       count(*) as total_emails, 
       ROW_NUMBER() OVER (ORDER BY count(*) DESC, from_user ASC) AS row_number
FROM google_gmail_emails
GROUP BY from_user
ORDER BY total_emails DESC, from_user ASC

/ 


with cte1 as (select from_user, count(*) as counts from google_gmail_emails
group by from_user ) 

select 
 * ,
 row_number() over (order by counts desc, from_user ASC)
 from cte1