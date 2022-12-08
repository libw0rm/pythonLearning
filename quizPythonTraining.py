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

''' Q[004]
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

# ''' 
def mult(a, b):
    i = 0
    while i <= 10:
        a, b = b, b + a
        print(b)
        i += 1
mult(0, 1)