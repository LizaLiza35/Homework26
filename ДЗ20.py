# Задание 1
# Дан список чисел, отфильтровать только положительные

list1 = [-20, 2, 84, -5, 5, 8.3, 0, 10.7, -12, 23]

new_list1 = list(filter(lambda x: x > 0, list1))
print(new_list1)
#
# Задание 2
# Дан список чисел, отфильтровать числа в диапазоне указанным пользователем.

first_number = int(input("Enter the beginning of the range: "))
second_number = int(input("Enter the end of the range: "))
user_list = list(filter(lambda x: x > first_number and x < second_number, list1))
print(user_list)

# Задание 3
# Дан список чисел, отфильтровать все целочисленные значения

new_list3 = list(filter(lambda x: type(x) is int, list1))
print(new_list3)

# Задание 4
# Дан список логинов пользователей, добавьте каждому логину приставку "$"

logins = ["Nick83", "Angel835", "Mike_233"]
new_logins = list(map(lambda x: "$" + x, logins))
print(new_logins)

# Задание 5
# На основе трех списков разных значений, сформировать список,
# элемент которого содержит набор из элементов других списков.

product = ["jam", "water", "milk"]
package = ["jar", "bottle", "carton"]
number = [80, 35, 68]
store = list(zip(product, package, number))
print(store)

# Задание 6
# Напишите программу, которая принимает список целых чисел и возвращает список строк, представляющих эти числа.

change_number = list(map(str, number))
print(change_number)

