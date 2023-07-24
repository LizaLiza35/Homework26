# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать
# все числа в этом диапазоне по следующему правилу: если число кратно 7, его надо выводить на экран.

user_number1 = int(input("Enter the first number: "))
user_number2 = int(input("Enter the second number: "))
while user_number1 < user_number2:
    user_number1 += 1
    if user_number1 % 7 == 0:
        print(user_number1)

# Задание 2
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

user_num1 = int(input("Enter the first number: "))
user_num2 = int(input("Enter the second number: "))
count = 0
while user_num1 <= user_num2:
    print(user_num1)
    user_num1 += 1
while user_num2 >= user_num1:
    print(user_num2)
    user_num2 -= 1
while user_num1 <= user_num2:
    user_num1 += 1
    if user_num1 % 7 == 0:
        print(user_num1)
while user_num1 <= user_num2:
     user_num1 += 1
     if user_num1 % 5 == 0:
        count += 1
        print (count)

# Задание 3
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число

user_n1 = int(input("Enter the first number: "))
user_n2 = int(input("Enter the second number: "))
while user_n1 < user_n2:
    user_n1 += 1
    if user_n1 % 3 == 0 and user_n1 % 5 == 0:
        print("Fizz Buzz")
    elif user_n1 % 3 == 0:
        print("Fizz")
    elif user_n1 % 5 == 0:
        print("Buzz")
    else:
        print(user_n1)

# Задание 4
# Написать программу – конвертер валют. Реализовать общение с пользователем через меню.

choice = int(input("Enter the currency 1-USD to EUR; 2-USD to UAH; 3-EUR to USD; 4-EUR to UAH;"
                      "5-UAH to USD; 6-UAH to EUR: "))
while choice:
    amount = int(input("Enter the amount of money: "))
    if choice == 1:
        print(amount * 0,91)
        continue
    if choice == 2:
        print(amount * 36.86)
        continue
    if choice == 3:
        print(amount * 1.1)
        continue
    if choice == 4:
        print(amount * 40.42)
        continue
    if choice == 5:
        print(amount * 0.027)
        continue
    if choice == 6:
        print(amount * 0.025)
        continue
    else:
        break

# Задание 5
# Пользователь вводит число. Определить количество цифр в этом числе, посчитать их сумму и среднее арифметическое.
# Определить количество нулей в этом числе. Общение с пользователем организовать через меню.

while 1:
    user_number3 = int(input("Enter the number: "))
    solve = int(input("1-количество цифр; 2-суммa; 3-седнее арифметическое; 4-количество нулей:"))
    if solve == 1:
        amount = 0
        while user_number3:
            amount += 1
            user_number3 //= 10
            print(amount)
    if solve == 2:
        sum = 0
        while user_number3:
            sum += user_number3 % 10
            user_number3 //= 10
            print(sum)
    if solve == 3:
        amount = 0
        sum = 0
        while user_number3:
           sum += user_number3 % 10
           user_number3 //= 10
           amount += 1
           user_number3 //= 10
           print(sum / amount)
    if solve == 4:
        zero = 0
        while user_number3:
            if user_number3 % 10 == 0:
                zero += 1
            user_number3 //= 10
            print(zero)


