import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
import seaborn as sns
from scipy import stats

data = pd.read_csv("Data_Analyst\CreditScoring.csv")

# print(data.info())
# print(data.describe())

# data.interpolate()
# data.fillna(0)

# data_1 = data
# Q1 = data_1.quantile(0.25)
# Q3 = data_1.quantile(0.75)
# IQR = Q3 - Q1

# data_1 = data_1[
#     ~((data_1 < (Q1 - 1.5 * IQR)) | (data_1 > (Q3 + 1.5 * IQR))).any(axis=1)
# ]

# cats = pd.qcut(data_1["age"], 5)
# print(cats)
# print(pd.value_counts(cats))

# cats = pd.cut(data_1["age"], [0, 30, 40, 50, 80, 150])
# dogs = pd.cut(data_1["MonthlyIncome"], [0, 30, 40, 50, 80, 150])
# print(pd.value_counts(cats))
# print(pd.value_counts(dogs))

phu_thuoc=data.loc[data["NumberOfDependents"]>0]
ko_phu_thuoc=data.loc[data["NumberOfDependents"]==0]
kho_khan=data.loc[data["SeriousDlqin2yrs"]==1]
ko_kho_khan=data.loc[data["SeriousDlqin2yrs"]==0]

phu_thuoc = phu_thuoc[~phu_thuoc["MonthlyIncome"].isna()]
ko_phu_thuoc = ko_phu_thuoc[~ko_phu_thuoc["MonthlyIncome"].isna()]
kho_khan = kho_khan[~kho_khan["NumberOfOpenCreditLinesAndLoans"].isna()]
ko_kho_khan = ko_kho_khan[~ko_kho_khan["NumberOfOpenCreditLinesAndLoans"].isna()]


print(stats.ttest_ind(ko_phu_thuoc.MonthlyIncome, phu_thuoc.MonthlyIncome, alternative="less"))
print(stats.ttest_ind(kho_khan["NumberOfOpenCreditLinesAndLoans"], ko_kho_khan["NumberOfOpenCreditLinesAndLoans"], alternative="greater"))

