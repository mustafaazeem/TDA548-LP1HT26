INPUT_FILE = 'Lecture_5_contacts.txt'

with open(INPUT_FILE, 'r') as infile:
    file_data = infile.readlines()

print(type(file_data))

line_0 = file_data[0]
print(line_0)
print("the type of line 0 is: ", type(line_0))

name, number = line_0.split(':')
print(f'name is {name} and numbers are {number}')

print(type(name), type(number))

name = name.strip('"')
print(name)

numbers = number.split(',')
# number = number.strip(" \n'").strip('[]')
print(numbers)