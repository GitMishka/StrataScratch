# Import your libraries
import pandas as pd

# Start writing code
worker.head()

import pandas as pd

worker['rank'] = worker['worker_id'].rank(method='dense', ascending=True)

worker.sort_values('worker_id', ascending=False, inplace=True)

worker = worker[worker['rank'] == worker['rank'].max()]
worker.drop('rank', axis = 1)

