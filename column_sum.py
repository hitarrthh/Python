import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
sum = np.sum(a,axis=0)
print("ORIGINAL ARRAY")
print(a)
print("SUM OF EVERY COLUMN")
print(sum)