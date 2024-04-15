select company_id,language, count(*) from playbook_events e 
join playbook_users u on e.user_id = u.user_id
where location = 'Argentina' and language <> 'Spanish'
and device = 'macbook pro'
group by company_id, language