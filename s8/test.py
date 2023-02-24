import os
import ast

contacts_file = r'C:\Users\Alexey\Desktop\GB\Python\swork\s8\contacts.txt'

def read_file(file) -> dict:                        #считывает файл и записывает содержимое в переменную
    contacts_dict = {}
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            dict_line = ast.literal_eval(line)      #преобразование строки файла в считываемый программой формат
            contacts_dict.update(dict_line)         #дополнение преобразованной строкой (парой элементов) словаря
    return contacts_dict

def print_nested_dict(nested_dict, keylist):        #навести красоту по табуляции, одного \t не хватает
    for key, value in nested_dict.items():
        for arg in value.keys():
            print(f'{keylist[arg]}:   {nested_dict[key][arg]}')
        print()

def append_contact(file, keylist, cont_numbers):    #добавление строки в формате вложенного словаря в файл
    contact_info = {}
    save_line = {}
    for key, value in keylist.items():              #цикл формирует пары {ключ:значение} и добавляет в словарь                    
        addition = input(f'Введите {value}:')       #подсказка для ввода - значение на русском
        contact_info.update({key: addition})
    save_line.update({str(len(cont_numbers) + 1):contact_info})     #пара {номер контакта:словарь}
    with open(file, 'a', encoding="utf-8") as f:
        f.write(f'\n{save_line}')
    print ('Контакт добавлен')

# print(contacts_dict['1']['name'])

def user_action():
    contacts_dict = read_file(contacts_file)
    cont_num_list = [int(key) for key in contacts_dict.keys()]
    cont_arg_list = dict(zip([key for key in contacts_dict['1']], ["Имя", "Отчество", "Фамилия", "Номер"]))
    print ('Добро пожаловать! \n'
    '1) Вывести весь справочник\n'
    '2) Добавить контакт \n'
    # '3) Найти контакт\n'
    # '4) Найти и удалить контакт\n'
    )
    while (input1:= int(input('Выберите действие со справочником (0 = выход):'))) != 0:
        if input1 == 1:
            print_nested_dict(contacts_dict, cont_arg_list)
        elif input1 == 2:
            append_contact(contacts_file, cont_arg_list, cont_num_list)
        # elif input1 == 3:
        #     print(search_contact(contacts_file))
        # elif input1 == 4:
        #     remove_contact(contacts_file)
        else:
            print("Некорректный ввод")

user_action()
