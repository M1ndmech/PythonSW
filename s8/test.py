import os
import ast

contacts_file = r'C:\Users\Alexey\Desktop\GB\Python\swork\s8\contacts.txt'

def read_file(file) -> dict:
    contacts_dict = {}
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            dict_line = ast.literal_eval(line)
            contacts_dict.update(dict_line)
    return contacts_dict

def append_contact(file):
    contact = input('Введите контакт в формате Ф И О Телефон:')
    with open(file, 'a', encoding="utf-8") as f:
        f.write(f'\n{contact}')
    print ('Контакт добавлен')

contacts_dict = read_file(contacts_file)
cont_num_list = [key for key in contacts_dict.keys()]
cont_arg_list = [key for key in contacts_dict['1']]

print(cont_num_list)
print(cont_arg_list)
print(contacts_dict['1']['name'])
