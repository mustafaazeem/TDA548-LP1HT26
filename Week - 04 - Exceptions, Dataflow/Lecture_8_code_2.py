m = [
    [1,    3,    None, 4,    None, None, 7,    None],
    [None, None, 3,    None, 5,    None, None, 8   ],
    [None, 2,    None, None, None, 6,    None, None],
    [9,    None, None, 1,    None, None, 4,    None],
    [None, None, 7,    None, 2,    None, None, 5   ],
    [None, 6,    None, 8,    None, 3,    None, None],
    [8,    None, None, 2,    None, None, 9,    None],
    [None, 4,    None, None, None, 7,    None, 1   ],
]

def is_group_complete(m, gi, gj):

    # is_row_index_valid

    # if gi+2 <= len(m):
    #     is_row_index_valid = True 
    # else: 
    #     is_row_index_valid = False 

    is_row_valid = gi+2 <= len(m)
    is_col_valid = gj+2 <= len(m[0])

    return is_row_valid and is_col_valid 

    # return gi+2 <= len(m) and gj+2 <= len[m[0]]

# print(is_group_complete(m, 6, 6))

def is_single_group(m, gi, gj):
    count = 0
    for i in range(gi, gi+2):
        for j in range(gj, gj+2):
            if m[i][j] is not None:
                count = count + 1
    if count == 1:
        return True 
    else:
        return False 

# print(is_single_group(m, 1, 0))


def rotate_group(m, gi, gj):
    
    m[gi][gj],   m[gi+1][gj],  m[gi][gj+1],   m[gi+1][gj+1] = \
    m[gi+1][gj], m[gi][gj],    m[gi+1][gj+1], m[gi][gj+1]

rotate_group(m, 0, 0)
for line in m:
    print (line)


def iteration(n, m):
    pass

