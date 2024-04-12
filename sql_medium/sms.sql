with base as
(select * from fb_sms_sends
where ds = '2020-08-04'
and type = 'message')

select cast(round((sum(confirmed_flag)*1.00)/count(*),2)*100 as int) as perc
from
(select a.*,iif(b.phone_number is not null,1,0) as confirmed_flag
from base a left join fb_confirmers b 
on a.ds = b.date and a.phone_number = b.phone_number) as temp;