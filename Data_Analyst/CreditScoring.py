import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
import seaborn as sns


# Nêu thông tin về kiểu dữ liệu và khoảng dữ liệu ở các cột
# Kiểm tra dữ liệu khuyết thiếu
# Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu bằng giá trị nội suy theo các cột
# Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu bằng giá trị 0
# Vẽ biểu đồ boxplot, biểu đồ phân bố dữ liệu cho các cột
# Loại bỏ giá trị ngoại lai
# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng phần tử bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng giữ liệu của mỗi nhóm.
# Chia dữ liệu ở các cột age và MonthlyIncome thành 5 nhóm theo các khoảng: 0, 30, 40, 50, 80, 150 và đếm số lượng phần tử ở mỗi nhóm.
# Đặt tên bất kỳ cho các nhóm ở 2 ý trên.

data = pd.read_csv("Data_Analyst\CreditScoring.csv")

# print(data.info())
# print(data.describe())

# data.interpolate()
# data.fillna(0)

data_1 = data
Q1 = data_1.quantile(0.25)
Q3 = data_1.quantile(0.75)
IQR = Q3 - Q1

data_1 = data_1[~((data_1 < (Q1 - 1.5 * IQR)) |
                  (data_1 > (Q3 + 1.5 * IQR))).any(axis=1)]

cats = pd.cut(data_1['age'],[0, 30, 40, 50, 80, 150],5)
print(cats)


#trung_liet_kham_thien=data[(data['ward_name']=="Phường Trung Liệt") | (data['ward_name']=="Phường Khâm Thiên")]

#three_bedrooms=data[(data['land_certificate']=="Sổ đỏ") & (data['bedroom']>=3)][['address','price','house_direction','balcony_direction']]

# type_land=data.pivot_table(values='price', index='type_of_land',  aggfunc = {'max', 'min', 'mean'})

# phuong=data.pivot_table(values=['bedroom','toilet','floor'], index='ward_name',  aggfunc = 'mean')

# print(data.isna())

# data_1 = data.dropna(subset=['price'])

# values = {"land_certificate": "không có thông tin",
#           "house_direction": data.house_direction.mode(),
#           "balcony_direction": data.balcony_direction.mode(),
#           "toilet": data.toilet.mode(),
#           "bedroom": data.bedroom.mode(),
#           "floor": data.floor.mode()}
# data_1 = data_1.fillna(value=values)

# nha_ngo = data.loc[data['title'].str.find('ngõ') > -1]

# nha_ngo['giá/m2'] = (data['price']*1000)/data['area']

# Q1 = nha_ngo.loc[:, ['area', 'giá/m2']].quantile(0.25)
# Q3 = nha_ngo.loc[:, ['area', 'giá/m2']].quantile(0.75)
# IQR = Q3 - Q1
# nha_ngo = nha_ngo[~((nha_ngo.loc[:, ['area', 'giá/m2']] < (Q1 - 1.5 * IQR))|
#                     (nha_ngo.loc[:, ['area', 'giá/m2']] > (Q3 + 1.5 * IQR))).any(axis=1)]


# ssc = StandardScaler().fit_transform(pd.DataFrame(nha_ngo['giá/m2']))
# mms = MinMaxScaler().fit_transform(pd.DataFrame(nha_ngo['giá/m2']))
# rsc = RobustScaler().fit_transform(pd.DataFrame(nha_ngo['giá/m2']))
