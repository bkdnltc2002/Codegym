import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import seaborn as sns


data = pd.read_csv("Data_Analyst\KoreanShop.csv", encoding="ISO-8859-1")

# data1 = data.dropna()
# sns.countplot(x="join_year", data=data1)
# sns.lmplot(x="rating_good", y="response_rate", data=data1)
# data1["response_time"] = pd.to_timedelta(data1["response_time"])
# data1["response_second"] = data1["response_time"].dt.total_seconds()
# sns.lmplot(x="rating_bad", y="response_second", data=data1)
# sns.violinplot(y="rating_star", data=data1)
# sns.countplot(x="is_official_shop", data=data1)
# sns.countplot(x="is_shopee_verified", data=data1)

# plt.show()
