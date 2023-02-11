'''
Последовательностью Фибоначчи называется последовательность чисел 
a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
Требуется найти N-е число Фибоначчи
Input: 7 
Output: 21
'''

def fibonacci (a):
    if a == 1 or a == 2:
        return 1
    else:
        return fibonacci (a-1) + fibonacci (a-2)

fibonacci_input = int(input('Введите номер числа в посследовательности Фибоначчи:'))
print(fibonacci(fibonacci_input))

fib_list = []
for i in range (1, fibonacci_input + 1):
    fib_list.append(fibonacci(i))
print(fib_list)


'''
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные. 
Input: 5 -> 1 3 3 3 4 
Output: 1 3 3 3 1
'''
def input_int_list (length, comment = ""):
    list = []
    for i in range (length):
        input_symbol = input(f'Введите {i+1} {comment}: ')
        list.append(int(input_symbol))
    return list

def max_min_replace (list_original: list[int]):
    minimum = min(list_original)
    maximum = max(list_original)
    list_new = list_original[:]
    #list_new = list_original.copy()
    for k in range(len(list_original)):
        if list_original [k] == maximum:
            list_new [k] = minimum
    return list_new 

marks_quantity = int(input('Введите количество оценок:'))
marks = input_int_list(marks_quantity, "оценку")

print(marks)
print(max_min_replace(marks))


'''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым 
Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
'''

def simple_check (n_input: int) -> bool:
    for i in range (2, n_input):
        if n_input % i == 0:
            return False
    return True

simple_n_input = int(input('Введите число для проверки:'))

if simple_check(simple_n_input) == True:
    print(f'Число {simple_n_input} простое')
else:
    print(f'Число {simple_n_input} не является простым')

'''
Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке. 
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). 
Input:    2 -> 3 4 Output: 4 3
'''

def recursive_reverse (n):
    if n == 0:
        return ""
    else:
        num = input('Введите число: ')
        return recursive_reverse(n - 1) + num

list_length = int(input('Введите длину списка для переворачивания: '))
print(recursive_reverse(list_length))