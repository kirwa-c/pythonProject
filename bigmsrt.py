import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('bigmart_data.csv')
# df.head()
# df.info()
# df.shape
df.isnull().sum()
data = df.dropna(subset=['Item_Weight', 'Outlet_Size'])
# data.head()
# print(df)
# data.shape
# data.isna().sum()
data.describe()
data['Item_Outlet_Sales'] = data['Item_Outlet_Sales'].fillna(data['Item_Outlet_Sales'].mean())