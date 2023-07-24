# Задание 1  Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
#    “Don't compare yourself with anyone in this world…
#     if you do so, you are insulting yourself.”
#     Bill Gates

def show_text():
  print("\"Don't compare yourself with anyone in this world… \nif you do so, you are insulting yourself.\" \n Bill Gates")


print(show_text())

# Задание 2 Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа
# между ними.

def find_range(a, b):
    return [i for i in range(a+1, b) if i % 2 == 0]


print(find_range(10, 20))


# Задание 3 Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.
def construct_square(length, symbol, boolean):
    x = length * symbol
    if boolean == True:
        for i in range(length):
            print(x)
    else:
        print(x)
        for i in range(length - 2):
            print(symbol + " " * (length - 2) + symbol)
        print(x)


print(construct_square(7, "*", False))


# Задание 4 Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.

def min_number(*args):
    return min(args)


print(min_number(10, 20, 30, 40, 50))

# Задание 5 Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.

def multiply_numbers(a, b):
     if a == b:
      print("Error")
     if a > b:
         a, b = b, a
     m = 1
     for i in range(a, b+1):
           m *= i
     return m


print(multiply_numbers(20, 10))

# Задание 6 Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.

def count_numbers(a):
    return(len(str(a)))


print(count_numbers(85325))

# Задание 7 Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра.
# Если число палиндром нужно вернуть из функции true, иначе false. «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например, 123321 — палиндром (первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром, а 421987 — не палиндром.

def find_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


print(find_palindrome(345543))