import pandas as pd

worker_logins['login_timestamp'] = pd.to_datetime(worker_logins['login_timestamp'])

latest_login_indices = worker_logins.groupby('worker_id')['login_timestamp'].idxmax()

result = worker_logins.loc[latest_login_indices].reset_index(drop=True)

result
