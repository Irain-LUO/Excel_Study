import pandas as pd
#  填充汽车差价
car = pd.read_excel('car.xlsx')
# car['差价'] = car['原价'] - car['售价']  #  操作符的重载（操作对象：list）：四则运算 操作对象：Excel列
# car['差价'] = car['原价'] - 8  # 所有原价值 - 8
# for i in car['原价'].index:  # for循环遍历：计算所有差价
#     car['差价'].at[i] = car['原价'].at[i] - car['售价'].at[i]

for i in range(3,8):  # for循环遍历:填充部分连续单元格
    car['差价'].at[i] = car['原价'].at[i] - car['售价'].at[i]

# def
print(car)
print("Done!")