import numpy as np
mat1=([1,2,3],[4,5,6],[7,8,9])
mat2=([7,8,7],[3,2,9],[5,8,3])
product=np.dot(mat1,mat2)
print("Prodouct of matrix is")
print(product)
add=np.add(mat1,mat2)
print("Addition of matrix is")
print(add)

import numpy as np

# Get the dimensions of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create an empty matrix
matrix = np.empty((rows, cols))

# Fill the matrix with user input
print("Enter matrix elements:")
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))

print("Matrix entered:")
print(matrix)
