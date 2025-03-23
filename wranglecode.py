# import numpy as np
import pandas as pd
# import os

data_path = "marketing_data.csv"
datafeed = pd.read_csv(data_path)
datafeed.columns = datafeed.columns.str.strip()

# convert income to numeric
datafeed['ID'] = pd.to_numeric(datafeed['ID'], errors='coerce')
datafeed['Income'] = pd.to_numeric(datafeed['Income'], errors='coerce')
# group income by educationa and marital status and fill by mean
datafeed['Income'] = datafeed.groupby(['Education', 'Marital_Status'])['Income'].transform(lambda x: x.fillna(x.mean()))
# get rid of empty spaces
datafeed['Education'] = datafeed['Education'].str.strip()
datafeed['Marital_Status'] = datafeed['Marital_Status'].str.strip()

# print section to check 
print(datafeed.head())
# print(datafeed.columns)
print(datafeed.shape)
print(datafeed.info())
print(datafeed.describe())