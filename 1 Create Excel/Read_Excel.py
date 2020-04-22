import pandas as pd

data = pd.read_excel('python.xlsx')  # 自动添加索引
print(data.head())


data1 = pd.read_excel('python.xlsx', index_col='ID')  # 设置索引
print(data1.head())
print(data1.tail(2))

data2 = pd.read_excel('python - 副本.xlsx',header=1)  # 从第二行取
print(data2.head())


data2 = pd.read_excel('python - 副本 (2).xlsx')  # 没有表头
print(data2.head())
data2.columns = ['ID',"Number"]  # 设置表头
print(data2.head())

##  第一行空白，keys和values都在，没有影响

