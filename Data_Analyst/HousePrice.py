import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
import seaborn as sns

data = pd.read_excel("Data_Analyst\House_Price.xlsx")

# print(data.info())
# print(data.shape)

# trung_liet_kham_thien = data[
#     (data["ward_name"] == "Phường Trung Liệt")
#     | (data["ward_name"] == "Phường Khâm Thiên")
# ]

# three_bedrooms = data[(data["land_certificate"] == "Sổ đỏ") & (data["bedroom"] >= 3)][
#     ["address", "price", "house_direction", "balcony_direction"]
# ]

# type_land = data.pivot_table(
#     values="price", index="type_of_land", aggfunc={"max", "min", "mean"}
# )

# phuong = data.pivot_table(
#     values=["bedroom", "toilet", "floor"], index="ward_name", aggfunc="mean"
# )

# print(data.isna())

# data_1 = data.dropna(subset=["price"])

# values = {
#     "land_certificate": "không có thông tin",
#     "house_direction": data.house_direction.mode(),
#     "balcony_direction": data.balcony_direction.mode(),
#     "toilet": data.toilet.mode(),
#     "bedroom": data.bedroom.mode(),
#     "floor": data.floor.mode(),
# }
# data_1 = data_1.fillna(value=values)

# nha_ngo = data.loc[data["title"].str.find("ngõ") > -1]

# nha_ngo["giá/m2"] = (data["price"] * 1000) / data["area"]

# Q1 = nha_ngo.loc[:, ["area", "giá/m2"]].quantile(0.25)
# Q3 = nha_ngo.loc[:, ["area", "giá/m2"]].quantile(0.75)
# IQR = Q3 - Q1
# nha_ngo = nha_ngo[
#     ~(
#         (nha_ngo.loc[:, ["area", "giá/m2"]] < (Q1 - 1.5 * IQR))
#         | (nha_ngo.loc[:, ["area", "giá/m2"]] > (Q3 + 1.5 * IQR))
#     ).any(axis=1)
# ]

# ssc = StandardScaler().fit_transform(pd.DataFrame(nha_ngo["giá/m2"]))
# mms = MinMaxScaler().fit_transform(pd.DataFrame(nha_ngo["giá/m2"]))
# rsc = RobustScaler().fit_transform(pd.DataFrame(nha_ngo["giá/m2"]))

# sns.barplot(data["toilet"], data["price"])
# plt.show()

# Phân tích mối liên hệ giữa diện tích với giá nhà. Đồng thời, giữa số phòng ngủ với giá nhà và giữa số toilet với giá nhà.
# So sánh giá nhà trung bình trên 1 m2 giữa các hình thức nhà (type_of_land). Đồn thời thể hiện tỉ lệ % bài đăng (bản ghi) giữa các hình thức nhà (type_of_land).
# Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ, theo số phòng toilet hoặc theo diện tích.

# plt.bar(x, y2, label="line 2", width=0.5)
# axes1 = plt.gca()
# axes2 = axes1.twinx()
# axes2.plot(x, y1, label="line 1", linewidth=2, c="r", marker="o")
# fig = plt.gcf()
# axes3 = fig.add_axes([left, bottom, width, height])
# axes3.plot()
# axes3 = fig.add_axes([0.2, 0.6, 0.25, 0.25])
# axes3.plot(x, y2)

# data1 = data.dropna()
# area_price = data1[["area", "price"]]
# bedroom_price = data1[["bedroom", "price"]]
# sns.lmplot(x="area", y="price", data=area_price)
# sns.lmplot(x="bedroom", y="price", data=bedroom_price)

# sns.violinplot(y="price", data=data1)

# sns.countplot(x="house_direction", data=data1)

# sns.boxplot(x="house_direction", y="price", data=data1)

# plt.show()
