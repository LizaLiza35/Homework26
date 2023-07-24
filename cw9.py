studBirthYear = [1997, 2003, 2000, 1999]

studAges = []
for year in studBirthYear:
    studAges.append(2023 - year)
print(studAges)

studAges = list(map(lambda x: 2023 - x, studBirthYear))
print(studAges)

print(abs(13))

myNumbers = [2, 6, 4 -5, 0]
print(myNumbers)
print(sorted(myNumbers))

def nameUpper(name):
    return "user" + name.upper()

def nameLower(name):
    return "user" + name.lower()

def makeLog(userName, maker):
    return maker(userName)

print(makeLog("Alex", nameUpper))

userLogs = ['123user', 'USER234', 'qwerty']
userLoginLow = list(map(str.lower, userLogs))
print(userLoginLow)

myValues = ['231', '345', '56']
resNum = list(map(float, myValues))
print(resNum)

myDigits = list(map(lambda x: int(x[0]), myValues))
print(myDigits)

pizzaTypes = ["Paperoni", "Four Season", "Four Cheese"]
def modifyPizzaTypes(pizzaType):
    return pizzaType + " pizza"

pizzanames = list(map(modifyPizzaTypes, pizzaTypes))
print(pizzanames)

nums = [1, 2, 3]
stepNums = [1, 2, 3]
res = list(map(lambda a, b: a ** b, nums, stepNums))
print(res)


prices = [100, 300, 600, 1000]
expensive = list(filter(lambda x: x > 500, prices))
print(expensive)

def checkLog(user):
    if user.lower().find('user') != -1:
        return True
    else:
        return False

checkedUser = list(filter(checkLog, userLogs))
print(checkedUser)

# zip ------------

userPass = ['1111', 'qwerty', 'vsfvdfv']

for log, passw in zip(userLogs, userPass):
    print(f"login: {log}, pass: {passw}")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1,list2)))
print(type(zip(list1, list2)))

from functools import reduce

nums = [1, 2, 3, 4, 5]

def mySum(x, y):
    return x + y

res1 = reduce(mySum, nums, 0)
print(res1)
res2 = reduce(lambda x, y: x + y, nums, 0)
print(res2)

words = ['python', 'js', 'c++']
sentence = reduce(lambda x, y: x + y if x == "" else x + " " + y , words, "")
print(sentence)

# 1. Используя функцию map, создайте новый список, в котором каждый элемент будет возводиться в квадрат.Исходный список:
# [1, 2, 3, 4, 5].

list1 = [1, 2, 3, 4, 5]
list2 = list(map(lambda x: x ** 2, list1))
print(list2)

# 2. Используя функцию map, преобразуйте список строк в список их длин. Исходный список: ["apple", "banana", "cherry"].

list3 = ["apple", "banana", "cherry"]
list4 = list(map(lambda x: len(x), list3))
print(list4)

# 3. Используя функцию filter, отфильтруйте список чисел, оставив только четные числа. Исходный список: [1, 2, 3, 4, 5].

list5 = [1, 2, 3, 4, 5]
list6 = list(filter(lambda x: x % 2 == 0, list5))
print(list6)

# 4. Используя функцию filter, отфильтруйте список строк, оставив только строки, начинающиеся с буквы "a".
# Исходный список: ["apple", "banana", "cherry"].

list7 = ["apple", "banana", "cherry"]
list8 = list(filter(lambda x: x[0] == 'a', list7))
print(list8)

# 5. Используя функции map и filter, создайте новый список, в котор останутся только числа, делящиеся на 3.
# Исходный список: [1, 2, 3, 4, 5].

list9 = [1, 2, 3, 4, 5]
list10 = list(filter(lambda x: x % 3 == 0, list9))
print(list10)

# 6. Используя функцию zip, объедините два списка чисел в список пар чисел. Исходные списки: [1, 2, 3] и [4, 5, 6].

list11 = [1, 2, 3]
list12 = [4, 5, 6]
print(list(zip(list11, list12)))

# 7. Используя функцию map, преобразуйте два списка чисел в список их произведений.
# Исходные списки: [1, 2, 3] и [4, 5, 6].

list13 = [1, 2, 3]
list14 = [4, 5, 6]
list15 = list(map(lambda x, y: x * y, list13, list14))
print(list15)

# # 8. Используя функцию filter, отфильтруйте список пар чисел, оставив только пары, в которых первое число больше второго.
# # Исходный список: [(1,2), (3, 1), (4, 4), (5, 3)].
#
# list16 = [(1,2), (3, 1), (4, 4), (5, 3)]
# list17 = list(filter(lambda x: if x[0] > x[1], list16))
# print(list17)


# 9 Напишите программу, которая берет список чисел и возвращает произведение их используя функцию reduce.

from functools import reduce
list18 = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x * y, list18)
print(res)


