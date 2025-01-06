import pandas as pd
from pandas.core.construction import range_to_ndarray

with open("D:\\Study\\WorldQuat Data Science\\Data\\ts.csv", "r") as f:
    colum_names = f.readline().strip().split(",")
    data = []
    for j in f:
        tt = j.strip().split(",")

        if len(tt) == len(colum_names):
            data.append(tt)
df = {colum_names[i]:[item[i] for item in data] for i in range(len(colum_names))}
df = pd.DataFrame(df)
print(df)
print(df.head())


#Dictionary comprehension
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
my_dict = {k:v for (k,v) in zip(keys, values)} # Using the help of the zip() function


my_dict1 = {keys[i] : values[i] for i in range(len(keys)) }
print(my_dict1)
my_dict2 = {keys[i] : values[i] for i in values for i in range(len(keys)) }
print(my_dict2)

#Dictionary comprehension using a condition using if statement
new_dict = {x:x**2 for x in range(20) if x**2 % 4 != 0}
print(new_dict)

new_dict1 = {x:x**2 for x in range(20+1) if x**2 % 4 == 0}
print(new_dict1)

m = "TON"
newdict = {x : {y : x for y in m} for x in m}
print(newdict)