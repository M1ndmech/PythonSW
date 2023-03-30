import functions as fn
import links as lnk

def user_action():
    contacts_dict = fn.read_file(lnk.contacts_file)
    cont_num_list = [int(key) for key in contacts_dict.keys()]
    cont_arg_list = dict(zip([key for key in contacts_dict['1']], ["Имя", "Отчество", "Фамилия", "Номер"]))
    print ('Добро пожаловать! \n'
    '1) Вывести весь справочник\n'
    '2) Добавить контакт \n'
    '3) Найти контакт\n'
    '4) Изменить контакт\n'
    '5) Удалить контакт'
    )
    while (input1:= int(input('Выберите действие со справочником (0 = выход):'))) != 0:
        if input1 == 1:
            fn.print_nested_dict(contacts_dict, cont_arg_list)
        elif input1 == 2:
            fn.append_contact(lnk.contacts_file, cont_arg_list, cont_num_list)
        elif input1 == 3:
            fn.lookup_contact(contacts_dict)
        elif input1 == 4:
            fn.change_contact(contacts_dict, cont_arg_list, lnk.contacts_file)
        elif input1 == 5:
            fn.remove_contact(contacts_dict, lnk.contacts_file)
        else:
            print("Некорректный ввод")

user_action()
