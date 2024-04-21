
import pandas as pd
import numpy as np

six_char = worker[worker['first_name'].str.contains('[a-zA-Z]{6}$')]
result = six_char[six_char['first_name'].str.endswith("h")]
