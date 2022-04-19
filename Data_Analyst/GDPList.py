import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd

data = pd.read_csv("GDPList.csv", encoding='ISO-8859-1')

# print(data.info())
# print(data.shape)

# data.rename(columns={'Country': 'Nuoc', 'Continent': 'Chauluc',
#             'GDP (millions of US$)': 'GDP (trieu $)'}, inplace=True)

# data.insert(1, 'Thanhpho', data['Nuoc'], True)

# data.Thanhpho = data.Thanhpho.replace('Vietnam', 'Hanoi', regex=True)

# data.drop(data.loc[data.Chauluc == 'Asia'].index, inplace=True)

# data.drop(data.loc[data['GDP (trieu $)'] < 300000].index, inplace=True)

# min=data['GDP (millions of US$)'].min()
# max=data['GDP (millions of US$)'].max()

#pop_continent=data.Continent.mode()

# sum_mean=data.pivot_table(values='GDP (millions of US$)', index='Continent',  aggfunc = {'sum', 'mean'})
# sum_mean.rename(columns={'mean': 'TBC GDP', 'sum':'Tong GDP'},inplace=True)

