
import pandas as pd
data = pd.read_csv("D:\\Study\\WorldQuat Data Science\\Data\\brasil-real-estate-2.csv", encoding = "latin")
#print(data.head()) #print the first five rows of the data.
print(data.index[:5]) #This retrieves the index of the DataFrame, which is essentially the row labels. By default, the index is an integer-based range starting from 0. [:5] Slices notation selects the first five elements of the index.
print(data.shape) #To tell the data shape of the dataframe(the number of rows and columns).
print(data.head()) #Print the first five rows of the data.
print(data.loc[2]) #print the third row of the data
print(data["state"])