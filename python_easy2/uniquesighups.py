# Import your libraries
import pandas as pd

# Start writing code

transactions["transaction_start_date"] = pd.to_datetime(transactions["transaction_start_date"])
    
transactions["month"] = transactions["transaction_start_date"].dt.month
select_months = transactions[(transactions["month"].isin([4, 5]))]
result = select_months["signup_id"].unique()
