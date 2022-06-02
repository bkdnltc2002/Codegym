import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
import seaborn as sns
from sqlalchemy import null
from scipy import stats

data = pd.read_csv("Data_Analyst\House_Price_HN.csv", encoding="ISO-8859-1")

data.dropna(how='all')

ngo = data.loc[data["property_type"] == "trong ngo"]
pho = data.loc[data["property_type"] == "mat pho"]
legal = data.loc[data["land_certificate"] == "So do"]
illegal = data[data["land_certificate"] != "So do"]

# print(illegal.shape)
# print(legal.shape)

# sns.kdeplot(ngo.price)
# sns.kdeplot(pho.price)


ngo = ngo[~ngo["price"].isna()]
pho = pho[~pho["price"].isna()]
legal = legal[~legal["price"].isna()]
ilegal = illegal[~illegal["price"].isna()]

print(stats.ttest_ind(pho.price, ngo.price,
      alternative="greater"))

print(stats.ttest_ind(illegal.price, legal.price,
      alternative="less"))
