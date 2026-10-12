'''
We implement linear and binary search to see the difference in running
time of each algorithm. 
The program generates a list named data, with list comprehension method
'''
import random 

# a list named data, which contains a billion integers randomly generated between range [100, 100_000]
# This is a list comprehension 

data = [random.randint(100, 10000) for _ in range(100_000)]


def lin_search(data, target):
    # for num in data:
    #     if num == target:
    #         print(f'{target} found at index {data.index(target)}')

    for index, num in enumerate(data):
        if num == target:
            return (f'{num} at {index}')

target = 123
size = len(data)

print(lin_search(data, target))

def bin_search(data, target):
    start = 0
    end = size-1 

    while start <= end:
        mid = (start+end) // 2
        if data[mid] == target:
            return f'{target} found at {mid}'
        elif data[mid] < target:
            start = mid + 1
        elif data[mid] > target:
            end = mid - 1