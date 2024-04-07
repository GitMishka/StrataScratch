Find the median total pay for each job. Output the job title and the corresponding total pay, 
and sort the results from highest total pay to lowest.

# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries.head()
df = sf_public_salaries.groupby(['jobtitle'])['totalpay'].median()