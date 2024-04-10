SELECT from_user, 
       count(*) as total_emails, 
       ROW_NUMBER() OVER (ORDER BY count(*) DESC, from_user ASC) AS row_number
FROM google_gmail_emails
GROUP BY from_user
ORDER BY total_emails DESC, from_user ASC