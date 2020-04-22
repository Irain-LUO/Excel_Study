import pandas as pd
# data = pd.read_excel('sort.xlsx')
# # data.sort_values(by='售价', inplace=True, ascending=False)  #  ascending:默认升序 TRUE
# data.sort_values(by=['存货','原价'], inplace=True, ascending=[True,False])  #  存货：先升序、原价：后降序
# print(data)

def sort_power(x):
    return 100 <= x <150  # python 特有的表达式
def sort_PL(x):
    return 1.5 <= x <= 2  # python 特有的表达式
data = pd.read_excel('car.xlsx')
# data = data.loc[data.马力.apply(sort_power)].loc[data['排量/L'].apply(sort_PL)]
data = data.loc[data.马力.apply(lambda x:100 <= x <150)]\
           .loc[data['排量/L'].apply(lambda x:1.5 <= x <= 2)]
print(data)
