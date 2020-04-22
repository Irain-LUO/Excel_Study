from pandas import  DataFrame
import os
value = {'ID':[1,2,3],'Number':['one', 'two', 'three']}
excel = DataFrame(value)
excel = excel.set_index("ID")
if os.path.exists("python.xlsx"):
    os.remove("python.xlsx")
    excel.to_excel("python.xlsx")
    print("ok")
else:
    excel.to_excel("python.xlsx")
    print("ok")
