import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
specified_row = np.array([4,5,6])
contains_row = any(np.array_equal(row,specified_row) for row in array)
if contains_row:
    print("The specified row is present in the array")
else:
     print("The specified row is not present in the array")
