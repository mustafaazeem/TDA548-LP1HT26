'''
Building a dictionary from a file with generator object
'''
INPUT_FILE = 'Lecture_5_contacts.txt'

def file_generator(file=INPUT_FILE):    
    with open(file, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            yield line

def parse_line(line):
    name, contact = line.split(':')
    # name = name.strip('"')
    # contact = contact.strip(' \n[]" ')
    # contact = contact.split(',')
    # return name, contact
    contact.replace('[]', '')
    return name.strip('"'), contact.strip('').split(',')

def build_dict(contacts_dict, name, contact):
    contacts_dict[name] = contact 
    # can, or should use, setdefault() here 


def main():
    contacts_dict = {}
    for line in file_generator():
        name, contact = parse_line(line)
        # build_dict(contacts_dict, name, contact)
        # print("name is: ", name)
        print("contact is: ", contact)
    # print(contacts_dict)

main()