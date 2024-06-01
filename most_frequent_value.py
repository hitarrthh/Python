import numpy as np
a = np.array([1,2,2,3,3,3,4,4,4,4,4])
count = np.bincount(a)
frequency = np.argmax(count)
print("The most frequent value in the array is:",frequency)