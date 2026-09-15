contacts_tuple = [ ("Alice", "070-1112233"), ("Bob", "070-4445566"), ("Carol", "070-7778899"), ("Dana", "070-0001122"), ("Eve", "070-3334455") ]

contacts_str = [ "Alice 070-1112233", "Bob 070-4445566", "Carol 070-7778899", "Dana 070-0001122", "Eve 070-3334455",
]
for contact in contacts_tuple:
    print(contact[1].strip('0').replace('-', ''))

# for contact in contacts_str:
#     print(contact)
#     print(contact.split()[1].strip('0').replace('-', ''))

# my_contact = ("Mustafa", 709725948, "Molndal")

# my_contact = my_contact.__add__(("Lektor",))

# print(my_contact)

# name, number = my_contact 

# print(number)




# Tuple 
# ("Alice", 070-1112233)

# if "Bob 070-4445566" in contacts:
#     print("Yes bob is found")
# else:
#     print("Bob is not in your contact list")

# for contact in contacts:
#     if "Bob" in contact:
#         print(contact)



# for i in range( len(contacts) ):
#     print(contacts[i])

# for contact in contacts:
#     print(contact)

# contacts.append("Daniel 070-652431")
# contacts.extend(["Anna 076-332561", "Per 072-635263"])

# print( sorted(contacts) )
# print(contacts)

# print(contacts)
# contacts.sort()
# print(contacts)
# print(contacts)
