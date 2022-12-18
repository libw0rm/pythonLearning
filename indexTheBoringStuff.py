# Python 3.11
# АВТОМАТИЗАЦИЯ РУТИННЫХ ЗАДАЧ С ПОМОЩЬЮ PYTHON. 2-Е ИЗДАНИЕ
# AUTOMATE THE BORING STUFF WITH PYTHON. 2ND EDITION

# !Описание тегов для быстрого поиска
# [ATBF_n]   - сокращение от AUTOMATE THE BORING STUFF + номер(а) страниц(ы), всегда используется в описании коммита 🧬
# (n)        - простое указание номера страницы книги 📍
# [!n.n]     - задание для самостоятельного решения 👩🏻‍🎓
# {Training} - самостоятельный разбор, преднамеренная практика 🤯
# [.TROUBLE] - нерешённое задание 💀
# Структура коммита: # [ATBF_n]:[Описание изменения файла]. #
# Например: [ATBF_0]: описана логика файла.
# Для обозначения пробелов используется underscore ( _ )
# Например: [ATBF_32]: добавлен код со страницы 32.
# Для обозначения интервалов используется дефис/hypen ( - )
# Например: [ATBF_32-34]: добавлен код со страниц 32-34.
#
#
import time
import sys
import random
import re

# #  (52) "Ваша первая программа"
# print('Hello World!\n')
# #
# print('What is your name?')
# myName = input()
# print('Nice to meet you, ' + myName, '\n')
# print('The length your name is: ')
# print(len(myName), ' letters', '\n')
# #
# print('How old are you?')
# myAge = input()
# print('In a year you will be ' + str(int(myAge) + 1) + ' old', '\n')


# # {Training_70}
# userName = input("Enter your name: ")
# if userName == "Darkness":
#     print("Hello, " + userName + "! My old friend 🧌")
# elif userName != "Darkness":
#     print("🧟 Nobody's Home")
# else:
#     print("Go away! I do not know you!")


# # {Training_76}
# inputName = input('Enter name: ') #Carol, Alice
# inputAge = int(input('Enter age: ')) #11, 12

# if inputName == 'Alice':
#     print("Hi, Alice.")
# elif inputAge < 12:
#     print("You're not Alice, kiddo")
# else:
#     print("You're neither Alice nor a little kid.")


# # {Training_80}
# userName = ''
# while userName != 'your name':
#     print("Please type your name: ")
#     userName = input()
# else:
#     print("Thank you!")


# # [ATBF_81] Инструкция break
# while True: #создание цикла, условие которого всегда True
#     userName = input("Please type your name: ")
#     if userName == 'your name':
#         break
# print("Thank you")


# # {Training_81}
# userName = ''
# while True:
#     print("Please type your name: ")
#     userName = input()
#     if userName == 'your name':
#         break
# print("Thank you!")


# # [ATBF_83] Swordfish
# while True:
#     # userName = input("How are you? ") # Ввод будет на той же строке
#     print("How are you?")
#     userName = input()
#     if userName != "Joe": 
#         continue #Если не "Joe", то возвращаемся в 1 инструкцию
#     print("Hello, Joe. What is the password? (It is a fish.)")
#     userPassword = input()
#     if userPassword == "swordfish":
#         break
# print("Access granted.")


# # [ATBF_85] Boolean
# print(bool(0.0))        #False
# print(bool(0))          #False
# print(bool(''))         #False
# print(bool(""))         #False
# print(bool(-1))         #True
# print(bool(1))          #True
# print(bool(True))       #True
# print(bool(False))      #False
# print(bool(not False))  #True
# print(bool(not 0))      #True
# print(bool(not ''))     #True


# # [ATBF_85] 
# userName = ''
# while not userName:
#     print("Enter your name: ")
#     userName = input()
# print("How many guests will there be?")
# numOfGuest = int(input())
# if numOfGuest:
#     print("OK! Goodlike!")
# print("I go to the sleep")


# # [ATBF_86] fiveTimes
# print("My name is")
# for i in range(5):
#     print("Jimmy Five Times (" + str(i) + ")") #Нумерация цикла с (0)
#     # print("Jimmy Five Times (" + str(i+1) + ")") #Нумерация цикла с (1)


# # [ATBF_87] 5050
# total = 0
# for i in range(101):
#     total = total + i
# print(total)


# # # [ATBF_88] fiveTimes (While)
# print("My name is")
# i = 0
# while i < 5:
#     # i = i + 1 # Нумерация с (1)
#     print("Jimmy Five Times (" + str(i) + ")")
#     i = i + 1 # Нумерация с (0)


# # {Training_88-89} range()
# for i in range(0, 1000, 100):
#     # print(i, i**2)
#     print(i, i**2, i**3, i**4)


# # [ATBF_90] random
# import random
# for i in range(5):
#     print(random.random())
#     # print(random.randint(1,20))
#     # print(random.randbytes(23))

# # randomBytes = random.randbytes(23)
# # print(type(randomBytes))

# # [ATBF_91] exitExample
# import sys

# while True:
#     print('Enter \'exit\' for exit')
#     response = input()
#     if response == 'exit':
#         print('DONE. BYE!')
#         sys.exit()


# # [ATBF_92] Игра "guessTheNumber"
# import random

# secretNumber = random.randint(1, 100)
# print('Я загадал число от 1 до 100') 
# # print(secretNumber) # cheatcode 😋

# for guessesTaken in range(1, 7): # Игроку даётся 6 попыток
#     print('⛳️ Попытка номер: ' + str(guessesTaken)) # Отображён счётчик попыток
#     print('Угадай число')
#     guess = int(input())

#     if guess < secretNumber:
#         print('>>> Мало\n')
#     elif guess > secretNumber:
#         print('>>> Много\n')
#     else:
#         break
# if guess == secretNumber:
#     print('Отлично! Число отгадано за ' + str(guessesTaken) + ' попыток!')
# else:
#     print('Та-дааам! Всё, котлетки кончились! Добро пожаловать на костёр 😈 Было загадано число ' + str(secretNumber))


# # [ATBF_94] Игра RPC Game
# import random, sys

# print('КАМЕНЬ, НОЖНИЦЫ, БУМАГА')

# wins = 0    # переменная для победы 
# losses = 0  # переменная для поражения
# ties = 0    # переменная для ничьих

#     # Главный цикл игры
# while True:
#     print('%s wins, %s losses, %s ties\n' % (wins, losses, ties))

#     # Цикл выбора хода 
#     while True:
#         print('Выбери ход: (к)амень, (н)ожницы, (б)умага или ' + \
#                 '(в)ыход')
#         playerMove = input()
#         if playerMove == 'в':
#             sys.exit() # выход из программы
#         if playerMove == 'к' \
#         or playerMove == 'н' \
#         or playerMove == 'б':
#             break # выход из цикла ввода
#         print('Введи "к", "н", "б", "в"')

#     # Отображение выбора пользователя 
#     if playerMove == 'к':
#         print('КАМЕНЬ и ...')
#     if playerMove == 'н':
#         print('НОЖНИЦЫ и ...')
#     if playerMove == 'б':
#         print('БУМАГА и ...')

#     # Отображение выбора системы
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'к'
#         print('🗿 КАМЕНЬ')
#     if randomNumber == 2:
#         computerMove = 'н'
#         print('✂️ НОЖНИЦЫ')
#     if randomNumber == 3:
#         computerMove = 'б'
#         print('🧻 БУМАГА')

#     # Отображение и учёт результатов
#     if playerMove == computerMove:
#         print('🤝 Ничья!')
#         ties = ties + 1
#     elif playerMove == 'к' and computerMove == 'н':
#         print('🥳 Вы выиграли')
#         wins = wins + 1
#     elif playerMove == 'б' and computerMove == 'к':
#         print('🤩 Вы выиграли')
#         wins = wins + 1
#     elif playerMove == 'н' and computerMove == 'б':
#         print('🤪 Вы выиграли')
#         wins = wins + 1
#     elif playerMove == 'к' and computerMove == 'б':
#         print('😳 Вы проиграли!')
#         losses = losses + 1
#     elif playerMove == 'б' and computerMove == 'н':
#         print('👻 Вы проиграли!')
#         losses = losses + 1
#     elif playerMove == 'н' and computerMove == 'к':
#         print('😱 Вы проиграли!')
#         losses = losses + 1


# # {Training_98-99}
# # Контрольные вопросы. Задание 4
# print(bool((5 > 4) and (3 == 5)), ': (5 > 4) and (3 == 5)')
# print(bool(not (5 > 4)), ': not (5 > 4)')
# print(bool((5 > 4) or (3 == 5)), ': (5 > 4) or (3 == 5)')
# print(bool(not ((5 > 4) or (3 == 5))), ': not ((5 > 4) or (3 == 5))')
# print(bool((True and True) and (True == False)), ': (True and True) and (True == False)')
# print(bool((not False) or (not True)), ': (not False) or (not True)')
# print(bool(True and False))
# print(bool(True or False))


# # 👽 Контрольные вопросы. Задание 9
# import sys
# 
# while True:
#     spam = input('Enter number or "e": ')
#     if spam == 'e':
#         # sys.exit()
#         exit() # выход без импорта модуля
#     if spam == "1":
#         print("Hello")
#     elif spam == "2":
#         print("Howdy")
#     else:
#         print("Greetings!")
#     # break # для однократного запуска программы

# # 👽 Контрольные вопросы. Задание 12-13
# for i in range (10):
#     print(i)
# for i in range (0, 10):
#     print(i)
# for i in range (0, 10, 1):
#     print(i)

# # 👽 Контрольные вопросы. Задание 13
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # [ATBF_102] helloFunc
# def hello():
#     print('Hello!')
#     print('Hello!!!')
#     print('Hello my friends!')

# hello()
# hello()
# hello()
# # 
# def hello(userName):
#     print('Hello, ' + userName)

# hello('Vicky')
# hello('Cristina')
# hello('Barcelona')


# # [ATBF_105] magic8Ball
# import random

# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'

# shuffleNumbers = random.randint(1, 9)
# fortune = getAnswer(shuffleNumbers)
# print(fortune)
# # print(getAnswer(shuffleNumbers))
# # print(getAnswer(random.randint(1, 9)))

# # # {Training_106}
# # spamOne = 'hello form spamOne'
# # spamTwo = print('hello from spamTwo')
# # spamTwo # вывод без None
# # print(spamTwo) # вывод с None
# # print(bool(None == spamTwo)) # True
# # print(bool(None == spamOne)) # False


# {Training_107}
# import random

# rVar = random.randint(1, 10) # Random from 1 to 10
# # rVar = random.randint(10, 1) # Error
# print(rVar)

# print('Hello', end=' ')
# print('World')
# print('World_1', 'World_2', 'World_3', sep=', ')
# print('S1n', 'S2n', 'S3n', sep='\n')
# print('Tab1', 'Tab2', 'Tab3', sep='\t') 
# print('CR1', 'CR2', 'CR3', sep='\r') 
# # перезапись строки в [print] с помощью [\r], на выходе - последнее значение [CR3]
# print('CR4', 'CR5', 'CR6', sep='\r\n') 
# # теперь перезапись строки невозможна


# # [ATBF_109] abcdCallStack
# def a():
#     print('a() starts')
#     b()
#     d()
#     print('a() returns')


# def b():
#     print('b() starts')
#     c()
#     print('b() returns')

# def c():
#     print('c() starts')
#     print('c() returns')

# def d():
#     print('d() starts')
#     print('d() returns')

# a()


# {Training_112-113}
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()
# # bacon()


# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)


# def spam():
#     eggs = 'spam local'
#     print(eggs)     # spam local

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)     # 1. bacon local
#     spam()          # 2. spam local
#     print(eggs)     # 3. bacon local

# eggs = 'global'     # 4. global
# bacon()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'
#     # print(eggs)
# eggs = 'global'
# # spam()
# print(eggs)

# # LOCAL
# def firstLocalFunction():
#     numOne, numTwo, numThree = '1', '2', '3'
#     print('👻 local output_first: ' + numOne, numTwo, numThree)

# firstLocalFunction()

# def secondLocalFunction():
#     numOne, numTwo, numThree = 'a', 'b', 'c'
#     print('👻 local output_second: ' + numOne, numTwo, numThree, '\n')
# secondLocalFunction()
# # # print('local: ' + numOne, end=' ')
# # # print('local: ' + numTwo, end=' ')
# # # print('local: ' + numThree)  

# # GLOBAL

# numOne, numTwo, numThree = 'C++', 'Python', 'Assembler'

# def firstGlobalFunction():
#     global numOne, numTwo, numThree
#     # переопределение внутри функции
#     # numOne, numTwo, numThree = 'a', 'b', 'c'
#     print('🎃 global output_first: ' + numOne, numTwo, numThree)

# firstGlobalFunction()
# print('fG: ' + numOne, end=' ')
# print('fG: ' + numTwo, end=' ')
# print('fG: ' + numThree, '\n')

# # переопределим значения переменных
# numOne, numTwo, numThree = 'prod', 'beta', 'alpha'

# def secondGlobalFunction():
#     global numOne, numTwo, numThree
#     print('🐙 global output_second: ' + numOne, numTwo, numThree)

# secondGlobalFunction()
# print('sG: ' + numOne, end=' ')
# print('sG: ' + numTwo, end=' ')
# print('sG: ' + numThree)


# # [ATBF_117-119] Обработка исключений
# def spam(divideBy):
#     return 42 / divideBy
# 
# # Ниже попробуем отловить ошибки
# 
# def spam(divideBy):
#     try: # если в этом блоке случится ошибка, то программа переходит к [except]
#         return 42 / divideBy
#     except ZeroDivisionError: # здесь выводится сообщение об ошибке в блоке [try]
#         print('Error: Invalid argument. ☠️')


# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# # Выделим [try-except] и поместим туда инструкции [print]
# def spam(divideBy):
#     return 42 / divideBy

# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1)) # не будет выполнено, тк после [except] не происходит возврата в [try]
# except ZeroDivisionError:
#     print('Error: Invalid argument. ☠️')


# # [ATBF_120] ZigZag
# import time, sys

# indent = 0                  # кол-во пробелов для отступа
# indentIncreasing = True     # квеличение или умемьшение отступа

# try:
#     while True: # основной цикл
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # выставляем паузу в 0.1s (1/10)

#         if indentIncreasing:
#             indent += 1
#             if indent == 10:
#                 indentIncreasing = False
#         else:
#             indent -= 1
#             if indent == 0:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

# {Training_122-123} Контрольные вопросы

''''''
# def collatz(number):

#     if number % 2 == 0:
#         return (number // 2)  # если n кратное 2, то [n//2]

#     else:
#         return (3 * number + 1)  # если n не кратное 2, то [3n+1]

# collatz(3)  #10
# collatz(10) #5
# collatz(5)  #16
# collatz(16) #8
# collatz(8)  #4
# collatz(4)  #2
# collatz(2)  #1
# collatz(1)  #4


# def collatz(number):

#     if number % 2 == 0:
#         return (number // 2)  # если n кратное 2, то [n//2]

#     else:
#         return (3 * number + 1)  # если n не кратное 2, то [3n+1]


# userInputInteger = int(input('Enter number: '))
# i = userInputInteger
# magicInput = collatz(userInputInteger)

# while True:
#     if i == 1:
#         break
#     magicInput = i
#     print(i)
#     i = collatz(i)


# # Последовательность Коллатца
# # функция принимает целое положительное число
# def collatz(number): 

#     if number % 2 == 0: 
#         return (number // 2)    # если n кратное 2, то [n//2]

#     else: 
#         return (3 * number + 1) # если n не кратное 2, то [3n+1]

# try:  # чекаем траблы ValueError or TypeError
#     i = int(input('Enter number: '))
#     j = 0       # счётчик итераций, just for fun
#     sum = 0     # счётчик итоговых сум, just for fun

#     while i != 1:
#         i = collatz(i)
#         j += 1
#         sum += i
#         print('Step:' + str(j) + '> ' + str(i))
#     print('total sum:' + str(sum))

# except ValueError or TypeError:
#     print('Enter even number from 1 to...')


# [ATBF_126] Списки
# {Training}

''' Получение фрагмента списка с помощью среза и отрицательные индексы
animalListAU = ['quokka', 'capybara', 'wombat', 'qoull']
animalListRU = ['viper', 'bear', 'wolf' , 'crane']
animalListCA = ['beaver', 'linx', 'bison', 'puffin']
animalListSumm = [animalListAU, animalListRU, animalListCA]

print(animalListSumm[0])              # animalListAU
print(animalListSumm)                 # all lists
print(animalListSumm[1])              # animalListRU
print(animalListSumm[2])              # animalListCA
print(animalListSumm[0][2])           # wombat
print(animalListSumm[1][2])           # wolf
print(animalListSumm[2][2])           # bison
print(animalListSumm[2][2][1])        # b[i]son
print(animalListSumm[2][2][-4])       # b[i]son
print(animalListSumm[2][2][1:])       # b[ison]
print(animalListSumm[2][2][-4:])      # b[ison]
print(animalListSumm[2][2][-5:])      # [bison]
print(animalListSumm[2][2][-2:])      # bis[on]
print(animalListSumm[2][2][0:-1])     # [biso]n
print(animalListSumm[2][2][-4:-1])    # b[iso]n
print(animalListSumm[2][2][-4])       # b[i]son
print(animalListSumm[0][0:2])         # quokka, capybara
print(animalListSumm[0][-1:])         # quoll
print(animalListSumm[0][0:-2])        # quokka, capybara
print(animalListSumm[0][-2])          # wombat
print(animalListSumm[0][-2:])         # wombat, quoll
print(animalListSumm[0][-2:-1])       # wombat
print(animalListSumm[0][:])           # == list[0]
print('Hello, ' + animalListSumm[0][2])

# определение длины списка
print(len(animalListAU)) # 4 индекса
print(len(animalListSumm)) # 3 индекса 
print(len(animalListSumm[0])) # 4 индекса 
# '''

''' Изменение элементов списка с помощью индексов
animalListAU = ['quokka', 'capybara', 'wombat', 'qoull']
animalListRU = ['viper', 'bear', 'wolf' , 'crane']
animalListCA = ['beaver', 'linx', 'bison', 'puffin']
animalListSumm = [animalListAU, animalListRU, animalListCA]

animalListAU[0] = 'parrot'
animalListRU[0] = 'tiger'
animalListCA[0] = 'snake'

print(animalListAU)
print(animalListRU)
print(animalListCA)
# '''

''' 
numberListOne = [1, 2, 3]
numberListTwo = [3, 4, 5]
numberListSumm = [numberListOne, numberListTwo]

print(numberListSumm[0][2] * 2) # (3*2)
print(numberListSumm[1][1] + numberListSumm[0][1]) # 4+2
print(numberListOne, numberListTwo) # вывод списков
print(numberListOne[2]*2, numberListTwo[2]*2) # 6, 10
# '''

''' Буллевы значения и списки
boolListNum = [1,2,3]
boolListStr = ['a','b','c']
boolListBool = [True, False, False]
boolListFalse = [False, False, False]
boolListTrue = [True, True, True]
boolListNone = [None, None, None]

print(bool(boolListNum))
print(bool(boolListStr))
print(bool(boolListBool[0]))
print(bool(boolListFalse[0]))
print(bool(boolListTrue[0]))
print(bool(boolListNone))
# '''

''' Изменение элементов списка
changeListNumber = [1, 2, 3]
print(changeListNumber)  # [1, 2, 3]

changeListNumber[:] = [0, 1, 2]
print(changeListNumber)  # [0, 1, 2]
# '''

'''
concatListStrOne = ['a', 'b', 'c']
concatListStrTwo = ['d', 'e', 'f' ]
concatListIntOne = [1, 2, 3]
concatListIntTwo = [4, 5, 6]

listStrStr = concatListStrOne + concatListStrTwo
listStrInt = concatListStrOne + concatListIntOne
listIntInt = concatListIntOne + concatListIntTwo

print(listStrStr)
print(listStrInt)
print(listIntInt)

# '''

''' Удаление значений из списка с помощью {del}
delListStr = ['a', 'b', 'c']
delListInt = [1, 2, 3, 4]
print(delListInt)

del delListInt[-1]
print('Удален последний индекс со значением (4): ', delListInt)

del delListStr[0]
print('Удалено первое значение (1): ', delListInt)
# '''

''' программа allMyCats

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' or (<Enter> for exit)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('Имена кошастиков:')
for name in catNames:
    print(' ' + name)
# '''

''' цикл for со списками

for i in range(3):
    print(i)

for i in [4, 5, 6]:
    print(i)

for i in ['a', 'b', 'c']:
    print(i)
# '''

'''
animalListAU = ['quokka', 'capybara', 'wombat', 'qoull']
for i in range(len(animalListAU)):
    print('Index ' + str(i) + ': ', animalListAU[i])
# '''

''' операторы in и not in
listInt = [1, 2, 3, 4]
print(1 in listInt)         # True
print('1' in listInt)       # False
print('1' not in listInt)   # True
# '''

''' My Pets
myPets = ['Sofy', 'Piter', 'Fatty']
print('Enter name: ')
inputName = input()
if inputName not in myPets:
    print('WAT? How?')
else:
    print(inputName + ' is my pet')
# '''

''' Груповое присваивание
cat = ['fatty', 'grey', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

size, color, disposition = cat
print(size, color, disposition)
# '''

''' Использование enumerate()
animalListAU = ['quokka', 'capybara', 'wombat', 'qoull']
for index, item in enumerate(animalListAU):
    print('Index', str(index) + ':',  item)

# '''

''' использование random.choice
import random
animalList = ['quokka', 'capybara', 'wombat', 'qoull', 'beaver', 'linx', 'bison', 'puffin', 'bear', 'tiger']
# print(random.choice(animalList))

for i in range(0, 10):
    print(random.choice(animalList))

# '''

''' использование random.shuffle
import random

animalList = ['quokka', 'capybara', 'wombat', 'qoull',
            'beaver', 'linx', 'bison', 'puffin', 'bear','tiger']
print(random.shuffle(animalList)) # None, удалено из Python 3.11
print(random.choice(animalList))
print(random.choices(animalList))
# '''

# ''' ☠️ WARNING! This is Generator for 100.000.000 32b str
# import random

# a = 10000000000000000000000000000000
# b = 99999999999999999999999999999999
# i = 0

# while i <= 100000000:
#     print(random.randint(a, b))
#     i += 1

# '''


''' Комбинированные операторы присваивания
spamNum = 13

# spamNum += 1 # 14
# spamNum -= 1 # 12
# spamNum *= 1 # 13
# spamNum /= 1 # 13.0
# spamNum %= 1 # 0

print(spamNum)
# '''

''' 
# Конкатенация [+] строк и списков
spamStr = 'Hello '
spamStr += 'World'

print(spamStr)

# репликация [*] строк и списков
piggy = ['Babel']
piggy *= 3  # ['Babel', 'Babel', 'Babel']

print(piggy)
# '''

''' [ATBF_135-140] Методы списков
# метод index()
helloList = ['hello', 'greetings', 'hi',  'howdy', 'bonjour']

print(helloList.index('hi')) # 2
# '''

''' методы append() и  insert()
addList = ['cat', 'dog']
print(addList)  # ['cat', 'dog']
addList.append('mouse')
print(addList)  # ['cat', 'dog', 'mouse']
addList.insert(0, 'kitty')
print(addList)  # ['kitty', 'cat', 'dog', 'mouse']
# append() и  insert() в присваивании
# addList = addList.insert(0, 'kitty')
# print(addList)  # None
# '''

''' методы remove() и del
addList.remove('kitty') # LIST.remove('value') удаляет по значению
print('remove() kitty', addList)    # ['cat', 'dog', 'mouse']
addList.append('kitty')
print('append() kitty', addList)    # ['cat', 'dog', 'mouse']
del addList[3] # del LIST[i] удаляет по индексу
print('del[] kitty', addList)       # ['cat', 'dog', 'mouse']
# '''

''' # сортировка с помощью sort()
sortCharList = ['d', 'c', 'b', 'a']
sortNumberList = [9, 6, 3, 1]
sortNumberList.sort(reverse=True)
sortNumberList.sort()
print(sortNumberList)
# print(sortCharList.sort()) # None

# Сортировка строки
s2 = "hello"
print(sorted(s2))                 # ['e', 'h', 'l', 'l', 'o']
print(sorted(s2, reverse=True))   # ['o', 'l', 'l', 'h', 'e']

# Сортировка списка
l1 = [1, 4, 5, 2, 456, 12]
print(sorted(l1))                 # [1, 2, 4, 5, 12, 456]
print(sorted(l1, reverse=True))   # [456, 12, 5, 4, 2, 1]

# Сортировка кортежа
t1 = (15, 3, 5, 7, 9, 11, 42)
print(sorted(t1))                 # [3, 5, 7, 9, 11, 15, 42]
print(sorted(t1, reverse=True))   # [42, 15, 11, 9, 7, 5, 3]

# Сортировка списка кортежей
t2 = [(1, 2), (11, 12), (0, 2), (3, 2)]
print(sorted(t2))                 # [(0, 2), (1, 2), (3, 2), (11, 12)]
print(sorted(t2, reverse=True))   # [(11, 12), (3, 2), (1, 2), (0, 2)]

# Сортировка множества
s1 = {1, 4, 3, 6, 2, 8, 11, 32}
print(sorted(s1))                 # [1, 2, 3, 4, 6, 8, 11, 32]
print(sorted(s1, reverse=True))   # [32, 11, 8, 6, 4, 3, 2, 1]

# Сортировка словаря
d1 = {2: 'red', 1: 'green', 3: 'blue'}
# Вернется список отсортированных ключей
print(sorted(d1))   # [1, 2, 3]

# Вернется список отсортированных значений
print(sorted(d1.values()))   # ['blue', 'green', 'red']

# Вернется список кортежей (ключ, значение), отсортированный по ключам.
print(sorted(d1.items()))   # [(1, 'green'), (2, 'red'), (3, 'blue')]

# Сортировка словаря в обратном порядке
print(sorted(d1, reverse=True))            # [3, 2, 1]
print(sorted(d1.values(), reverse=True))   # ['red', 'green', 'blue']
# [(3, 'blue'), (2, 'red'), (1, 'green')]
print(sorted(d1.items(), reverse=True))

vegetables = ['squash', 'pea', 'carrot', 'potato']
new_list = sorted(vegetables)
# new_list = ['carrot', 'pea', 'potato', 'squash']
print(new_list)
# vegetables = ['squash', 'pea', 'carrot', 'potato']
print(vegetables)

vegetables.sort()
# vegetables = ['carrot', 'pea', 'potato', 'squash']
print(vegetables)
# '''

'''
# инверсия списка с помощью reversed()
integersStringList = ['1', '2', '3', '4']
integersList = [1, 2, 3, 4]

integersStringList.reverse()
integersList.reverse()

print(integersStringList)           # ['4', '3', '2', '1']
print(integersList)                 # [4, 3, 2, 1]
print(integersStringList.reverse()) # None
# '''

''' [ATBF_142] версия Magic-8-Ball со списком
import random


magicBallMessages = [
    'It is certain',  \
    'It is decidedly so', \
    'Yes', \
    'Reply hazy try again', \
    'Ask again later', \
    'Concentrate and ask again', \
    'My reply is no', \
    'Outlook not so good', \
    'Very doubtful'
    ]

fortune = magicBallMessages[random.randint(0, len(magicBallMessages)-1)]

print(fortune)
# '''

''' [ATBF_143] списковые типы данных
nameString = 'Socrates'
print(nameString[0]) # S
print(nameString[0:3]) # Soc
print('So' in nameString) # True
print('so' in nameString) # True
print('do' in nameString) # False
print('do' in nameString or 'so' in nameString) # False
for i in nameString:
    print(str.upper('-*- ' + i + ' -*-'))
# '''

''' [ATBF_144] изменяемые и неизменяемые типы данных
# kittyName = 'Kittify'
# kittyName[4] = 'this is'
# print(kittyName)  # TypeError

eggs = [1, 2, 3]
eggs = [4, 5, 6]

print(eggs)  # [4, 5, 6]

del eggs[2]
eggs.append(7)
print(eggs)  # [4, 5, 7]
del eggs[1]
eggs.append(8)
print(eggs)  # [4, 7, 8]
del eggs[0]
eggs.append(9)
print(eggs)  # [7, 8, 9]


print('Удаление значений списка через [:] или [0:] или [0:3]')
del eggs[:]   # аналогичен [0:3], остаётся пустой список
print(eggs)     # []

print('Удаление переменной "eggs" с помощью del')
del eggs
print(eggs)  # NameError: name 'eggs' is not defined
# '''

''' Кортежи / Python Tuples

firstTuple = ('hi', 42, 0.05)
print(firstTuple[:])

try:
    firstTuple[2] = 0.5     # неизменяемость кортежа
    print(firstTuple[:])    # TypeError
except TypeError:
    print('TypeError in firstTuple')

typeTestTuple = ('hello')
print(type(('hello',)))  # <class 'tuple'>
print(type(('hello')))   # <class 'str'>
# '''

''' [ATBF_147] Преобразование типов с помощью list() и tuple()
listVeg = ['squash', 'pea', 'carrot', 'potato']
tupleBerry = ('strawberry', 'blueberry', 'cranberry')

# присвоение переменным
tempTuple = tuple(listVeg)
tempList = list(tupleBerry)

# преобразование типов 
print(tuple(listVeg))       # list to tuple
print(list(tupleBerry))     # tuple to list

# проверка типов
print(type(tempList))       # <class 'list'>
print(type(tempTuple))      # <class 'tuple'>

# обращение по индексу
print(list(tupleBerry[1]))  # ['b', 'l', 'u', 'e', 'b', 'e', 'r', 'r', 'y']
print(tuple(listVeg[0]))    # ('s', 'q', 'u', 'a', 's', 'h')
# '''

''' [ATBF_148] Ссылки
spam = 42 # spam ссылается на значение 42
cheese = spam # cheese начинает ссылаться на значение spam, то есть 42
spam = 100 # значение spam начинает ссылаться на значение 100, cheese не изменён
print('Spam:', spam) # 100
print('Cheese:', cheese) # 42
# '''

''' [ATBF_148]
# создадим список [0, 1, 2, 3, 4, 5] и запишем ссылку на него в spam
spam = [0, 1, 2, 3, 4, 5]

# cкопируем ссылку на список из spam в cheese
cheese = spam
# теперь spam и cheese ссылаются на 1 список - [0, 1, 2, 3, 4, 5]

# измененим элемент [1] нашего списка
cheese[1] = 'Ooops!'

# посмотрим что внутри
print(spam) 
print(cheese)
print(id(spam), '< id списка в spam') 
print(id(cheese), '< id списка в cheese')
# переменная cheese ссылается на тот же список
# '''

''' [ATBF_148] тождественность и id в Python
testIdListOne = ['a', 'b', 'c']
testIdListTwo = ['a', 'b', 'c']
idTestListOneFirst = id(testIdListOne)
print(id(testIdListOne), '< id testIdListOne')  # разные id
print(id(testIdListTwo), '< id testIdListTwo', '\n')  # разные id

# добавим в testIdListOne значение 'd'
# append() не создаёт новый объект списка, он изменяет существующий список
testIdListOne.append('d')
print(id(testIdListOne), testIdListOne,
      '< id testIdListOne')  # id не изменился
print(id(testIdListTwo), testIdListTwo,
      "< id testIdListTwo", '\n')

# пересоздание testIdListOne с тем же набором значений
testIdListOne = ['a', 'b', 'c', 'd']
idTestListOneSecond = id(testIdListOne)

print('Сравним id-значения списков testIdListOne: ',
      idTestListOneFirst, idTestListOneSecond,
      bool(idTestListOneFirst == idTestListOneSecond), sep='\n')
# '''

''' [ATBF_151] Передача ссылок
def passingReference(someParameter):
    someParameter.append('Hello')

# создадим список
linkList = [1, 2, 3]
print(id(linkList), linkList)

# передадим функции passingReference в качестве аргумента
# переменную linkList, которая для passingReference
# станет параметром
passingReference(linkList)  # linkList - аргумент для функции pR

print(id(linkList), linkList) # посмотрим id и вывод
# '''

''' [ATBF_152] Функции copy() и deepcopy()
# copy() позляет создать копию изменяемого значения, 
# такого как список или словарь, а не просто копию ссылки
# deepcopy() используется если список содержит вложенные списки
import copy


firstListCopy = ['A', 'B', 'C', 'D']
print(id(firstListCopy), '< id firstListCopy')

secondyListCopy = copy.copy(firstListCopy)
print(id(secondyListCopy), '< id secondyListCopy')

secondyListCopy[1] = 42
print(id(firstListCopy), firstListCopy)
print(id(secondyListCopy), secondyListCopy)
# '''

''' [ATBF_154-155] Игра "Жизнь"
import random, time, copy
WIDTH = 100
HEIGHT = 40

# Создадим список списков для клеток
nextCells = []
for x in range(WIDTH):
    column = [] # создание нового столбца
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # добавление живой кетки
        else:
            column.append(' ') # добавление мертвой клетки
    nextCells.append(column) # nextCells содержит список столбцов
    i = 0

while True:
    # print('\n\n\n\n\n') # отделим каждый шаг с помощью символов новой строки
    currentCells = copy.deepcopy(nextCells)
    i += 1

    # Вывод текущих строк на экран
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # вывод решётки или пробела
        print()

    # Вычисление клеток на следующем шаге на основе клеток текущего шага
    for x in range(WIDTH):
        for y in range(HEIGHT):
        # Получение соседних координат.
        # Выражение '% WIDTH' гарантирует, что значение
        # leftCoord всегда находится между 0 и WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # print('X-left:', leftCoord, 'X-right:', rightCoord)
            # print('Y-above:', aboveCoord, 'Y-below:', belowCoord, '\n')
        
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # жива клетка слева сверху
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # жива клетка сверху
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # жива клетка справа сверху
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # жива клетка слева
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # жива клетка справа
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1  # жива клетка слева снизу
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1  # жива клетка снизу
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1  # жива клетка справа снизу

            # Изменение клетки на основе правил
            if currentCells[x][y] == '#' and (numNeighbors == 2 or 
                                                numNeighbors == 3):
                # Живые клетки с 2 или 3 соседями остаются живыми
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Мёртвые клетки с 3 живыми соседям оживают
                nextCells[x][y] = '#'
            else:
                # все остальные умирают или остаются мертвыми
                nextCells[x][y] = ' '
    print(i)
    time.sleep(0.005)
# '''

''' [ATBF_159] Контрольные вопросы
# {Training}
# (159) Задание 2
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
spam

# (159) Задания 3, 4, 5
spam = ['а', 'b', 'с', 'f' , 'd']
spam[int('3' * 2) // 11]
# '3' * 2 = '33' => int('33') // 11 == [3]
spam[-1]  # 'd'
spam[:2]  # ['а', 'b']

# (159) Задания 6, 7, 8
bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.index('cat')) # [1]
bacon.append(99) # значение (99) будет добавлено в конец списка
print(bacon) # [3.14, 'cat', 11, 'cat', True, 99]
bacon.remove('cat') # будет удалено первое соответствующее вхождение [1]
print(bacon, '\n')

# (159) Задание 9
foo = 'bar'
bar = 'foo'
print('Конкатанация: bar + foo > ', bar + foo)  # foobar
print('Репликация: bar * foo > ', ((bar + foo) * 2), '\n')  # foobarfoobar

# (159) Задание 10. В чем разница между списковыми методами append() insert()?
foo = ['f' , 'o']
bar = ['b', 'a']
foo.append('0') # append() добавляет значение в конец списка
bar.insert(2, 'r') # insert() добавляет значение по индексу со смещением
print(foo, 'append() добавляет значение в конец списка')
print(bar, 'insert() добавляет значение по индексу со смещением')

# (159) Задание 11. Два способа удаления значений из списков
foo.remove('0') # удаление по значению
del bar[2] # удаление по индексу
print(foo)  # ['f' , 'o']
print(bar)  # ['b', 'a']

# (159) Задания 14, 15. 
# 14. Как записать кортеж, содержащий единственное целочисленное значение 42? 
# 15. Как преобразовать список в кортеж? Как преобразовать кортеж в список?
foo = (42,) # кортеж с единственным целочисленным значением
bar = [42] # список
print('Type foo: ', type(foo)) # <class 'tuple'>
print('Type bar: ', type(bar)) # <class 'list'>

print('\nПреобразование списка в кортеж и кортеж в список')
print('Type foo: ', type(list(foo))) # <class 'list'>
print('Type bar: ', type(tuple(bar))) # <class 'tuple'>
# '''

''' 💀 [.TROUBLE] Орёл и решка
import random

customerInput = int(input('Сколько раз подбрасываем? \n'))
outputList = []
countObverse = 0
countReverse = 0

for i in range(customerInput):
    if random.randint(0, 1) == 0:
        outputList.append('P')
        countReverse += 1
    else:
        outputList.append('O')
        countObverse += 1
    i += 1

print('Орлов выпало: ', countObverse, '\n''Решек выпало: ', countReverse)
# print(outputList)
# '''

''' [ATBF_164] Словари
myCatDict = {'size': 'fat',
             'color': 'gray',
             'disposition': 'loud'
             }
print(myCatDict['size'])

numTestDict = {12345: 'PassOne', 42: 'Answer'}
print(numTestDict[42])

# сравнение словарей
print(myCatDict == numTestDict)  # False

eggs = {
    'name': 'Sophie',
    'species': 'cat',
    'age': '8'}

ham = {
    'species': 'cat',
    'age': '8',
    'name': 'Sophie'}
print(eggs == ham)  # True
print(ham['name']) # Sofie
# '''

''' [ATBF_165] Словарь "Дни рождения"
birthdays = {
    'Alice' : 'Apr 1',
    'Bob'   : 'Dec 12',
    'Carol' : 'Mar 4',
    'Macy'  : 'Sep 17',
}

while True:
    print("Enter name (<Enter> for exit): ")
    input_name = input().capitalize()
    if input_name == '':
        break
    
    if input_name in birthdays:
        print(input_name + ' is the birthday of ' + birthdays[input_name], '\n')
    else:
        print('I do not have birthday information for ' + input_name)
        print('What is their birthday?')
        bday = input()
        birthdays[input_name] = bday
        print('Birthday db updated')
# '''

''' [ATBF_166] Методы keys(), values(), items()
birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4',
    'Macy': 'Sep 17',
    # 'Alice': 'Alice' # срока для разовых проверок значений
}

# for v in birthdays.keys():
#     print('Вывод dict_keys:', v)
# for v in birthdays.values():
#     print('Вывод dict_values', v)
# for v in birthdays.items():
#     print('Вывод dict_items', v)

# # проверим классы
# checkForKeys = birthdays.keys()
# checkForValues = birthdays.values()
# checkForItems = birthdays.items()
# print() # отделим вывод новой строкой для комфорта
# print(type(checkForKeys))   # <class 'dict_keys'>
# print(checkForKeys, '\n')  
# print(type(checkForValues)) # <class 'dict_values'>
# print(checkForValues, '\n')
# print(type(checkForItems))  # <class 'dict_items'>
# print(checkForItems, '\n')

# # преобразование словаря в list и tuple
# transferList = list(checkForItems)
# transferTuple = tuple(checkForItems)
# print('Проверим тип у list(dict): ', type(transferList))
# print('Посмотрим содержимое: ', transferList, '\n') # кортеж в списке

# print('Проверим тип у tuple(dict): ', type(transferTuple)) 
# print('Посмотрим содержимое: ', transferTuple, '\n')  # кортеж в кортеже

# преобразование в список с помощью методов
list_keys_bday = list(birthdays.keys())   # list
list_values_bday = list(birthdays.values()) # list
list_items_bday = list(birthdays.items())  # tuple in list

# # "конвертируем" в список
# print(list_keys_bday) # names
# print(list_values_bday) # birthday date
# print(list_items_bday) # tuple in list with names and date

# посмотрим на вывод при запросе ключа у разных методов
print("Check 'Alice' in list_keys_bday:", 'Alice' in list_keys_bday)    
# True, есть ключ 'Alice'
print("Check 'Alice' in list_values_bday:", 'Alice' in list_values_bday)  
# False, нет значения 'Alice'
print("Check 'Alice' in list_items_bday:", 'Alice' in list_items_bday)   
# False, тк это список с кортежем, нужно указать, где ищем
print("Check 'Alice' in list_items_bday with [0]:", 'Alice' in list_items_bday[0]) 
# True
# 
# спросим без методов, есть ли 'Alice' в словаре
print("Check 'Alice' in birthdays:", 'Alice' in birthdays)  
# True, есть ключ 'Alice' в словаре
# '''

''' [ATBF_169] Метод get()
picnitItems = {'apple' : 5, 'cup' : 2}
print('Я несу', str(picnitItems.get('cup', 0)), 'чашки')
print('Я несу', str(picnitItems.get('egg', 0)), 'яйца')
# '''

''' [ATBF_169] Метод setdefault()
spam = {
    'name' : 'Piter',
    'age' : 5,
    }
# добавим новый элемент 'color':'black'
if 'color' not in spam:
    spam['color'] = 'black'
# добавим новый элемент 'food':'broccoli'
spam.setdefault('food', 'broccoli')
# заменим 'food':'broccoli' на 'food':'burger'
spam.setdefault('food', 'burger') 
# 🥦 Петя не будет жмякать бургер, потому что ключ 'food' занят брокколяшками
print(spam)
# '''

''' [ATBF_170] character count
import pprint
message = 'it was a bright cold day in April, and the clock were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)
# pprint.pprint(count)
print(pprint.pformat(count))
# '''

''' [ATBF_174] Крестики-Нолики

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
            }
# print(theBoard.items['top-L']) # проверка словаря

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Кому ходить ' + turn + '. Куда класть?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
# '''


''' Памятка по спискам
# {Training}

# пустой список
L = []

# четыре элемента: индексы 0..3
L = [123, 'abc', 1.23, {}]

# вложенные подсписки
L = ['Alice', 40.0, ['dev', 'murloc']]

# список элементов интерируемого объекта
L = list('spam')

# список сгенерированных последовательных целых чисел
L = list(range(-4, 4))

# индекс
L[i]
# индекс индекса
L[i][j]
# индекс среза
L[i:j]
# длина списка
len(L)

# конкатенация
L1 + L2
# повторение / репликация
L1 * L2

# итерация
for x in L: print(x)
# членство
3 in L

# методы: увеличение
L.append(4)         # в конец списка
L.insert(i, X)      # произвольная вставка
L.extend([5,6,7])   # объединение списков

#  методы: поиск
L.index(X)
L.count(X)

# методы:
L.sort()    # пересобирает список по правилам
L.reverse() # возвращает список в обратной последовательности
L.clear()   # очищает список до []

# методы: уменьшение
L.pop(i)
L.remove(X)
del L[i]
del L[i:j]
L[i:j] = []

# присваивание
L.[i] = 3 # по индексу
L[i:j] = [4,5,6] # по срезу

# списковые включения и отображения
L = [X**2 for x in range(5)]
list(map(ord, spam))
# '''


''' [ATBF_179] Вложенные словари и списки
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}
            }
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')

print(f" - Apples         {totalBrought(allGuests, 'apples')}")
print(f" - cups           {totalBrought(allGuests, 'cups')}")
print(f" - cakes          {totalBrought(allGuests, 'cakes')}")
print(f" - ham sandwiches {totalBrought(allGuests, 'ham sandwiches')}")
print(f" - apple pies     {totalBrought(allGuests, 'apple pies')}")
# '''

''' [ATBF_186] СТРОКИ / STRINGS
# методы upper(), lower(), isupper(), and islower() Methods
foo = 'foo'
bar = 'monkeyball'
fooList = ['Foo', 'Fighters']
song = 'The Pretender, Everlong, My Hero'

print('\n методы upper(), lower(), isupper(), and islower():')
print(' --------------------------------------------------')
# вывод заглавными/прописными буквами
print(f' {foo.upper()}  | foo.upper())')

# вывод строчными буквами
print(f' {foo.lower()}  | foo.lower())')

# проверка есть ли строчные буквы в строке
print(f' {foo.islower()} | foo.islower())')

# проверка есть ли прописные буквы в строке
print(f' {foo.isupper()}| foo.isupper())')

# изменение регистра и проверка есть ли строчные буквы в строке
print(f' {foo.upper().isupper()} | foo.upper().isupper()')

# методы startswith() и endswith()
print('\n startswith() и endswith() for \'monkeyball\':')
print(' -------------------------------------------')
print(f' {bar.startswith("mon")}  | bar.STARTswith("mon")')  # True
print(f' {bar.startswith("ball")} | bar.STARTswith("ball")') # False
print(f' {bar.endswith("mon")} | bar.ENDswith("mon")')       # False
print(f' {bar.endswith("ball")}  | bar.ENDswith("ball")')    # True

# методы join() и split()

print('\n метод join():')
print(' -------------')
# ВАЖНО! Cтрока, для которой вызывается метод join(arg),
# вставляется между элементами списка

print(f" {' '.join(fooList)} | ' '.join(fooList)") # Foo Fighters
print(f" {'•'.join(fooList)} | '•'.join(fooList)") # Foo•Fighters

# метод split() вызывается для строки с последующим созданием списка из неё
print('\n метод split():')
print(' --------------')
# обычный вывод
print(f' print(song)        | The Pretender, Everlong, My Hero')

# вывод с split()
print(f' song.split()       | {song.split()}')
# по умолчанию строка разбивается в тех местах, 
# где встречаются пробельные символы: 
# пробел ' ', табуляция '\t', новая строка '\n'
# но можно передать в качестве аргумента и другие значения
print(f' song.split("e")    | {song.split("e")}')
# ['Th', ' Pr', 't', 'nd', 'r, Ev', 'rlong, My H', 'ro']

# проверим тип данных для song
print(f' type(song)         | {type(song)}')

# проверим тип данных для song.split()
print(f' type(song.split()) | {type(song.split())}')

# Разбиение строк с помощью метода partition()
# метод разбивает строку на кортеж
# ДО разделителя, РАЗДЕЛИТЕЛЬ, после разделителя
print('\n метод partition():')
print(' -----------------')

print(f' song.partition("Pretender") | {song.partition("Pretender")}')
# ('The ', 'Pretender', ', Everlong, My Hero')

# если аргумент встречается несколько раз,
# то метод разбивает строку только на первом разделителе
print(f' song.partition("e")         | {song.partition("e")}')
# ('Th', 'e', ' Pretender, Everlong, My Hero')

# если аргумент не встречается ни разу, то создаётся кортеж ('string', '', '')
print(f' song.partition("q")         | {song.partition("q")}')
('The Pretender, Everlong, My Hero', '', '')

# методы rjust(), ljust(), center()
print('\n методы r/ljust(), center():')
print(' --------------------------')
print(f' len(song) == {len(song)}')
print(f' song.rjust(52)  + len()  | {song.rjust(52)} : len({len(song.rjust(52))})')
print(f' song.rjust(42)  + len()  | {song.rjust(42)} : len({len(song.rjust(42))})')
print(f' song.rjust(20)  + len()  | {song.rjust(20)} : len({len(song.rjust(20))})')
print(f' song.center(70, ".")     | {song.center(70, ".")}')

# метод strip() с аргументом
# метод strip() чувствителен к регистру
spam = 'pythpythpythc++pythpy'

print('\n метод strip() с параметром:')
print(' --------------------------')

print(f' spam.strip("ypht") | {spam.strip("ypht")}')
# '''


''' Picnic Table
def printPicnic(itemDict, leftWidth, rightWidth):
    print('PICNIC YAMMY'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches' : 4, 
                'apples'    : 12, 
                'cups'      : 4, 
                'cookies'   : 9000}

printPicnic(picnicItems, 16, 5)
# '''


''' ord() и chr()
# ord() переводит символ в код Unicode
print('\v перевод символов Unicode \n в кодовое представление:')
print(' ------------------------')

print(f" ord('A') | {ord('A')}") # 65
print(f" ord('4') | {ord('4')}") # 52 
print(f" ord('N') | {ord('N')}") # 78

# ord() переводит код Unicode в символ
print(f" chr(65)  | {chr(65)}") # 'A'
print(f" chr(52)  | {chr(52)}") # '4'
print(f" chr(49)  | {chr(49)}") # '1' 

print(f"\v ord('A') < ord('B') | {ord('A') < ord('B')}")
print(f" ord('A') == chr(65) | {ord('A') == ord(chr(65))}")
print(f" chr(ord('A'))       | {chr(ord('A'))}")
print(f" chr(ord('A') + 1)   | {chr(ord('A') + 1)}")
print(f" chr(ord('A') * 5)   | {chr(ord('A') * 5)}")
# умножая код 65(A) * 5 получаем 325(Ņ)
# '''

''' 🐷 PIG LATIN Translate engine 🚒
# создадим константу и кортеж с гласными буквами
VOWELS = ('а', 'е', 'i', 'o', 'u', 'у')

# запросим слово у пользователя
# message = input('Enter word: ')
message = "My name is Frank Bosses" # вместо регулярного ввода

# список слов на 🐷 латыни
pigLatin = [] 

# основной цикл программы

for word in message.split(): # разделим строку на список

    # процесс отделения небуквенных символов в начале слова
    prefixNonLetters = '' # строка для небуквенных символов в начале
    
    while len(word) == 0 and word[0].isalpha():
        # метод .isalpha() - проверка на небуквенные символы
        prefixNonLetters += word[0]
        word += word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
        

    # отделяем небуквенные символы в конце слова
    suffixNonLetter = '' # объект для небуквенных символов в конце
    while not word[-1].isalpha:
    # цикл while выполняется пока в строке имеются небуквенные символы
        suffixNonLetter += word[-1]
        word = word[:-1]
        # найденные символы записываются в конец списка word
    
    # запоминаем регист слова
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # перевод в нижний регистр

    # отделяем согласные в начале слова
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    
    # добавляем финальный слог
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    # возвращаем исходный регистр
    # 👻 пока что не работает
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # возвращаем небуквенные символы
    pigLatin.append(prefixNonLetters + word + suffixNonLetter)

# соединяем слова обратно в строку

print('\v', ' '.join(pigLatin))
# '''

''' 💀 [.TROUBLE][ATBF_214] The Table

# '''

# # ГЛАВА 7. RegEx

''' [ATBF_223] Поиск телефонного номера
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print(isPhoneNumber('415-666-1313'))

message = 'Call•me•back•at•number•415-666-1313•\
           or•999-666-1313,•415-666-131A'

for i in range(len(message)):
    chunk = message[i:i+12]
    if len(chunk) != 12:
        break
    # print(f'iteration #{i}: {chunk}')
    if isPhoneNumber(chunk):
        print(f'\viteration #{i}: {chunk}\n')
print('Done')
#'''

''' [ATBF_225] Поиск номера с помощью RegEx
import re

message = 'Call•me•back•at•number•415-666-1313•\
           or•999-666-1313,•(415)-666-1314'

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# # phoneNumRegexGroup = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# phoneNumRegexGroup = re.compile(r'(\d+)-(\d+)-(\d+)')
# phoneNumRegexBack = re.compile(r'(\(\d+\)-\d+.\d+)')

# moOne = phoneNumRegex.search(message)
# moTwo = phoneNumRegexGroup.search(message)
# moThree = phoneNumRegexBack.search(message)

# print(moOne.group())    # 415-666-1313
# print(moOne.group())    # 415-666-1313
# print(moTwo.group())    # 415-666-1313
# print(moThree.group())  # (415)-666-131

# примитивные способы поиска с RE
phoneNumbers = '123-456-789\
                123456789\
                (000)-123-456-789\
                (000 123456789\
                000- 123456789\
                000123-456-789\
                (000) 123 456 789'

# 🤘 123-456-789
print(re.compile(r'(\d+.)*').search(phoneNumbers))

# 💀 123456789
# print(re.compile(r'\d+').search(phoneNumbers))

# 🤘 (000)-123-456-789
print(re.compile(r'(\(\d+\)).(\d+.)(\d+).(\d+)').search(phoneNumbers))
print(re.compile(r'(\(\d+\)).(\d+.)(\d+).(\d+)').findall(phoneNumbers))
# [('(000)', '123-', '456', '789'), ('(000)', '123 ', '456', '789')]

# 💀 (000 123456789
# print(re.compile(r'(\(\d+).(\d+)').search(phoneNumbers))

# 💀 000 - 123456789
# print(re.compile(r'(\d+)[.]*(\d+)').search(phoneNumbers))

# 💀 000123-456-789
# print(re.compile(r'(\d+).(\d+).(\d+)').search(phoneNumbers))

# 💀 (000) 123 456 789
# print(re.compile(r'(\(\d+\).(\d+).(\d+))').search(phoneNumbers))

phoneRE = re.compile(r'\d+')
phoneRELong = re.compile(r'(\d+).(\d+).(\d+).(\d+)')
tmpOutputPhone = phoneRELong.search(phoneNumbers)
# в phoneRE{Long} лежит ссылка на объект, созданный с помощью re.compile(), 
# которому передана необработанная строка поискового шаблона 

print(f'\vDEBUG OUTPUT: {tmpOutputPhone}\n')

print(phoneRE.search(phoneNumbers)) # 123
print((re.compile(r'\d+')).search(phoneNumbers)) # 123
print(f'вывод с f-string: {phoneRE.search(phoneNumbers)}')
# выдаст 123, так как '123-456-789' - первое совпадение
print(f'вывод с f-string: {phoneRE.search(phoneNumbers)}')
# <class 're.Match'>
print(f're.search(var).group(): {(phoneRELong).search(phoneNumbers).group()}')
# group() - выберет все группы, group(2) - только вторую (456)
print(f're.search(var).group(2): {(phoneRELong).search(phoneNumbers).group(2)}')
# вывод группировкой, <class 'str'>
print(f're.search(var).groups: {(phoneRELong).search(phoneNumbers).groups()}')
# вывод группировкой, <class 'tuple' >
# '''


'''
dcVallians = 'Joker, Mr. Freeze, Deathstroke, Bane, Catwoman, Scarecrow'
dcHero = 'Superman, Batman, Wonder Woman, The Flash, Green Lantern, Aquaman'
batmanGadget = 'Batpad, Batmobile, Batphone, Batarang, Batclaw'

# ищем злыдней в dcVallians
dcValliansFinder = re.compile(r'Catwoman|Deathstroke')
# re.compile(r'Deathstroke|Catwoman') найдёт только первое совпадение в строке

# действия ниже:
# для объекта RE в dcValliansFinder применяется метод search()
# которому передаётся объект со строкой в dcVallians
# если что-то будет найдено, то вернётся объект Match
print(dcValliansFinder.search(dcVallians))
print(re.compile(r'Catwoman|Deathstroke').search(dcVallians))
# <re.Match object; span=(19, 30), match='Deathstroke'>
# для объекта Match имеется метод group(), который возвращает
# содержимое match
print(f'{dcValliansFinder.search(dcVallians).group()}')
# Deathstroke
print(re.compile(r'Catwoman|Deathstroke').findall(dcVallians))
# ['Deathstroke', 'Catwoman']

# # (не)жадный поиск
# print('\v')
trainStr = 'ha@ha-ha,ha&ha'
trainRE = re.compile(r'(ha.)*')  # ha@ha-ha,ha&
trainRE = re.compile(r'(ha(.)?)+')  # ha@ha-ha,ha&ha
trainRE = re.compile(r'(ha(.)?){1,}')  # ha@ha-ha,ha&ha
trainRE = re.compile(r'(ha(.)?){1,}?')  # ha@ пример нежадного поиска
training = trainRE.search(trainStr).group()

print('+---RegEx-----+---- Result ---+')
print("(ha.)*        |", re.compile(r'(ha.)*').search(trainStr).group())
print("(ha(.)?)+     |", re.compile(r'(ha(.)?)+').search(trainStr).group())
print("(ha(.)?){1,}  |", re.compile(r'(ha(.)?){1,}').search(trainStr).group())
print("(ha(.)?){1,}? |", re.compile(r'(ha(.)?){1,}?').search(trainStr).group())
print('+-------------+---------------+')

# пример работы символьных классов
xmasNeeds = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, \
            7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, \
            1 partridge'
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(xmasNeeds))
# '''

''' [ATBF_236] Создание создание собственных символьных классов
vowelRegex = re.compile(r'[aeiouAEIOU.]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', '.', 'A', 'O', 'O']

vowelRegex = re.compile(r'[^aeiouAEIOU.]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', ' ', 'B', 'B', 'Y', ' ', 'F', 'D']
# '''

# ''' [ATBF_236] Символы caret/circumflex(^) и dollor($)
beginsWithHello = re.compile(r'Hello')
print(beginsWithHello.search('Hello, World!'))
# <re.Match object; span=(0, 5), match='Hello'>
print(beginsWithHello.search('He said hello') == None)
# True

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Guide to the Number 42'))
# <re.Match object; span=(21, 22), match='2'>

endsWithNumber = re.compile(r'\d+$') # добавим (+) для жадности 😈
print(endsWithNumber.search('Guide to the Number 42'))
# <re.Match object; span=(20, 22), match='42'>

print(endsWithNumber.search('Guide to the Number forty-two') == None)
# True

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
# <re.Match object; span=(0, 10), match='1234567890'>

print(wholeStringIsNum.search('1234xyz567890') == None)
# True

print(wholeStringIsNum.search('123 456 7890') == None)
# True

# '''
# '''



''' памятка по синтаксису RE
.       =>  любой символ, кроме '\n'
^       =>  начало строки
$       =>  конец строки
*       =>  повторение RE, от 0 до бесконечности
+       =>  повторение RE, от 1 до бесконечности
?* ?+   =>  нежадные версии ( * ) и ( + ) 
?       =>  предшествующая знаку группа встречается не более 1 раза
{...}   =>  повторение RE от m до n раз: (RE){m, n}
[...]   =>  любой символ из набора в []: [a..zA..z]
[^...]  =>  любой символ НЕ из набора в []: [a..zA..z]
(...)   =>  выделение группы: (\d+\w+)
\       =>  экранирование
|       =>  логическое ИЛИ - вернёт первое соответствие
\7      =>    
\A      =>    
\b      =>    
\B      =>    
\d      =>    
\D      =>    
\s      =>    
\S      =>    
\w      =>    
\W      =>    
\Z      =>    
\\      =>  
#'''