# Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте, является ли введенная строка палиндромом.
# Палиндром — слово или текст, которое читается одинаково слева направо и справа налево.
# Например, кок; А роза упала на лапу Азора; доход; А буду я у дуба.
import string

str1 = input("Enter the word or sentence: ")
if str1 != str1[::-1]:
    print("It is not a palindrome")
else:
    print("It is a palindrome")

# Задание 2
# Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

try:
    str2 = input("Enter the text: ")
    words = input("Enter the words with a comma: ").split(",")
    for i in words:
        if i in str2:
            str2 = str2.replace(i, i.upper())
        else:
            raise Exception
    print(str2)
except Exception:
        print("You should enter words from the text")

# Задание 3
# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.

try:
    str3 = input("Enter the text: ")
    print(str3.count('.') + str3.count('!') + str3.count('?'))
    if str3 == "":
        raise Exception
except Exception:
    print("You did not enter the text")
