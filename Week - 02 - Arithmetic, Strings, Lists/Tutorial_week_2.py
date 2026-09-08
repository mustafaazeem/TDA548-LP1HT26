
# import random 
# # for i in range(0, 5, 1):
# for i in range(5):
#     print(f'points for person {i+1} are {random.randint(55, 93)}')

# s1_points = random.randint(50, 100)
# s2_points = random.randint(50, 100)
# s3_points = random.randint(50, 100)
# s4_points = random.randint(50, 100)
# s5_points = random.randint(50, 100)

# students_points = []

# for i in range(100_000):
#     students_points.append(random.randint(50, 100))

# for i in range(100_000):
#     print(students_points[i])

# print(s1_points, s2_points, s3_points, s4_points, s5_points)



# friends_names = ["Anna", "Elsa"]
friends_names = [] 
number_of_friends = int(input("How many friends do you have: "))

for i in range(number_of_friends):
    name = input(f'enter name of friend {i+1} : ')
    friends_names.append(name)

for i in range(number_of_friends):
    print(friends_names[i])

print(friends_names[3:])
print(friends_names[-1])
print(friends_names[2:4])