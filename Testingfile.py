column_row = ["a", "b", "c", "d"]
row01 = [6, 7, 90, 84]
row02 = [77, 988, 760, 7788]
#Dictoionary comprehension
pickle_dict = {m:n for (m,n) in zip(column_row, row02)}
print(pickle_dict)

import pickle

pickle.dumps(pickle_dict, open("D:\Study\WorldQuat Data Science\Data\pickle files\pickle_dict.pkl", "wr"))