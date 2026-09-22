'''
Basic matrix representation, and how to print it in multiple ways. 
'''
matrix = [ [0, 1, 8], [1, 7, 9, 8, 3],  [3, 1, 3, 4] ]

matrix_representation_2 = [
                             [0, 1, 8], 
                             [1, 7, 9, 8, 3],  
                             [3, 1, 3, 4] 
                             ]

# print(matrix)
# print(matrix_representation_2)

# for row in matrix:
#     # print(f'row is {row}')
#     for element in row:
#         print("The element is", element)

# for i in range(len(matrix)):
#     print("This is matrix", i, ": ", matrix[i])
#     for j in range(len(matrix[0]))

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(f'printing {i},{j}: {matrix[i][j]}')

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()