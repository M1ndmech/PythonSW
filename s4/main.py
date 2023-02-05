'''
1. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n. 
Input: a a a b c a a d c d d 
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''

def input_list (length):
    list = []
    for i in range (length):
        input_symbol = input('Введите символ: ')
        list.append(input_symbol)
    return list

length_input = int(input("Введите длину списка: "))
list1 = input_list(length_input)
set1 = set(list1)

for item in set1:
    print(f'{item}: {list1.count(item)}')

'''альтернатива'''
# list_1 = input("Введите слово: ")
# temp = list_1[0]
# count = 0
# dict_1 = {}
# for i in range(len(list_1)):
#     for j in range(len(list_1)):
#         if list_1[i] == list_1[j]:
#             count += 1
#     dict_1[list_1[i]] = count
#     count = 0
# print(dict_1)


'''
2. Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
Определите, сколько различных слов содержится в этом тексте. 

Input: She sells sea shells on the sea shore 
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore 
I'm sure that the shells are sea shore shells 
Output: 13'''

str_test = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells" 
str_test2 = str_test.lower()
set2 = set(str_test2.split(" "))
print(set2)
print(len(set2))

#print(dir(a)) - выводит все методы для типа класса

'''
3. Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
“Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, которая завершается 
первым встретившимся нулем (число 0 не входит в последовательность)”. 
Однако 2  друга оказались не такими смышлеными. 
Никто из ребят не смог до конца сделать это задание. 
Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
За помощью товарищи обратились к Вам, студентам.
'''

input_num_list = input('Введите последовательность целых чисел: ')
list_num = input_num_list.split("0")
list_num_check = int(list_num[0])
max_num = 0
while list_num_check > 0:
    if list_num_check % 10 > max_num:
        max_num = list_num_check % 10
        break
    list_num_check // 10

print(max_num)

# оператор присваивания, или моржовый оператор - на заметку
# maxx = 0
# while (x:=int(input("Введите число: "))) != 0:
#     if x > maxx:
#         maxx = x
# print(f'Максимальное из введённых число: {maxx}')
