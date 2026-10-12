'''
A small introduction to how enumerate works
'''
data = [10, 5, 8, 3, 2]

for num in data:
    print(num)

print('now enumerating')

for index, num in enumerate(data):
    print(index, ' --- ', num)
