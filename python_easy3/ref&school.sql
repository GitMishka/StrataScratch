import pandas as pd
result1 = loans[loans['type'] == 'Refinance']
result2 = loans[loans['type'] == 'InSchool']
result = pd.DataFrame(set(result1['user_id']).intersection(set(result2['user_id'])))
