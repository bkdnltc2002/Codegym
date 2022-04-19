import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
import seaborn as sns


# Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
# Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.
# Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
# Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.

data = pd.read_excel("House_Price.xlsx")

# print(data.info())
# print(data.shape)


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

