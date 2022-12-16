''' Q[001]
a = [0, 1, 0]
b = [1, 1, 0]
s = 0

for x in (a,b,a):
    s += x.count(1)

print(s)
# '''

''' Q[002]
a = (0, 1, 2, 3, 4, 5)
b = slice(0, 2)
print(a[b])
# '''

''' Q[003]
def f1():
    x = 100
    print(x)
x = + 1
f1()
# '''

''' Q[004] Что выведет (a)
a = {3, 4, 5}
a.update([1, 2, 3])
print(a)
# '''

'''Q[005]
def foo(x):
    x = ['def', 'abc']
    return (x) and id(x)

q =['123', '456']
z = foo([0][0])

# check id for everythink
print('id_foo:', id(foo))
print('id_foo(q):', id(foo(q)))
print('id_foo(z):', id(foo(z))) 
print('id_(q):', id(q), '<-', q)
print('id_(z):', id(z), '<-', z)
print('id_(q[0]):', id(q[0]),'<-', (q[0]))
print('id_(q[1]):', id(q[1]),'<-', (q[1]))
print('id_(q[1][0]-4):', id(q[1][0]), '<-', q[1][0])
print('id_(q[1][1]-5):', id(q[1][1]), '<-', q[1][1])
print('id_(q[1][2]-6):', id(q[1][2]), '<-', q[1][2])
print('id_foo(x[0][0]-d):', id(foo([0][0])), '<-', z, '<->', foo([0][0]))
# '''

# ''' Q[006] Какой тип у (X)
x = {x for x in range(3)}
print(type(x))
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
# переменные для всех
writters_tuple = ('Orwell', 'Tolkien', 'Doyle', 'Joyce')
keychron_list = ['Keychron', 'K6', 'RGB', 'HotSwap']
keyboard_dict = {'Product'       : 'Keyboard', 
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
# '''


# print('"Doyle" in tuple:', writters_tuple.index('Doyle'))  # =2
# print('"Doyle" in list:','Doyle' in keychron_list) # False
# print('"K6" in list:','K6' in keychron_list) # False
# print('Doyle' in writters_tuple) # True
# print('Doyle' in keyboard_dict)
# '''

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


'''
# СПИСКИ В PYTHON
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

'''
for d in range(1, 10000):
    n = 3
    s = 38
    while s <= 1200:
        s = s + d
        n = n + 7 
    if n == 150:
        print(f' d{d}:n{n}:s{s}')
# '''


# ''' CHESS

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

''' [Tool] Multiplication table generator
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
def multiplication_table_user_mode(intX, intY):
    # math
    product = intX * intY

    # output at screen
    # print(f'{intX} x {intY} = {product}')
    return (f'{intX} x {intY} = {product}')

print(multiplication_table_user_mode(4, 10))
# ''' 


# a = int(input('Enter first: '))
# b = int(input('Enter second: '))
a = 64187263498761287364761425199182531
b = 12765497168234781629351234147122
i = 1

# # первый вариает
# while b != 0:
#     i += 1
#     print(f'Debug case [{i}] start> {a}:{b}')
#     if a > b:
#         a -= b
#     else:
#         b -= a
#         print(f'Debug case ELSE> {a}:{b}')
#     print(f'{a+b}, {i}')

while a >= 0 or b >= 0:
    i += 1
    print(f'DEBUG case [{i}] start> {a}:{b}')

    if a > b:
        print(f'DEBUG case preIF> {a}:{b}')
        a %= b
        print(f'DEBUG case IF> {a}:{b}')
    elif b > a:
        b %= a
        print(f'DEBUG case ELSE> {a}:{b}')
print(f'result = {a+b}, count = {i}')