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


# [ATBF_94] Игра RPC Game
import random, sys

print('КАМЕНЬ, НОЖНИЦЫ, БУМАГА')

wins = 0    # переменная для победы 
losses = 0  # переменная для поражения
ties = 0    # переменная для ничьих

    # Главный цикл игры
while True:
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    
    # Цикл выбора хода 
    while True:
        print('Выбери ход: (к)амень, (н)ожницы, (б)умага или ' + \
                '(в)ыход')
        playerMove = input()
        if playerMove == 'в':
            sys.exit() # выход из программы
        if playerMove == 'к' \
        or playerMove == 'н' \
        or playerMove == 'б':
            break # выход из цикла ввода
        print('Введи "к", "н", "б", "в"')
    
    # Отображение выбора пользователя 
    if playerMove == 'к':
        print('Камень и ...')
    if playerMove == 'н':
        print('Ножницы и ...')
    if playerMove == 'б':
        print('Бумага и ...')

    # Отображение выбора системы
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'к'
        print('🗿 КАМЕНЬ')
    if randomNumber == 2:
        computerMove = 'н'
        print('✂️ НОЖНИЦЫ')
    if randomNumber == 3:
        computerMove = 'б'
        print('🧻 БУМАГА')
    
    # Отображение и учёт результатов
    if playerMove == computerMove:
        print('Ничья!')
        ties = ties + 1
    elif playerMove == 'к' and computerMove == 'н':
        print('Вы выиграли')
        wins = wins + 1
    elif playerMove == 'б' and computerMove == 'к':
        print('Вы выиграли')
        wins = wins + 1
    elif playerMove == 'н' and computerMove == 'б':
        print('Вы выиграли')
        wins = wins + 1
    elif playerMove == 'к' and computerMove == 'б':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'б' and computerMove == 'н':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'н' and computerMove == 'к':
        print('Вы проиграли!')
        losses = losses + 1

        
        
