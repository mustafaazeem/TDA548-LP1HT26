M = [
    [11, 4, 2, 3, 8], 
    [32, 1, 4, 33, 9],
    [23, 2, 5, 3, 99]
]

# for i in range(len(M)):
#     for j in range(len(M[0])):
#         print(M[i][j], end=' ')
#     print()

M_transpose = [ 
    ['o' for _ in range(len(M))]  # columns 
    for _ in range(len(M[0]))       # rows 
]

for i in range(len(M)):
    for j in range(len(M[0])):
        M_transpose[j][i]= M[i][j]

print(M_transpose)


# for i in range(len(M_transpose)):
#     for j in range(len(M_transpose[0])):
#         print(M_transpose[i][j], end = " ")
#     print()
