# Import your libraries
import pandas as pd

# Start writing code
medical_appointments.head()

df = medical_appointments.groupby(['gender']).size().to_frame('total').reset_index().sort_values('total',ascending=False).head(1)
