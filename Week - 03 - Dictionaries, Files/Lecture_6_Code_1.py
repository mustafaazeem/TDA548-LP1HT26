'''
Simple generator function examples 
'''
def generate_123_v1():
    '''
    will generate integers 1, 2, and 3 in a row
    but only one at a time
    Input: None 
    Output: returns one integer at a time in range 1-4
    '''
    return 1, 2, 3

def generate_123_v2():
    return 1
    return 2
    return 3

def generate_123_v3():
    yield 1
    yield 2
    yield 3
    yield 4

# generator object 

gen_obj = generate_123_v3() 
print(gen_obj)
print('first yield call: ', next(gen_obj))
print('second yield call: ',next(gen_obj))
print('third yield call: ',next(gen_obj))
print('fourth yield call: ',next(gen_obj))

# print(generate_123_v2())
# print(generate_123_v2())
# print(generate_123_v2())