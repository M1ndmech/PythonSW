import os
import random
'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
1.Программа должна выводить данные 
2.Программа должна сохранять данные в текстовом файле 
3.Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
4.Использование функций. Ваша программа не должна быть линейной

1. Чтение
2. Поиск
3. Добавить
4. Сохранить
'''

contacts_file = r'C:\Users\Alexey\Desktop\GB\Python\swork\s8\contacts.txt'

def append_contact(contacts_file):
    contact = input('Введите контакт в формате Ф И О Телефон:')
    with open(contacts_file, 'a', encoding="utf-8") as f:
        f.write(f'\n{contact}')
    print ('Контакт добавлен')

def read_file(contacts_file):
    with open(contacts_file, 'r', encoding="utf-8") as f:
        print (f.read())

def search_contact(contacts_file):
    search_by = input("Введите информацию для поиска (фамилия, имя или отчество):")
    with open(contacts_file, 'r', encoding="utf-8") as f:
        for line in f:
            if search_by in line:
                print(line)


def user_action():
    print ('Добро пожаловать! 1) Вывести весь справочник 2) Добавить контакт 3) Найти контакт')
    while (input1:= int(input('Выберите действие со справочником (0 = выход):'))) != 0:
        if input1 == 1:
            read_file(contacts_file)
        elif input1 == 2:
            append_contact(contacts_file)
        elif input1 == 3:
            search_contact(contacts_file)
        else:
            print("Некорректный ввод")

user_action()

















# def add_contact (dict1):
#     name = input("Введите имя контакта:")
#     surname = input("Введите фамилию контакта:")
#     patronymic = input("Введите отчество контакта:")
#     phone = input("Введите телефонный номер:")
#     new_contact = {'name': name, 'surname': surname, 'patronymic': patronymic, 'phone': phone}
#     return dict1 | new_contact

# contact_dict = {}

# with open(contacts_file, 'r') as open_file:
#     open_file.read()
#     add_contact(contact_dict)
# print(contact_dict)

