# Задание 1
# Есть некоторый текст. Реализуйте следующую функциональность:
# 1.Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# 2.Посчитайте сколько раз цифры встречаются в тексте;
# 3.Посчитайте сколько раз знаки препинания встречаются в тексте;
# 4.Посчитайте количество восклицательных знаков в тексте.

import string
text = input("Enter the text: ")
numbers = sum(i.isdigit() for i in text)
print(numbers)
punctuation = sum(i in string.punctuation for i in text)
print(punctuation)
print(text.count("!"))


# Задание 2
# Пользователь с клавиатуры вводит элементы списка целых и некоторое число. Необходимо посчитать сколько раз
# данное число присутствует в списке. Результат вывести на экран.

list1 = input("Enter some numbers: ").split()
number = int(input("Enter the number from the first list: "))
count = 0
for number in list1:
   count = list1.count(number)
print(count)

# Задание 3
# Пользователь с клавиатуры вводит элементы списка целых. Необходимо посчитать сумму всех элементов
# и их среднеарифметическое. Результаты вывести на экран.

list2 = list(map(int, input("Enter some numbers: ").split()))
print(sum(list2))
print(sum(list2) / len(list2))

# Задание 4
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
# 1 Создать список целых, содержащий только четные числа из первого списка;
# 2 Создать список целых, содержащий только нечетные числа из первого списка;
# 3 Создать список целых, содержащий только отрицательные числа из первого списка;
# 4 Создать список целых, содержащий только положительные числа из первого списка.

import random
nums = []
for i in range(10):
    nums.append(random.randint(-100, 100))
print(nums)
even = [i for i in nums if not i % 2]
print("Even numbers:", even)
odd = [i for i in nums if i % 2]
print("Odd numbers:", odd)
negative = [i for i in nums if i < 0]
print("Negative numbers:", negative)
positive = [i for i in nums if i > 0]
print("Positive numbers:", positive)

