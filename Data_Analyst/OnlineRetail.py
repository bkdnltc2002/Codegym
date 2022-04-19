import matplotlib.pyplot as plt
from nbformat import read
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv("Data_Analyst\OnlineRetail.csv", encoding='ISO-8859-1')

# print(data.info())
# print(data.shape)

# description_quantity = data.loc[:, ['Description','Quantity']]
# description_quantity.to_csv('OnlineRetails.csv')

# first_1000th=data.iloc[0:1000,:]
# first_1000th.to_excel('OnlineRetail.xlsx')

# quantity = data.loc[data['Quantity']>10]
# quantity.to_hdf('OnlineRetail.h5','quantity',format='table')

# require_5=data.loc[1000:2000,['Quantity','InvoiceDate','UnitPrice']]
# require_5.to_json('OnlineRetail.json',orient='columns')

# invoice=data.loc[data['InvoiceNo']=='536365']
# invoice.to_html('OnlineRetail.html')

# country_price_mean=data.pivot_table(values='Quantity', index='InvoiceNo', columns='Country',  aggfunc = 'mean')
# min_max_customer=data.pivot_table(values='Quantity', index='CustomerID', columns='StockCode', aggfunc = {min,max})
# stock_sum_mean=data.pivot_table(values=['Quantity','UnitPrice'], index='StockCode', aggfunc = {'Quantity': np.sum,'UnitPrice': np.mean})
# daily_total=data.pivot_table(values='Quantity', index='InvoiceDate', aggfunc = 'sum')

# conditions_previous= [(data.InvoiceDate.str.split('/').str[0] == '1') | (data.InvoiceDate.str.split('/').str[0]== '2') |(data.InvoiceDate.str.split('/').str[0] == '3'),
#               (data.InvoiceDate.str.split('/').str[0] == '4') | (data.InvoiceDate.str.split('/').str[0]== '5') |(data.InvoiceDate.str.split('/').str[0] == '6'),
#               (data.InvoiceDate.str.split('/').str[0] == '7') | (data.InvoiceDate.str.split('/').str[0]== '8') |(data.InvoiceDate.str.split('/').str[0] == '9'),
#               (data.InvoiceDate.str.split('/').str[0] == '10') | (data.InvoiceDate.str.split('/').str[0]== '11') |(data.InvoiceDate.str.split('/').str[0] == '12')]
# choices = ['1', '2', '3', '4']
# data['Previous'] = np.select(conditions_previous, choices, default='0')

# data['Amount']=data['Quantity']*data['UnitPrice']

# data['Discount']=data['Amount']
# data.loc[(data.Country == 'United Kingdom') & (data.Previous== '4'),'Discount']=data['Amount']*0.1
# data.loc[data.Country == 'France','Discount']=data['Amount']*0.05

# data['Total']=data['Amount']-data['Discount']
# print(data)

# Phát hiện các dòng, cột chứa dữ liệu khuyết thiếu
# Có nên xóa hết các dòng chứa dữ liệu khuyết thiếu, giải thích vì sao
# Thực hiện xử lý giá trị khuyết thiếu: Thay thế giá trị khuyết thiếu của thuộc tính Description bằng giá trị mặc định “Không biết”
# Thực hiện phát hiện giá trị ngoại lai của thuộc tính Quantity và Thuộc tính UnitPrice
# Tiến hành lọc riêng bộ dữ liệu chứa giá trị ngoại lai và bộ dữ liệu sạch
# Mô tả thông tin của bộ dữ liệu trên và nhận xét

# print(data.describe())

# print(data.isna())

data_1 = data.dropna()
values = {"Description": "Không biết"}
data_1 = data_1.fillna(value=values)
data_1 = pd.DataFrame(data_1)

data_1 = data_1[((data_1['Quantity'] < 0) |
                 (data_1['UnitPrice'] == 0))]

sns.kdeplot(data=data_1.loc[:, ['Quantity', 'UnitPrice']])
plt.show()