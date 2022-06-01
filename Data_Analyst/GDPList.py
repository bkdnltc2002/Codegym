from unittest import result
import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
from scipy import stats

data = pd.read_csv("Data_Analyst\GDPlist.csv", encoding="ISO-8859-1")

# print(data.info())
# print(data.shape)

# data.rename(
#     columns={
#         "Country": "Nuoc",
#         "Continent": "Chauluc",
#         "GDP (millions of US$)": "GDP (trieu $)",
#     },
#     inplace=True,
# )

# data.insert(1, "Thanhpho", data["Nuoc"], True)

# data.Thanhpho = data.Thanhpho.replace("Vietnam", "Hanoi", regex=True)

# data.drop(data.loc[data.Chauluc == "Asia"].index, inplace=True)

# data.drop(data.loc[data["GDP (trieu $)"] < 300000].index, inplace=True)

# min = data["GDP (millions of US$)"].min()
# max = data["GDP (millions of US$)"].max()

# pop_continent = data.Continent.mode()

# sum_mean = data.pivot_table(
#     values="GDP (millions of US$)", index="Continent", aggfunc={"sum", "mean"}
# )
# sum_mean.rename(columns={"mean": "TBC GDP", "sum": "Tong GDP"}, inplace=True)

# plt.bar(data["Continent"], data["GDP (millions of US$)"])
# plt.show()

# d11 = data[
#     data["Country"].isin(["Vietnam", "Indonesia", "Cambodia", "Thailand", "Malaysia"])
# ]
# data1 = pd.DataFrame({"x": d11["Country"], "y": d11["GDP (millions of US$)"]})
# data1.plot(x="x", y="y", kind="bar")
# plt.xlabel("Country", fontsize=14)
# plt.ylabel("GDP", fontsize=14)
# plt.show()

# filter1 = data[
#     data["Country"].isin(["Vietnam", "Indonesia", "Cambodia", "Thailand", "Malaysia"])
# ]
# result = filter1[["Country", "GDP (millions of US$)"]]
# plt.pie(result["GDP (millions of US$)"], labels=result["Country"])
# plt.show()

print(stats.ttest_1samp(data["GDP (millions of US$)"], 50000))

asia = data.loc[data["Continent"] == "Asia"]
europe = data.loc[data["Continent"] == "Europe"]
print(stats.ttest_ind(europe["GDP (millions of US$)"],
      asia["GDP (millions of US$)"], equal_var=True, alternative="greater"))

america = data.loc[(data["Continent"] == "South America") |
                   (data["Continent"] == "North America")]
print(stats.ttest_ind(
    europe["GDP (millions of US$)"], america["GDP (millions of US$)"]))
