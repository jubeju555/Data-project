# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import os

data_path = "marketing_data.csv"
datafeed = pd.read_csv(data_path)
datafeed.columns = datafeed.columns.str.strip()

datafeed['ID'] = pd.to_numeric(datafeed['ID'], errors='coerce')

# convert income to numeric
datafeed['Income'] = datafeed['Income'].apply(lambda x: str(x).replace('$', '').replace(',', '').strip())
datafeed['Income'] = pd.to_numeric(datafeed['Income'], errors='coerce')
# group income by education and marital status and fill by mean
datafeed['Income'] = datafeed.groupby(['Education', 'Marital_Status'])['Income'].transform(lambda x: x.fillna(x.mean()))

# get rid of empty spaces

datafeed['Education'] = datafeed['Education'].str.strip()
datafeed['Marital_Status'] = datafeed['Marital_Status'].str.strip()

datafeed['Dt_Customer'] = pd.to_datetime(datafeed['Dt_Customer'], errors='coerce')
datafeed['TotalChildren'] = datafeed['Kidhome'] + datafeed['Teenhome']
datafeed['age'] = 2025 - datafeed['Year_Birth']
datafeed['Total_Spending'] = datafeed[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)
datafeed['Total_purchases'] = datafeed[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)

datafeed['onlineactivity'] = datafeed['NumWebPurchases'] + datafeed['NumCatalogPurchases'] + datafeed['NumWebVisitsMonth']
datafeed['instoreactivity'] = datafeed['NumStorePurchases']

def shoppingpref(row):
    if row['onlineactivity'] > row['instoreactivity']:
     return 'online shopper'
    elif row ['onlineactivity'] < row['instoreactivity']:
       return 'instore shopper'
    else: 
       return 'mixed shopper'
    
datafeed['shoppertype'] = datafeed.apply(shoppingpref, axis=1)

# Age vs shopping type
print(datafeed.groupby('shoppertype')['age'].mean())
# Children vs shopping type
print(datafeed.groupby('shoppertype')['TotalChildren'].mean())
# Count of each type
print(datafeed['shoppertype'].value_counts())


# graphs and plots

# numericcols = ['Income', 'age', 'Recency', 'TotalChildren', 'Total_Spending', 'Total_purchases']

# for col in numericcols:
#     plt.figure(figsize=(8,4))
#     sns.histplot(datafeed[col], kde=True, bins=30)
#     plt.title(f'Distribution of {col}')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.grid(True)
#     plt.show()

# for col in numericcols:
#     plt.figure(figsize=(8, 4))
#     sns.boxplot(x=datafeed[col])
#     plt.title(f'Box Plot of {col}')
#     plt.grid(True)
#     plt.show()



# print section to check 
print(datafeed)
# print(datafeed.columns)
# print(datafeed.shape)
# print(datafeed.isnull().sum())
print(datafeed.info())
# print(datafeed.describe())

# print(datafeed.isnull().sum())

