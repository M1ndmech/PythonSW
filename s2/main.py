'''
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while 

Input:       5 
Output:    120
'''

factorial_input = int(input('Введите число для вычисления его факториала: '))
factorial = 1
i = 1
while (i <= factorial_input):
    factorial *= i
    i += 1
print (factorial)


'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1. 
1 1 2 3 5 8 13
Input:   5
Output:  6
'''


a = int(input('Введите число Фибоначчи: '))
number = a

if (a == 0):
    print(0)
else:
    fibPrev, fibNext = 0, 1
    n = 1
    while(fibNext <= a):
        if(fibNext == a):
            print(f'{number} является {n}-м по счету числом Фибоначчи.')
            break
        fibPrev, fibNext = fibNext, fibPrev + fibNext
        n += 1
    else:
        print(f'{number} не является числом Фибоначчи, введите другое число.')


'''
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50 
Input:    6 -> -20 30 -40 50 10 -10 
Output: 2
'''

import random

days = int(input("Введите количество дней наблюдений: "))
list_temp = []
for i in range (days):
    # temp = int (input(f'Введите температуру в {i+1} день: '))
    # list_temp.append(temp)
    list_temp.append(random.randint(-10,10))
print (list_temp)

count = 0
period = 0
for item in list_temp:
    if item > 0:
        count += 1
        if count > period:
            period = count
    else:
        count = 0
print (period)
