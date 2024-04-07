# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries.head()

df = sf_public_salaries[sf_public_salaries['employeename'].str.contains('Patric')][['employeename','benefits']]
