# import numpy as np
import pandas as pd
# import os

data_path = "marketing_data.csv"
marketingdata = pd.read_csv(data_path)
marketingdata.columns = marketingdata.columns.str.strip()

# convert income to numeric
marketingdata['ID'] = pd.to_numeric(marketingdata['ID'], errors='coerce')

print(marketingdata['ID'].head())
print(marketingdata.columns)

