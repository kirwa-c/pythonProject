import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('bigmart_data.csv')
data = df.dropna(subset=['Item_Weight', 'Outlet_Size'])
data.isna().sum()
data.describe()
# data['Item_Outlet_Sales'] = data['Item_Outlet_Sales'].fillna(data['Item_Outlet_Sales'].mean())
data.info()
data.duplicated().value_counts()
data['Item_Type'].value_counts()
freq_table = data.groupby(['Item_Type']).size().reset_index(name='Count')
# print(freq_table)
freq_table['Count%'] = freq_table['Count']/sum(freq_table['Count'])*100
print(freq_table)
plt.bar(freq_table['Item_Type'], freq_table['Count'])
# plt.show()

data["Item_Outlet_Sales"].mean()

# data2=data["Item_Outlet_Sales"].max()
# data.hist()
plt.hist(data['Item_Outlet_Sales'])
# plt.show()
plt.figure(figsize = (10,7))
data.boxplot()
plt.title("Box Plot")
# plt.show()
data2=sns.lmplot(x='Item_Outlet_Sales', y='Item_Weight', hue='Outlet_Type', fit_reg=False, data=data)
plt.show()