'''
1. За день машина проезжает n километров. Сколько дней нужно, 
чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

**Input:**
n = 700
m = 750

**Output:**
2
'''

n = int(input('Введите пробег авто за день:'))
m = int(input('Введите длину маршрута:'))
print (f'Количество дней на маршрут: {(m + n - 1)//n}', end = ' ')
print ('д')

'''
2. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них. 

Input: 20 21 22(ввод чисел НЕ в одну строку) 
Output: 32
'''
class_1 = int(input('Введите количество учеников в классе 1:'))
class_2 = int(input('Введите количество учеников в классе 2:'))
class_3 = int(input('Введите количество учеников в классе 3:'))

print (f'Количество парт для закупки - {(class_1 + 1)//2   +   (class_2 + 1)//2   +   (class_3 + 1)//2}')

'''
3. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
Если год является високосным, то выведите YES, иначе выведите NO. 
Напомним, что в соответствии с григорианским календарем, год является високосным, 
если его номер кратен 4, но не кратен 100, а также если он кратен 400. 

Input: 2016 
Output: YES
'''
year_input = int(input('Введите год:'))
if year_input % 400 == 0:
    print ("Yes")
elif year_input % 100 == 0:
    print ("No")
elif year_input % 4 == 0:
    print ("Yes")
else:
    print ("No")
         
year_input = int(input('Введите год:'))
if (year_input % 4 == 0) and (year_input % 100 != 0) or (year_input % 400 == 0):
    print ("Yes")
else:
    print ("No")