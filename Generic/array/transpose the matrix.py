#Transpose the matrix
A = [ [1, 1, 1, 1], 
 [2, 2, 2, 2], 
 [3, 3, 3, 3], 
 [4, 4, 4, 4]] 
rows = len(A)
cols = len(A[0])


# B = [[0] * cols for _ in range(rows)]
# print(B)
# B = A[:][:]
# print(B)

# for i in range(rows):
#     for j in range(cols):
#         B[i][j] = A[i][j]
# print(B)

T = [list(row) for row in zip(*A)]

print(T)