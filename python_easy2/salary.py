# Import your libraries
import pandas as pd

# Start writing code
worker.head()

salary = worker[(worker['salary'] <= 100000) & (worker['salary'] >= 50000)]
salary['full_name'] = (salary['first_name'] + ' ' +  salary['last_name'])
result = salary[['full_name','salary']]
