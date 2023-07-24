# Задание 1
# Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.

try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(x ** y)
except ValueError:
    print("x and y must be an integer!")

# Задание 2
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.

try:
    user_number = int(input("Enter the number: "))
    del36 = 0
    i = 0
    if user_number <= 0:
        raise Exception
    while user_number > 0:
        del36 = user_number % 10
        user_number = user_number // 10
        if del36 % 10 != 3 and del36 % 10 != 6:
            user_number = user_number + del36 * i
            i *= 10
            print(del36)
except ValueError:
    print("The number must be an integer!")
except Exception:
    print("The number must not be equal to zero and be less than zero!")


# Задание 3 Пользователь вводит с клавиатуры целое шестизначное число. Написать программу, которая определяет,
# является ли введенное число — счастливым (Счастливым считается шестизначное число, у которого сумма первых 3 цифр
# равна сумме вторых трех цифр). Например, 123321 — счастливое число, так как 1+2+3 = 3+2+1.С другой стороны 378423
# несчастливое число, так как 3+7+8 != 4+2+3. Если пользователь ввел не шестизначное число требуется вывести
# сообщение об ошибке.
#
try:
    six_number = int(input("Enter the six-digit number: "))
    if six_number < 100000:
        raise Exception
    elif six_number >= 999999:
        raise Exception
    elif (int(six_number/100000) + (int(six_number / 10000) % 10) + (int(six_number / 1000) % 10)) == ((int(six_number / 100) % 10)
             + (int(six_number / 10) % 10) + (six_number % 10)):
        print("lucky")
    elif (int(six_number/100000) + (int(six_number / 10000) % 10) + (int(six_number / 1000) % 10)) != ((int(six_number / 100) % 10)
             + (int(six_number / 10) % 10) + (six_number % 10)):
        print("unlucky")
except ValueError:
        print("The number must be an integer!")
except Exception:
        print("The number must be six-digit!")

# Задание 4
# Пользователь вводит с клавиатуры номер месяца (от 1
# до 12). В зависимости от полученного номера месяца программа выводит на экран надпись: Winter (если введено
# значение 1,2 или 12), Spring (если введено значение от 3 до 5), Summer (если введено значение от 6 до 8), Autumn
# (если введено значение от 9 до 11).
# Если пользователь ввел значение не в диапазоне от 1 до 12 требуется вывести сообщение об ошибке.

try:
    month = int(input("Enter the number from 1 to 12: "))
    if month > 12 or month <= 0:
        raise Exception
    elif month == 1 or month == 2 or month == 12:
        print("Winter")
    elif month == 3 or month == 4 or month == 5:
        print("Spring")
    elif month == 6 or month == 7 or month == 8:
        print("Summer")
    elif month == 9 or month == 10 or month == 11:
        print("Autumn")
except ValueError:
        print("It must be a number! The number must be an integer!")
except Exception:
        print("The number must be from 1 to 12")

# Задание 5 Пользователь вводит с клавиатуры длину и ширину прямоугольника. Требуется отобразить на экран
# незаполненный прямоугольник (отображаются только границы прямоугольника). Размер длины и ширины равен введенным
# данным.

try:
        i = 0
        num1 = int(input("Enter width: "))
        num2 = int(input("Enter length: "))
        if num1 and num2 <= 0:
            raise Exception
        if num1 == num2:
            raise Exception
        while i < num1:
            if i == 0 or i == num1 - 1:
                print("*" * num2)
            else:
                print("*" + " " * (num2 - 2) + "*")
            i += 1
except ValueError:
    print("It is must be an integer")
except Exception:
    print("number error ")
