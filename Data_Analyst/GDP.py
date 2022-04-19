import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd

data = pd.read_csv("GDPList.csv", encoding='ISO-8859-1')
# print(data.info())

# GDP=data['GDP (millions of US$)']
# plt.hist(GDP,125,ec="red")
# plt.title("Phân bố GDP")
# plt.xlabel("GDP")
# plt.ylabel("Số lượng quốc gia")
# plt.show()

# count_country=data.groupby(['Continent'])['Country'].count()
# print(count_country)

# total_continent_GDP=data.groupby(['Continent'])['GDP (millions of US$)'].sum().sort_values(ascending=False)
# print(total_continent_GDP)

data = data.sort_values(ascending=False, by=['GDP (millions of US$)'])
print(data.head(10))
