import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
from requests import head
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


data = pd.read_csv("Data_Analyst\Advertising.csv")

# Mô hình hồi quy tuyến tính đơn biến
X = data['TV'].values.reshape(-1, 1)
y = data['Sales'].values.reshape(-1, 1)
# chia bộ dữ liệu làm 2 tập train và test theo tỉ lệ 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()  # Khai báo mô hình hồi quy tuyến tính
regressor.fit(X_train, y_train)  # Huấn luyện mô hình
print("Mô hình hồi quy tuyến tính đã được huấn luyện, có các tham số:")
print("Intercept =", regressor.intercept_)
print("Coefficients:", regressor.coef_)

# dự đoán trên số sales của bộ dữ liệu test
y_pred = regressor.predict(X_test)

# Đánh giá mô hình qua R2-score và mean_squrd_error
score=r2_score(y_test,y_pred)
print('R2-score is ',score)
print('Mean_sqrd_error is==',mean_squared_error(y_test,y_pred))