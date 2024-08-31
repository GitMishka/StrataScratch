import pandas as pd
import numpy as np

result = olympics_athletes_events[olympics_athletes_events['team'].str.contains('/')][['name','team','games','sport','medal']]
