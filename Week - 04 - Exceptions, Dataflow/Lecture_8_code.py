################################# Q1
'''G = 6.674e-11
def escape(M, r, V):
    v = (2*G*M / r)**0.5        # minimum velocity to escape 
    e = (V**2 - v**2)**0.5      # excess speed above minimum velocity 

    if V > v:                   # if object V is greater than minimum required escape velocity 
        print(f'Excess speed: {e}')
    else: 
        print("The object won't escape")


escape(7.3e22, 1.7e6, 5000)
escape(6e24, 5.6e6, 5000)
'''

################################# Q2


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
    return gi+2 <= len(m) and gj+2 <= len(m[0])

# print(is_group_complete(m, 0, -1))

def is_single_group(m, gi, gj):
    count = 0
    for i in range(gi, gi+2):
        for j in range(gj, gj+2):
            if m[i][j] is not None:
                count+=1 
    if count == 1:
        return True
    else:
        return False 

# print(is_single_group(m, 1, 1))
      
def rotate_group(m, gi, gj):
    m[gi][gj],   m[gi][gj+1], m[gi+1][gj],   m[gi+1][gj+1] = \
    m[gi+1][gj], m[gi][gj],   m[gi+1][gj+1], m[gi][gj+1]


# rotate_group(m, 0, 0)
# for row in m:
#     print(row)
    

def iteration(n, m):
    start = n%2

    for i in range(start, len(m), 2):
        for j in range(start, len(m[0]), 2):
            if is_group_complete(m, i, j):
                if is_single_group(m, i, j):
                    rotate_group(m, i, j)

