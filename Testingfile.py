
import pandas as pd
data1 = pd.read_csv("D:\\Study\\Rapic Tech Skills\\Data Science\\worldometer_data.csv")
data2 = pd.read_csv(r"D:\\Study\Rapic Tech Skills\\Data Science\\worldometer_data.csv")
data3 = pd.read_csv(r"D:/Study/Rapic Tech Skills/Data Science/worldometer_data.csv")
data4 = pd.read_csv("D:/Study/Rapic Tech Skills/Data Science/worldometer_data.csv")
print(data1.head())
print(data2.tail())
print(data3.head())
print(data4.tail())
