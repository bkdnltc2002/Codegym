import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
import seaborn as sns
from sqlalchemy import null
from scipy import stats

data = pd.read_csv("Data_Analyst\House_Price_HN.csv", encoding="ISO-8859-1")

data = data.dropna(how='all')

# ngo = data.loc[data["property_type"] == "trong ngo"]
# pho = data.loc[data["property_type"] == "mat pho"]
# legal = data.loc[data["land_certificate"] == "So do"]
# illegal = data[data["land_certificate"] != "So do"]

# print(illegal.shape)
# print(legal.shape)

# sns.kdeplot(ngo.price)
# sns.kdeplot(pho.price)

# ngo = ngo[~ngo["price"].isna()]
# pho = pho[~pho["price"].isna()]
# legal = legal[~legal["price"].isna()]
# ilegal = illegal[~illegal["price"].isna()]

# print(stats.ttest_ind(pho.price, ngo.price,
#       alternative="greater"))

# print(stats.ttest_ind(illegal.price, legal.price,
#       alternative="less"))

# data = data[~data["price"].isna() & ~data["area"].isna()]
# price = data["price"]
# area = data["area"]

# print(stats.pearsonr(price, area))

# data = data[~data["price"].isna() & ~data["lat"].isna() & ~data["long"].isna()]
# price = data["price"]
# lat = data["lat"]
# long = data["long"]

# print(stats.pearsonr(price, lat))
# print(stats.pearsonr(price, long))

# data1 = data.filter(["land_certificate", "property_type"])
# data1 = data1.dropna()
# contigency= pd.crosstab(data1["land_certificate"], data1["property_type"])
# c, p, dof, expected = stats.chi2_contingency(contigency)
# print (p)

data1 = data.filter(['price'])
data1 = data1.dropna()

q1, q2, q3, q4 = data1.price.quantile(0.25), data1.price.quantile(
    0.5), data1.price.quantile(0.75), data1.price.quantile(1.0)


def price_order(price):

    if price < q1:

        return 1

    elif price >= q1 and price < q2:

        return 2

    elif price >= q2 and price < q3:

        return 3

    else:

        return 4


data1['price_ordinal'] = data1.price.apply(price_order)
print(stats.spearmanr(data1.price, data1.price_ordinal))