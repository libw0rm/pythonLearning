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


# [ATBF_86] fiveTimes
print("My name is")
for i in range(5):
    print("Jimmy Five Times (" + str(i) + ")") #Нумерация цикла с (0)
    # print("Jimmy Five Times (" + str(i+1) + ")") #Нумерация цикла с (1)

