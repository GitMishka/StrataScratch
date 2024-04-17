import pandas as pd

# Creating a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Using .agg() to apply multiple functions to the same column
result = df.agg({
    'A': ['sum', 'min', 'max'],  # Multiple functions for column A
    'B': 'mean'                  # Single function for column B
})

print(result)
