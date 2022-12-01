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


# [ATBF_120] ZigZag
import time, sys

indent = 0                  # кол-во пробелов для отступа
indentIncreasing = True     # квеличение или умемьшение отступа

try:
    while True: # основной цикл
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # выставляем паузу в 0.1s (1/10)

        if indentIncreasing:
            indent += 1
            if indent == 10:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()


