
import pandas as pd

with open("D:\\Study\\WorldQuat Data Science\\Data\\tt.csv", "r") as f:
    colum_names = f.readline().strip().split(",")
    data = []
    for j in f:
        tt = j.strip().split(",")

        if len(tt) == len(colum_names):
            data.append(tt)
df = {colum_names[i]:[row[i] for row in data] for i in range(len(colum_names))}
df = pd.DataFrame(df)
print(df)

