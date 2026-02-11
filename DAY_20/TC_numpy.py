import numpy as np
import pandas as pd
arr=np.array([10,20,5,6,200])

print("array:",arr)
print("sum",np.sum(arr))
print("mean",np.mean(arr))
print("multily by 2:",arr*2)

data={
    "Name":["AKASH","DURGA","PRASAD"],
    "Age":[23,24,26],
    "City":["Bangalore","Chennai","Hydrabad"],
    "gender":["male",'male',"male"]
}

df=pd.DataFrame(data)
print(df)

print(df["Name"])

print(df[df["Age"]>26])
df["Salary"]=[55000,66000,78000]
print(df)