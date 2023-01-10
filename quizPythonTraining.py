''' Q[001]
a = [0, 1, 0]
b = [1, 1, 0]
s = 0

for x in (a,b,a):
    s += x.count(1)

# print(s)
# '''

''' Q[002] 
a = (0, 1, 2, 3, 4, 5)
b = slice(0, 2)
# print(a[b])
# '''

''' Q[003]
def f1():
    x = 100
    print(x)
x = + 1
# f1()
# '''

''' Q[004]
a = {3, 4, 5}
a.update([1, 2, 3])
# print(a)
# '''

'''Q[005]
def foo(x):
    x = ['def', 'abc']
    return (x) and id(x)

q =['123', '456']
z = foo([0][0])
# '''

''' Q[006] Какой тип у (x)
from math import sqrt
x = {x for x in range(3)}
# print(type(x))
# '''


''' Q[007]
s = 'foo'
t = 'bar'
# print('barf' in 2 * (s+t))
# '''

''' Q[008]
a = b = None, 1
# print(a if a is b else b + a)
# '''

''' Q[009]
a = [1, [2, 3]]
b = a
c = a[:]

a[1][0] = 1

print('\vDEBUG: посмотрим содержимое списков и id объектов')
print(f"id(a):, {a} {id(a)}") # [1, [1, 3]]
print(f"id(b):, {b} {id(b)}") # [1, [1, 3]]
print(f"id(c):, {c} {id(c)}") # [1, [1, 3]]

print('\vDEBUG: посмотрим элементы списков a, c и их id')
print(f"id(a[0])    | {a[0]} : {id(a[0])}")
print(f"id(c[0])    | {c[0]} : {id(c[0])}")
print(f"id(a[1])    | {a[1]} : {id(a[1])}")
print(f"id(c[1])    | {c[1]} : {id(c[1])}")
print(f"id(a[1][1]) | {a[1][1]} : {id(a[1][1])}")
print(f"id(c[1][1]) | {c[1][1]} : {id(c[1][1])}")

print('\vDEBUG: объекты на которые ссылаются a и c - разные')
print(f"id(a) == id(c) : {bool({id(a)} == {id(c)})} ")

print('\vDEBUG: но элементы объектов, на которые ссылаются a и c - идентичны')
print(f"a[0] == c[0] : {bool({id(a[0])} == {id(c[0])})} ")
print(f"a[1] == c[1] : {bool({id(a[1])} == {id(c[1])})} ")
print(f"a[1][1] == c[1][1] : {bool({id(a[1][1])} == {id(c[1][1])})}")
# '''

''' Q[010] Каким будет результат выполнения кода?
a = {1 : 'a', 2 : 'b'}
b = {2 : 'c', 3 : 'd'}
c = {**a, **b} 

# print(c[2])
# '''

''' Q[011]
list = [0]
for n in range(10):
    if n % 2 != 0:
        print(f'DEBUG case in IF #{n}: {n % 2}')
        list.append(n)

# print(max(list) - min(list))    
# '''


''' Что выдаст X?
x = 'abc'
x.replace('a', '1')
x + 'def'
print(x)
# '''










'''
________ _______ _______ _______ _______ _______ _______ _______ ________ 
|\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | |
| |F  | | |U  | | |N  | | |C  | | |T  | | |I  | | |O  | | |N  | | |S  | |
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|
'''


''' Fibonachi
def mult(a, b):
    i = 0
    while i <= 10:
        a, b = b, b + a
        print(b)
        i += 1
        
mult(0, 1)
# '''

''' Factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

print(factorial(10))
# '''

''' Поиск НОД
# a = int(input('Enter first: '))
# b = int(input('Enter second: '))

# # первый вариант
# while b != 0:
#     i += 1
#     print(f'Debug case [{i}] start> {a}:{b}')
#     if a > b:
#         a -= b
#     else:
#         b -= a
#         print(f'Debug case ELSE> {a}:{b}')
#     print(f'{a+b}, {i}')

# while a >= 0 or b >= 0:
#     i += 1
#     print(f'DEBUG case [{i}] start> {a}:{b}')

#     if a > b:
#         print(f'DEBUG case preIF> {a}:{b}')
#         a %= b
#         print(f'DEBUG case IF> {a}:{b}')
#     elif b > a:
#         b %= a
#         print(f'DEBUG case ELSE> {a}:{b}')
# print(f'result = {a+b}, count = {i}')

#  Отличный вариант
a = int(input("Enter first any number: "))
b = int(input("Enter second any number: "))
i = 1 
while b!= 0:
    a %= b
    print(f'Debug case {i}:  {a} : {b}')
    a, b = b, a
    i += 1
print(a)
# '''

''' Поиск простых чисел
# inputInt = int(input("Num-num: "))
inputInt = 10
list = []
tuple = ()
k = 0
i = 0
for inputInt in range(3, inputInt + 1, 2):
# for inputInt in range(1, inputInt):
    k += 1
    if  inputInt % 2 != 0 and \
        inputInt % 3 != 0 and \
        inputInt % 5 != 0 and \
        inputInt % 7 != 0:
            list.append(inputInt)
            i += 1
print(list)
# '''

''' Проверка простых чисел
from math import sqrt

# n = int(input("n= "))
n = 20
lst = []
score = 0
for i in range(3, n+1, 2):
    print("DEBUG case", i)
    print(lst)
    score += 1
    if (i > 10) and (i % 10 == 5):
        continue
    print("DEBUG case in {first if}:", i)
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            print("DEBUG case in {lst.append}:" , i)
            break
        if (i % j == 0):
            print("DEBUG case in {if = i%j>break}: ", i)
            break
    else:
        lst.append(i)
print (f'score: {score} >>> list: {lst}')
# '''

''' 
import random
epic = 'EPIC'
print(f'{epic:#<10}') # EPIC######
print(f'{epic:_>14}') # __________EPIC
print(f'{epic:.^32}') # ..............EPIC..............
# '''

'''# функция, которая найдёт общее начало
# исходный массив со строками
strs = ['дом', 'домен', 'домра', 'домирак']

def longestCommonPrefix(strs):
	# на старте общее начало пустое
	prefix = []
	# разбираем слова побуквенно в отдельные списки и перебираем их по очереди
	for x in zip(*strs):
		# смотрим, сколько уникальных элементов у нас получилось в наборе на этом этапе
		if len(set(x)) == 1:
			# если уникальный элемент один — добавляем его к общему началу
			prefix.append(x[0])
		# если уникальных элементов было больше одного
		else:
			# прерываем цикл и выходим из него
			break
	# возращаем результат работы функции
	# если общее начало пустое, то на выходе получим тоже пустую строку
	return "".join(prefix)
# выводим результат работы функции
print(longestCommonPrefix(strs))
# '''


''' # функция, которая посчитает число пи
def count_pi(n):
	# общее количество бросков
    i = 0
# сколько из них попало в круг
    count = 0
    # пока мы не дошли до финального броска
    while i < n:
        # случайным образом получаем координаты x и y
        x = random.random()
        y = random.random()
        # проверяем, попали мы в круг или нет
        if (pow(x, 2) + pow(y, 2)) < 1:
		# если попали — увеличиваем счётчик на 1
            count += 1
	# в любом случае увеличиваем общий счётчик
        i += 1
    # считаем и возвращаем число пи
    return 4 * (count / n)


# запускаем функцию
pi = count_pi(1_000_000)
# выводим результат
print(pi)
# '''




''' [$Perversions] String and methods
clear = 'Keychrone K6 RGB HotSwap'
upper = 'Keychrone K6 RGB HotSwap'.upper()
lower = 'Keychrone K6 RGB HotSwap'.lower()
capitalize = 'Keychrone K6 RGB HotSwap'.capitalize()
startswith = 'Keychrone K6 RGB HotSwap'.startswith('Key')
startswithMiddle = 'Keychrone K6 RGB HotSwap'.startswith('K6')
endswitchWithI = 'Keychrone K6 RGB HotSwap'.endswith('swap')
endswitchWithOutI = 'Keychrone K6 RGB HotSwap'.endswith('Swap')
endswitchMid = 'Keychrone K6 RGB HotSwap'.endswith('RGB')
another = 'Keychrone K6 RGB HotSwap'.find('K6')
anotherLow = 'Keychrone K6 RGB HotSwap'.find('k6')
replace = 'Keychrone K6 RGB HotSwap'.replace('K6', 'K2')
len = len('Keychrone K6 RGB HotSwap')

# Output Strings Perversions
print('\nOutput Strings Perversions')
print('Method:[option]: bool\n')
print('clear:', clear)
print('upper:', upper)
print('lower:', lower)
print('capitalize:', capitalize)
print('startswith:[Key]:', startswith)
print('startswithMiddle:[K6]:', startswithMiddle)
print('endswitchWithI:[swap]:', endswitchWithI)
print('endswitchWithOutI:[Swap]:', endswitchWithOutI)
print('endswitchMid:[RGB]:', endswitchMid)
print('another:[K6]:', another)
print('anotherLow:[k6]:', anotherLow)
print('replace:[K6, K2]:', replace)
print('replace:[K6, K2][RGB, White]:', replace)
print('len:', len)
# '''

''' Reverse fun

writters_tuple = ('Orwell', 'Tolkien', 'Doyle', 'Joyce')
keychron_list = ['Keychron', 'K6', 'RGB', 'HotSwap']
keyboard_dict = {   
                'Product'       : 'Keyboard', 
                'Manufacture'   : 'Keychron',
                'Model'         : 'K6',
                'Highlight'     : 'RGB',
                'Switch'        : 'Brown',
            }

name = 'Alice'
hero = 'Harry'
guide = 'Dobby'
enemy = 'Lord V.'

charactersDict = {hero, guide, enemy} 
charactersTuple = (hero, guide, enemy)
charactersList = [hero, guide, enemy]
# '''

''' Принтование characters
print('\nOutput characters Dict, Tuple and List\n')
print('id charactersDict:', id(charactersDict))
print('out of  charactersDict:\n', charactersDict, '\n')
print('id charactersTuple:', id(charactersTuple))
print('out of charactersTuple:\n', charactersTuple, '\n')
print('id charactersList:', id(charactersList))
print('out of  charactersList:\n', charactersList, '\n')

clone_army_again = {hero, guide, enemy, enemy, enemy, enemy}
print('inside clone_army_again:', clone_army_again)
print('id@clone_army_again:', id(clone_army_again))
print('hash(enemy): ', hash(enemy))

print('"Doyle" in tuple:', writters_tuple.index('Doyle'))  # =2
print('"Doyle" in list:','Doyle' in keychron_list) # False
print('"K6" in list:','K6' in keychron_list) # False
print('Doyle' in writters_tuple) # True
print('Doyle' in keyboard_dict)
# '''

''' # СПИСКИ В PYTHON
animalListAU = ['quokka', 'capybara', 'wombat', 'qoull']
print(animalListAU)
# ['quokka', 'capybara', 'wombat', 'qoull']

# присоединение элемента в конец списка
animalListAU.append('kengoo')
print(animalListAU)
# ['quokka', 'capybara', 'wombat', 'qoull', 'kengoo']

# присоединение элемента в прозвольную позицию списка
animalListAU.insert(0, 'devil')
print(animalListAU)
# ['devil', 'quokka', 'capybara', 'wombat', 'qoull', 'kengoo']

# удаление элемента с известной позицией
del animalListAU[0]
print(animalListAU)
# ['quokka', 'capybara', 'wombat', 'qoull', 'kengoo']

# удаление последнего элемента
animalListAU.pop()
print(animalListAU)
# ['quokka', 'capybara', 'wombat', 'qoull']

# удаление с pop() по индексу
animalListAU.pop(2)
print(animalListAU)
# ['quokka', 'capybara', 'qoull']

# удаление элемента по значению
animalListAU.remove('capybara')
print(animalListAU)
# ['quokka', 'qoull']

animalListAU = ['quokka', 'capybara', 'wombat', 'qoull']
print(animalListAU)
auid = id(animalListAU)

# сортировка списка перезаписывает индекс и значение исходного списка
# id списка остаётся прежним
animalListAU.sort()
print(animalListAU)
# ['capybara', 'qoull', 'quokka', 'wombat']

# сортировка обратная
# animalListAU.sort(reverse=True)
animalListAU.reverse()
# ['wombat', 'quokka', 'qoull', 'capybara']

# временная сортировка sorted()
print(sorted(animalListAU))
# ['capybara', 'qoull', 'quokka', 'wombat']

# длина списка
print(len(animalListAU))
print('reverse', animalListAU)

for value in animalListAU:
    print(value)
# '''

# square = [value ** 2 for value in range(1, 11)]
# print(min(square))
# print(max(square))
# print(sum(square))

''' просто задачка
for d in range(1, 10000):
    n = 3
    s = 38
    while s <= 1200:
        s = s + d
        n = n + 7 
    if n == 150:
        print(f' d{d}:n{n}:s{s}')
# '''


''' CHESS

HEIGHT = 8
WEIGHT = 8

boardRow    = ['1', '2', '3', '4', '5', '6', '7', '8']
boardColumn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
INFOINDEX   = ['0', '1', '2', '3', '4', '5', '6', '7']

boardBlackPlaceList = (
'8b', '8d', '8f', '8h',
'7a', '7c', '7e', '7g',
'6b', '6d', '6f', '6h',
'5a', '5c', '5e', '5g',
'4b', '4d', '4f', '4h',
'3a', '3c', '3e', '3g',
'2b', '2d', '2f', '2h',
'1a', '1c', '1e', '1g',
)
boardBlackPlaceDict = {
'8b':'', '8d':'', '8f':'', '8h':'',
'7a':'', '7c':'', '7e':'', '7g':'', 
'6b':'', '6d':'', '6f':'', '6h':'', 
'5a':'', '5c':'', '5e':'', '5g':'',
'4b':'', '4d':'', '4f':'', '4h':'', 
'3a':'', '3c':'', '3e':'', '3g':'',
'2b':'', '2d':'', '2f':'', '2h':'', 
'1a':'', '1c':'', '1e':'', '1g':'',
}
boardStarting = {
'8a': 'WR', '8b': 'Wn', '8c': 'WB', '8d': 'WQ', '8e': 'WK', '8f': 'WB', '8g': 'Wn', '8h': 'WR', 
'7a': 'WP', '7b': 'WP', '7c': 'WP', '7d': 'WP', '7e': 'WP', '7f': 'WP', '7g': 'WP', '7h': 'WP', 
'6a': '',   '6b': '',   '6c': '',   '6d': '',   '6e': '',   '6f': '',   '6g': '',   '6h': '', 
'5a': '',   '5b': '',   '5c': '',   '5d': '',   '5e': '',   '5f': '',   '5g': '',   '5h': '', 
'4a': '',   '4b': '',   '4c': '',   '4d': '',   '4e': '',   '4f': '',   '4g': '',   '4h': '', 
'3a': '',   '3b': '',   '3c': '',   '3d': '',   '3e': '',   '3f': '',   '3g': '',   '3h': '', 
'2a': 'WP', '2b': 'WP', '2c': 'WP', '2d': 'WP', '2e': 'WP', '2f': 'WP', '2g': 'WP', '2h': 'WP', 
'1a': 'WR', '1b': 'WN', '1c': 'WB', '1d': 'WQ', '1e': 'WK', '1f': 'WB', '1g': 'WN', '1h': 'WR', 
}
chessBoardDict = {
'8a': '', '8b': '', '8c': '', '8d': '', '8e': '', '8f': '', '8g': '', '8h': '', 
'7a': '', '7b': '', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '', 
'6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '', 
'5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '', 
'4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '', 
'3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '', 
'2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '', 
'1a': '', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '', 
}
chessBoardList = [
['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h'], 
['2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h'], 
['3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h'], 
['4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h'], 
['5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h'], 
['6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h'], 
['7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h'], 
['8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h'], 
]

def blackPlace():
    for i in range(7, -1, -1):
        if i % 2 == 0: print(chessBoardList[i][0::2])
        else: print(chessBoardList[i][1::2])
        i += 1

# # генерация пустого словаря для поля
# for row in range(1, 9):
#     for column in range(0, 8):
#         print(f'\'{row}{boardColumn[column]}\': \'\',')

# # генерация чёрных клеток
# # цикл для рядов 1, 3, 5, 7
# for row in range(1, WEIGHT, 2):
#     for column in range(0, HEIGHT, 2):
#         print(f'black: {row}{boardColumn[column]}')
# # цикл для рядов 2, 4, 6, 8
# for row in range(2, 9, 2):
#     for column in range(1, 8, 2):
#         print(f'black: {row}{boardColumn[column]}')

# print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
# print('-+-+-')

# def multiplyIndex(int):
#     i = 0
#     a, b = 0, 8
#     for i in range(int):
#         a, b = b, b + 8
#         print(f'[{a}:{b}]')
#         i += 1

# print(multiplyIndex(8))
# '''

''' [Tool] Multiplication table generator
# 
def multiplication_table_generator():
    multiplier = 1
    multiplicand = 1
    for multiplier in range(1, 10):
        for multiplicand in range(1, 10):
            product = multiplier * multiplicand
            print(f'{multiplier} x {multiplicand} = {product }')

multiplication_table_generator()
# ''' 

''' [Tool] Multiplication function with parameters
# 
def multiplication_table_user_mode(intX, intY):
    # math
    product = intX * intY

    # output at screen
    # print(f'{intX} x {intY} = {product}')
    return (f'{intX} x {intY} = {product}')

print(multiplication_table_user_mode(4, 10))
# ''' 

''' сколько резюме читает HR-команда в крупной компании, 2022 год
# YEAR
YWORKHOURS = 1973                                # рабочих часов в 2022 году
YWORKDAYS = 248                                  # рабочих дней в 2022 году
HOURS_PER_DAY = int(round(YWORKHOURS / YWORKDAYS, 1))
DAYS_PER_MONTH = int(round(YWORKDAYS // 12))
HR_COUNT = 10                                   # количество HR'ов
messageTotal = 5_000_000  # примерное количество откликов в год


print(f'HOURS_PER_DAY   : {HOURS_PER_DAY}')
print(f'DAYS_PER_MONTH  : {DAYS_PER_MONTH}')

msgPerMonth = messageTotal // (247//12)
print(f'Писем на HR\'a в год: {msgPerMonth}')
mesPerHRMonth = msgPerMonth // HR_COUNT
print(f'Писем на HR\'a в месяц: {mesPerHRMonth}')
mesPerHRDay = mesPerHRMonth // 20
print(f'Писем на HR\'a в день: {mesPerHRDay}')
mesPerHour = mesPerHRDay // 8
print(f'Писем на HR\'a в час: {mesPerHour} | нагрузка 100% (8 ч/д)')
mesPerHour = mesPerHRDay // 4
print(f'Писем на HR\'a в час: {mesPerHour} | нагрузка 50% (4 ч/д)')
mesPerHour = mesPerHRDay // 2
print(f'Писем на HR\'a в час: {mesPerHour} | нагрузка 25% (2 ч/д)')


# '''