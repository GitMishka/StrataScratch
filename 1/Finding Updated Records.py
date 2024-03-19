# Import your libraries
import pandas as pd
result = ms_employee_salary.groupby(['id','first_name','last_name','department_id'])['salary'].max()
# result = ms_employee_salary.groupby(['id','first_name','last_name','department_id'])['salary'].max().reset_index().sort_values('id')
result