myStr = "python was created in the late 1980's by Guido van Rossum. was"
# print(myStr)
# print(myStr[0])
# print(myStr[-1])
# print(len(myStr))
# print("length - ", len(myStr))
# print(myStr[len(myStr) - 1])
#
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.capitalize())
# print(myStr.title())
# print(myStr.swapcase())
# myStr = myStr.upper()
# print(myStr)
#
# print(myStr.find('WAS'))
# print(myStr.lower().find('was'))
# print(myStr.lower().rfind('was'))
# print(myStr.lower().index('was'))
# print(myStr.lower().rindex('was'))
# print(myStr.join(" | "))
# print(myStr.split(" "))
print(myStr.replace("late".upper(), "early"))
# print(myStr.lower().count("was"))
# print("PYTHON".center(10, "-"))
# print("    PYTHON".strip().center(10, "-"))
#
# str1 = "123"
# print(str1.isdigit())
#
# countDigit = 0
# countUpper = 0
# countLower = 0
# pathword = input("enter path = ")
# i = 0
# while i < len(pathword):
#     if pathword[i].isdigit():
#         countDigit += 1
#     elif pathword[i].islower():
#         countLower += 1
#     elif pathword[i].isupper():
#         countUpper += 1
#     i += 1
# if countLower == 0 or countUpper == 0 or countDigit == 0 or len(pathword) <8:
#     print("weak pathword! ")
# else:
#     print("Path ok\\")
#
# str3 = "huhihihihihihihihih \
# bhbjbjjhg"
#
# print(myStr[0:2:1])

# import string
# import random
#
# s = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
# password = ""
# print(s)
#
# i = 0
# while i < 8:
#     password += random.choice(s)
#     i += 1
# print(f"New password: {password}")


# Задание 1 Пользователь вводит с клавиатуры строку. Произведите поворот строк и полученный результат выведите на экран.
# str1 = input("Enter: ")
# print(str1[::-1])

# Задание 2 Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке.
# Выведите оба количества на экран.

str2 = "Привет 12 25 7"
countDigit = 0
countAlpha = 0
i = 0
while i < len(str2):
    if str2[i].isdigit():
        countDigit += 1
    elif str2[i].isalpha():
        countAlpha += 1
    i += 1
print(countDigit)
print(countAlpha)

# Задание 3 Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке встречается
# искомый символ.  Полученное число выведите на экран.

# str2 = input("Enter: ")
# sign = "n"
# print(str2.find('n'))
#
#

