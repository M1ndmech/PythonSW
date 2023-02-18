import math

# values = [1, 23, 42]
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


# test_1 = tuple(filter(lambda x: (x > 3) and (x < 40), values))
# print(test_1)


# test_2 = []
# for item in values:
#     if ((item > 3) and (item < 40)):
#         test_2.append(item)
        
# test_2 = [item for item in values if ((item > 3) and (item < 40))]
# print(test_2)


'''
У вас есть код, который вы не можете менять 
(так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 
transformation = <???> 
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] или любой другой список
transormed_values = list(map(transformation, values)) 
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation. 
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
а нужно получить его как есть. 
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
'''

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(lambda x: x, values))
# # values.append(1)
# # print(values)
# print(transformed_values)


'''
Планеты вращаются вокруг звезд по эллиптическим орбитам. 
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
по которой вращается самая далекая планета. Круговые орбиты не учитывайте: 
вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. 
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
При решении задачи используйте списочные выражения. 
Подсказка: проще всего будет найти эллипс в два шага: 
сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. 
Гарантируется, что самая далекая планета ровно одна
'''
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(*find_farthest_orbit(orbits))
# 2.5 10

#почитать про работу с десятичными дробями - округление и т.д.

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
orbits_elliptic = [item for item in orbits if item [0] != item [1]]
max_elliptic_length = max(list(map(lambda x: math.pi*x[0]*x[1], orbits_elliptic)))
longest_orbit = [item for item in orbits_elliptic if math.pi*item[0]*item[1] == max_elliptic_length]

print('{:.4f}'.format(max_elliptic_length))
print(*longest_orbit)


# def find_farthest_orbit(orbits):
#     return max(orbits, key=lambda x:(x[0] != x[1])* x[0] * x[1])

# orbits = [(1, 3), (2.5, 10), (7, 2), (6,6)]
# print(find_farthest_orbit(orbits))
# print(orbits.index(find_farthest_orbit(orbits)))


'''
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
'''

def same_by (characteristic, values):
    if not values:
        return True
    return len(set(map(characteristic, values))) == 1

values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values): 
    print('same')
else:
    print('different')