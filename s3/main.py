import random
'''
Задача 1. Дан список чисел. 
Определите, сколько в нем встречается различных чисел. 
Input: [1, 1, 2, 0, -1, 3, 4, 4] 
Output: 6
'''

def random_int_list (length, min, max):
    list = []
    for i in range (length):
        list.append(random.randint(min,max))
    return list


# length_input = int(input("Введите длину списка: "))
# min_input = int(input("Введите минимальное значение списка: "))
# max_input = int(input("Введите максимальное значение списка: "))
# list1 = random_int_list(length_input, min_input, max_input)
# print(list1)
# set1 = set(list1)
# print(set1)
# print(len(set1))

'''
Задача 2. Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число. 
Input:   [1, 2, 3, 4, 5] k = 3 
Output:  [4, 5, 1, 2, 3]
'''

# length_input_2 = int(input("Введите длину списка: "))
# min_input_2 = int(input("Введите минимальное значение списка: "))
# max_input_2 = int(input("Введите максимальное значение списка: "))
# # k_input = int(input("Введите значение сдвига списка: "))
# list2 = random_int_list(length_input_2, min_input_2, max_input_2)

# print (list2)

# if k_input > 0: 
#     for i in range (k_input):
#         list2.insert(0, list2.pop(-1))

# print (list2)


# альтернативный вариант:

# start_lst = [1, 2, 3, 4, 5]
# k = int(input('k: '))
# k = -(k%len(start_lst))
# result_lst = []

# for i in range(len(start_lst)):
#     result_lst.append(start_lst[k])
#     k += 1

# print(result_lst)


'''
Задача 3. Напишите программу для печати всех уникальных значений в словаре. 
Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
{
    1: 'V',
    4: 'C',
    'ew': 'C'
}
-> V, C
'''

dict1 = {
    "IV": "S001", 
    "V": "S002", 
    "VI": "S001", 
    "III": "S005", 
    "VII": "S005", 
    "IX": "S009", 
    "VIII":"S007"
    }
print(*set(dict1.values()))


'''
Задача 4. Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
Input: [0, -1, 5, 2, 3] 
Output: 2 (-1 < 5, 2 < 3)
'''

length_input_3 = int(input("Введите длину списка: "))
min_input_3 = int(input("Введите минимальное значение списка: "))
max_input_3 = int(input("Введите максимальное значение списка: "))
list3 = random_int_list(length_input_3, min_input_3, max_input_3)
counter = 0
for i in range (1, len(list3)):
    if list3[i] > list3[i-1]:
        counter += 1

print(list3)
print(counter)    