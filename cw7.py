# def sayHello():
#     print("Hello!")
# print("before func")
# sayHello()
# print("after func")
#
# def sayHello2(name):
#     print(f"Hello, {name}")
# sayHello2("Bill")
#
# def sumNums(a,b,c=0):
#     print(a + b + c)
#
#
# sumNums(1, 2, 3)
#
# def sunNums2(*args):
#     print(*args)
#     sum = 0
#     for elem in args:
#         sum +=elem
#     print("sum = ", sum)
# sunNums2(1, 2, 3, 4, 5, 6, 7)
#
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")
#
# show_info(name = "user1", age = 20, path = "qwerty")
#
# mas = [1, 2, 3, 4, 5]
#
# def show_mas(array):
#     for i in array:
#         print(i)
#
# show_mas(mas)
#
# def pow(a,b):
#     return a ** b
# print("2 ** 3 = ", pow(2, 3))
# res = pow(2, 3)
# print("res = ", res)
# global_num = 1
# def testGlobal():
#     global global_num
#     global_num = 5
#     print("global num ", global_num)
#     local_num = 2
#     print("local_num = ", local_num)
#
#
# testGlobal()
# print("global num = ", global_num)
#
# def outer_func():
#     print("outer func working")
#     number = 100
#     def inner_func():
#         nonlocal number
#         print("inner func working")
#         number = 200
#         print("number = ", number)
#         print("global num = ", global_num)
#     inner_func()
#     print("number = ", number)
# outer_func()

# 1 реализовать функции для поиска времени и растояния которое проехал автомобиль

def find_speed(distance, time):
    if time != 0:
      return distance // time
    else:
        return -1

print(find_speed(233, 2), "km/h")

def find_time(distance, speed):
    if speed != 0:
      return distance // speed
    else:
        return -1

print(find_time(233, 80), "h")

def find_distance(time, speed):
      return time * speed

print(find_distance(3, 80), "km")

# 1Написать функцию, которая возвращает истину, если передаваемое значение положительное и ложь, если отрицательное.

def check_number(number):
    if number > 0:
        return True
    elif number < 0:
        return False
print(check_number(3))


# 2.Написать функцию, определяющую минимум и максимум (значение и номер) элементов передаваемого ей массива.

import random
randNums = []
for i in range(10):
    randNums.append(random.randint(-100, 100))
print(randNums)

def define_min_max(randNums):
    return ("Min: ", min(randNums),"Max: ", max(randNums))
print (define_min_max(randNums))



# 3.Написать функцию, определяющую среднее арифметическое элементов передаваемого ей массива

def count_average(randNums):
    return (sum(randNums) / len(randNums))
print(count_average(randNums))


# 4.Написать функцию, меняющую порядок следования элементов передаваемого ей массива на противоположный.

def change_reverse(randNums):
    return randNums[::-1]
print(change_reverse(randNums))

# 5.Написать функцию, которая получает в качестве параметров 2 целых числа и возвращает сумму чисел из диапазона между ними.
