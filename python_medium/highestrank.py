import pandas as pd
import numpy as np

df = salesforce_employees[salesforce_employees['manager_id'] == 13][['first_name','target']]
result = df[df['target'] == df['target'].max()]