# Import your libraries
import pandas as pd

# Start writing code
employee_list.head()
employee_list_filtered =employee_list[(employee_list['last_name'] == 'Johnson' ) & (employee_list['profession'] == 'Doctor')]
result = employee_list_filtered[['first_name','last_name']]
result