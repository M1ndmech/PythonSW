import random

'''
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут 
в первом массиве), которых нет во втором массиве. 
Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. 
Затем элементы второго массива
Ввод: 
7 
3 1 3 4 2 4 12 
6 
4 15 43 1 15 1 
Вывод: 3 3 2 12  
(каждое число вводится с новой строки)
'''
def random_int_list (length, min, max):
    list = []
    for i in range (length):
        list.append(random.randint(min,max))
    return list

def input_int_list (length, comment = "элемент"):
    list = []
    for i in range (length):
        input_symbol = input(f'Введите {i+1} {comment}: ')
        list.append(int(input_symbol))
    return list

# n_length = int(input('Введите длину списка:'))
# n_list = input_int_list(n_length)
# m_length = int(input('Введите длину списка:'))
# m_list = input_int_list(m_length)

def not_in_second_array (list1 = [], list2 = []) -> list:
    new_list = []
    for item in list1:
        if item not in list2:
            new_list.append(item)
    return new_list

# print(n_list)
# print(m_list)
# print(not_in_second_array(n_list, m_list))

'''
Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел. 
Ввод: 5
Ввод: 1 2 3 4 5 
Вывод: 0
'''

# k_length = int(input('Введите длину списка:'))
# k_list = random_int_list(k_length, 0, 10)

def check_neighbours (input_list):
    count = 0
    for i in range (1, len(input_list) - 1):
        if input_list[i] > input_list[i-1] and input_list[i] > input_list[i+1]:
            count +=1
    return count

# print(k_list)
# print(check_neighbours(k_list))

'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках. 
Ввод: 1 2 3 2 3
Вывод: 2
'''

# g_length = int(input('Введите длину списка:'))
# g_list = random_int_list(g_length, 0, 10)

def check_pairs (list1):
    count = 0
    for i in range (len(list1)):
        for j in range (i + 1, len(list1)):
            if list1 [i] == list1 [j]:
                count += 1
    return (count)

# print(g_list)
# print(check_pairs(g_list))

'''
Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает на вход одно натуральное число k, не превосходящее 10^5. 
Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. 
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает). 
Ввод:300
Вывод: 220 284
'''

number_friend_check = int(input('Введите число для проверки:'))

def divisors_sum (input_number):
    sum = 0
    for i in range (1, input_number):
        if input_number % i == 0:
            sum += i
    return sum

def friendly_pairs (input_number):
    for i in range (2, input_number + 1):
        j = divisors_sum (i)
        if i <= (input_number) and j <= (input_number):
            print(i, j)

friendly_pairs(number_friend_check)

# без дублей:

# n = int(input())
# list_1 = list()

# for i in range(n):
#     summa = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#             summa += j
#     list_1.append(tuple([i, summa]))


# for i in range(len(list_1)):
#     for j in range(i, len(list_1)):
#         if (i != j) and (list_1[i][0]) == (list_1[j][1]) and (list_1[i][1]) == (list_1[j][0]):
#             print(*list_1[i])
