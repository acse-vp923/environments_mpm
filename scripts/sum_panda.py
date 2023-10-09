import pandas as pd
from envtest import sum_column_values

data = {"A": [1,2,3], "B": [4,5,6]}
column_name = "B"
result = sum_column_values(data, column_name)
print(f"Sum of {column_name} : {result}")