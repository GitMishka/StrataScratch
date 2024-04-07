# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries.head()

df = sf_public_salaries[sf_public_salaries['jobtitle'].str.contains('METROPOLITAN TRANSIT AUTHORITY')][['employeename','totalpaybenefits']]