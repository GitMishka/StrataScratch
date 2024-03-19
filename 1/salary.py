import pandas as pd
import numpy as np

title_worker_id = title.rename(columns={"worker_ref_id": "worker_id"})
merged_df = pd.merge(worker, title_worker_id, on="worker_id")
max_salary = merged_df[merged_df["salary"] == merged_df["salary"].max()][
    ["worker_title","salary"]].rename(columns={"worker_title": "best_paid_title"})
max_salary

test = worker[['worker_id','last_name']]
test