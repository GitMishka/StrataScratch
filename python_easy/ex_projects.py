# Import your libraries
import pandas as pd
import math
# Start writing code
# ms_projects.head()
# ms_emp_projects.head()
emp_count = ms_emp_projects.groupby("project_id")['emp_id'].count().reset_index()
result = pd.merge(ms_projects, emp_count, left_on = 'id', right_on = 'project_id')
result['budget_per_emp'] = round(result['budget']/result['emp_id'])
result[['title','budget_per_emp']].sort_values('budget_per_emp', ascending = False)