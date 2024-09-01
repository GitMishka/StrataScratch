import pandas as pd
import datetime as dt

worker_logins["login_timestamp"] = pd.to_datetime(worker_logins["login_timestamp"])
dates_df = worker_logins[
    worker_logins["login_timestamp"].between("2021-12-13", "2021-12-19")
]
result = dates_df["worker_id"].unique()