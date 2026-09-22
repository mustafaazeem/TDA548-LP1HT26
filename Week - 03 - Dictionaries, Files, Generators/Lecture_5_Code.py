IN_FILE = 'Lecture_5_contacts.txt'  # Global constant 

# r - read mode 
# w - write mode 
# a - append mode 

with open(IN_FILE, 'r') as input_file:
    file_data = input_file.read()

contacts_dict = {}
# result
# if any(letter not in {'ACTG'} for letter in result)

for line in file_data.splitlines():
    # print(line)
    name, phone_number = line.split(':')
    name = name.strip('" ')
    phone_number = phone_number.strip(', ')
    # print(name, phone_number)
    contacts_dict[name] = phone_number

for k,v in contacts_dict.items():
    print(f'name is {k} and value is {v}')

# lines = file_data.splitlines()

# # print(type(lines), len(lines))
# line = lines[0]

# print("before parsing")
# print(line)

# print("\nafter parsing")

# line = line.strip(', "\n').split(':')

# name, phone_number = line

# name = name.strip('"')

# print(name, ' --- ', phone_number)

# def print_contacts(contacts_dict):
#     for key, value in contacts_dict.items(): 
#         print(f'name is: {key} and number is {value}')

# def add_contact(contacts_dict, new_name, phone_numbers):
    
#     # contacts_dict[new_key] = new_value
#     # contacts_dict[new_name] = phone_numbers
#     # contacts_dict.setdefault(new_name, []).extend(phone_numbers)
#     value = contacts_dict.setdefault(new_name, [])
#     value.extend(phone_numbers)

# def main():
#     new_name = 'Julia'
#     phone_numbers = ['070-972 59 48']
#     add_contact(contacts_dict, new_name, phone_numbers)


#     # name = 'Mustafa'

    

#     print("After addition: ")
#     print_contacts(contacts_dict)


    # query = contacts_dict.get(name, "The person you try to find is not in our contacts book")
    # print('.get method brings back: ', query)

    # query2 = contacts_dict.setdefault(name, "Dummy value")
    # print("With setdefault method", query2)

    # print_contacts(contacts_dict)

    # query2 = contacts_dict['Hassan']
    # print("Results of query 2", query2)

    # print("Before adding new contact")
    # print_contacts(contacts_dict)

    # add_contact(contacts_dict, new_name, phone_numbers)
    # print("\nAfter adding new contact")
    # print_contacts(contacts_dict)

# main()
