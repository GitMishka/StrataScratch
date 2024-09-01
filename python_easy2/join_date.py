import pandas as pd
import numpy as np
import datetime as dt

employees["joining_date"] = pd.to_datetime(employees["joining_date"])
employees["year"] = employees["joining_date"].dt.year
employees["month"] = employees["joining_date"].dt.month

year_df = employees.loc[employees["year"] == 2022, :]
month_df = year_df.loc[year_df["month"].between(1, 7)]
result = len(month_df)
s