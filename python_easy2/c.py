import pandas as pd


# List of names to check
names = ['Vipul', 'Satish']

pattern = '|'.join(names) 


a = worker[~worker['first_name'].str.contains(pattern, na=False)]

c = ['c','C']
pattern = '|'.join(c) 

b = a[~a['last_name'].str.contains(pattern)]
