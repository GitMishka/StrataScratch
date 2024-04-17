# Import your libraries
import pandas as pd

# Start writing code
fraud_score.head()
fraud_score['perc'] = fraud_score.groupby('state')['fraud_score'].rank(pct=True)
df = fraud_score[fraud_score['perc'] >.95]
result = df[['policy_num','state','claim_cost','fraud_score']]