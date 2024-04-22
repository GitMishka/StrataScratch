# Import your libraries
import pandas as pd

# Start writing code
worker.head()

#worker = pd.merge(worker,title, left_on = 'worker_id', right_on = 'worker_ref_id')
worker["highest_sal"] = worker["salary"].rank(method="dense", ascending=False)
worker["lowest_sal"] = worker["salary"].rank(method="dense", ascending=True)
worker_sal = worker.loc[
    (worker["lowest_sal"] == 1) | (worker["highest_sal"] == 1), :
]

worker_sal.loc[worker_sal["highest_sal"] == 1, "salary_type"] = "Highest Salary"
worker_sal.loc[worker_sal["lowest_sal"] == 1, "salary_type"] = "Lowest Salary"
result = worker_sal[["worker_id", "salary", "department", "salary_type"]]