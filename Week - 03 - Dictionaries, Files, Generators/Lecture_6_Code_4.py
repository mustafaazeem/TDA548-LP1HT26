'''This is the same contacts dictionary building program, but with a json file 
'''
import json 

INPUT_FILE = 'Lecture_5_contacts.json'

contacts_dict = {}

with open(INPUT_FILE, 'r', encoding='utf-8') as json_file:
    contacts_dict = json.load(json_file)

# print(contacts_dict)

for k,v,t in contacts_dict.items():
    print(f'{k} has phone {v}')

with open('my_output.json', 'a', encoding='utf-8') as out_file:
    json.dump(contacts_dict, out_file)

