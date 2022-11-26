#Python 3.11
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


#  (52) "Ваша первая программа"
print('Hello World!\n')
# 
print('What is your name?')
myName = input()
print('Nice to meet you, ' + myName, '\n')
print('The length your name is: ')
print(len(myName), ' letters', '\n')
# 
print('How old are you?')
myAge = input()
print('In a year you will be ' + str(int(myAge) + 1) + ' old', '\n')
