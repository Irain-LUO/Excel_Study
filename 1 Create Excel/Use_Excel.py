import pandas as pd
import os
value = {'ID':[1,2,3],'content':['one', 'two', 'three']}  #  Excel文件里的字典内容
excel = pd.DataFrame(value)    # 字典转换为DataFrame
excel = excel.set_index('ID') #  ID作为索引
if os.path.exists('python.xlsx'):  #  判断当前路径下存在python.xlsx
    os.remove('python.xlsx')  #   存在，则删除
    excel.to_excel("python.xlsx")  #  重新创建
else:
    excel.to_excel("python.xlsx")  # 创建新文件
