import os
import ast

def read_file(file) -> dict:                        #считывает файл и записывает содержимое в переменную
    contacts_dict = {}
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            dict_line = ast.literal_eval(line)      #преобразование строки файла в считываемый программой формат
            contacts_dict.update(dict_line)         #дополнение преобразованной строкой (парой элементов) словаря
    return contacts_dict

def write_dict(nested_dict, file):                        #считывает файл и записывает содержимое в переменную
    with open(file, 'w', encoding="utf-8") as f:
        for k, v in nested_dict.items():
            if k == "1":
                f.writelines(f'{{"{k}":{v}}}')
            else:
                f.writelines(f'\n{{"{k}":{v}}}')
    print('Файл перезаписан')

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
    save_line.update({str(cont_numbers[-1] + 1):contact_info})     #пара {номер контакта:словарь}
    with open(file, 'a', encoding="utf-8") as f:
        f.write(f'\n{save_line}')
    print ('Контакт добавлен')

def lookup_contact (nested_dict):
    print ('Поиск по:\n'
    '1) Имени\n'
    '2) Фамилии'
    )
    while (input_choice:= int(input('Выберите действие (0 = выход):'))) != 0:
        if input_choice == 1:
            input1 = input("Введите имя:")
            for key, value in nested_dict.items():
                if nested_dict[key]['name'] == input1:
                   print(f'Найдена запись: {" ".join(str(x) for x in nested_dict[key].values())}')
            return
        elif input_choice == 2:
            input2 = input("Введите фамилию:")
            for key, value in nested_dict.items():
                if nested_dict[key]['surname'] == input2:
                    print(f'Найдена запись: {" ".join(str(x) for x in nested_dict[key].values())}')
            return
        else:
            return

def change_contact (nested_dict, keylist, file):    
    input1 = input("Поиск изменяемого контакта. Введите фамилию или имя:")
    flag = False
    for key, value in nested_dict.items():
        if nested_dict[key]['name'] == input1 or nested_dict[key]['surname'] == input1:
            print(f'Найдена запись: {" ".join(str(x) for x in nested_dict[key].values())}') 
            while(input_choice_2:= int(input('Выбран правильный контакт? (1 - Да, 2 - Нет):'))) != 2:
                if input_choice_2 == 1:
                    for k, v in keylist.items():
                        nested_dict[key][k] = (input_2 := input(f'Введите новое значение {v} или нажмите Enter:'))
                    flag = True
                    break
    if flag:
        write_dict(nested_dict, file)

def remove_contact (nested_dict, file):    
    # Условно работает - изменяет, но добавляет строку в начало файла.
    # И надо нажимать 2 несколько раз если есть повторы имен/фамилий
    input1 = input("Поиск удаляемого контакта. Введите фамилию или имя:")
    flag = False
    new_dict = nested_dict.copy()
    for key, value in nested_dict.items():
        if nested_dict[key]['name'] == input1 or nested_dict[key]['surname'] == input1:
            print(f'Найдена запись: {" ".join(str(x) for x in nested_dict[key].values())}') 
            while(input_choice_2:= int(input('Выбран правильный контакт? (1 - Да, 2 - Нет):'))) != 2:
                if input_choice_2 == 1:
                    del new_dict[key]
                flag = True
                break
    if flag:
        write_dict(new_dict, file)
