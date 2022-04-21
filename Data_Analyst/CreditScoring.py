import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
import seaborn as sns



# Đặt tên bất kỳ cho các nhóm ở 2 ý trên.

data = pd.read_csv("Data_Analyst\CreditScoring.csv")

# print(data.info())
# print(data.describe())

# data.interpolate()
# data.fillna(0)

# data_1 = data
# Q1 = data_1.quantile(0.25)
# Q3 = data_1.quantile(0.75)
# IQR = Q3 - Q1

# data_1 = data_1[~((data_1 < (Q1 - 1.5 * IQR)) |
#                   (data_1 > (Q3 + 1.5 * IQR))).any(axis=1)]

# cats= pd.qcut(data_1['age'],5)
# print(cats)
# print(pd.value_counts(cats))

# cats = pd.cut(data_1['age'],[0, 30, 40, 50, 80, 150])
# dogs = pd.cut(data_1['MonthlyIncome'],[0, 30, 40, 50, 80, 150])
# print(pd.value_counts(cats))
# print(pd.value_counts(dogs))
