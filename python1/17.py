# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries.head()
sf_public_salaries['rank'] = sf_public_salaries['overtimepay'].rank(method = 'min', ascending=False)
ranked = sf_public_salaries.sort_values('rank',ascending = True)
top3 = ranked[ranked['rank'] <=3][['jobtitle']]

Get the job titles of the 3 employees who received the most overtime pay
Output the job title of selected records.