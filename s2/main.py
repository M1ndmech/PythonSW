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
