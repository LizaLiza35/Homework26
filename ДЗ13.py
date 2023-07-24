# Задание 1
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.

user_num1 = int(input("Enter the first number:"))
user_num2 = int(input("Enter the second number:"))
user_num3 = int(input("Enter the third number:"))
user_choice = int(input("Enter 1-sum or 2-product:"))
if user_choice == 1:
    print(user_num1 + user_num2 + user_num3)
elif user_choice == 2:
    print(user_num1 * user_num2 * user_num3)


# Задание 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.

user_number1 = int(input("Enter the first number: "))
user_number2 = int(input("Enter the second number: "))
user_number3 = int(input("Enter the third number: "))
user_choice2 = int(input("Enter 1-max number, 2-min number, 3-arithmetic mean "))
if user_choice2 == 1:
    print(max(user_number1, user_number2, user_number3))
elif user_choice2 == 2:
    print(min(user_number1, user_number2, user_number3))
elif user_choice2 == 3:
        print((user_number1 + user_number2 + user_number3) / 3)

# Задание 3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

user_meter = int(input("Enter the number of meters:"))
user_choice3 = int(input("Enter 1-mile, 2-inch, 3-yard:"))
mile = 0.000621371
inch = 39.3701
yard = 1.093613888889
if user_choice3 == 1:
    print(user_meter * mile, " miles")
elif user_choice3 == 2:
    print(user_meter * inch, " inches")
elif user_choice3 == 3:
    print(user_meter * yard, " yards")

# Задание 4
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник,
# 2 — вторник и т.д.

user_day = int(input("Enter the number from 1 to 7:"))
if user_day == 1:
    print("Monday")
elif user_day == 2:
    print("Tuesday")
elif user_day == 3:
    print("Wednesday")
elif user_day == 4:
    print("Thursday")
elif user_day == 5:
    print("Friday")
elif user_day == 6:
    print("Saturday")
elif user_day == 7:
    print("Sunday")

# Задание 5
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

user_month = int(input("Enter the number from 1 to 12: "))
if user_month == 1:
    print("January")
elif user_month == 2:
    print("February")
elif user_month == 3:
    print("March")
elif user_month == 4:
    print("April")
elif user_month == 5:
    print("May")
elif user_month == 6:
    print("June")
elif user_month == 7:
    print("July")
elif user_month== 8:
    print("August")
elif user_month == 9:
    print("September")
elif user_month == 10:
    print("October")
elif user_month == 11:
    print("November")
elif user_month == 12:
    print("December")

# Задание 6
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»

user_num = int(input("Enter number - "))
if user_num > 0:
    print("Number is positive")
elif user_num < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

# Задание 7
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.

user_number4 = int(input("Enter the number -"))
user_number5 = int(input("Enter the number -"))
if user_number4 == user_number5:
    print("equals")
elif user_number4 > user_number5:
    print(user_number5, user_number4)
else:
    print(user_number4, user_number5)

# Задание 8 *
# Написать программу подсчета стоимости разговора для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран

talkTime = int(input("Enter talk time (minutes): "))
user_choice4 = int(input("1-kyivstar to kyivstar, 2-kyivstar to vodafone/lifecell,  "
                         "3-vodafone to vodafone, 4-vodafone to kyivstar/lifecell , "
                         "5-lifecell to lifecell, 6-lifecell to kyivstar/vodafone: "))
if user_choice4 == 1:
    print(talkTime * 0.25, "UAH")
elif user_choice4 == 2:
    print(talkTime * 1.5, "UAH")
elif user_choice4 == 3:
    print(talkTime * 0.2, "UAH")
elif user_choice4 == 4:
    print(talkTime * 1.6, "UAH")
elif user_choice4 == 5:
    print(talkTime * 0.1, "UAH")
elif user_choice4 == 6:
    print(talkTime * 1.2, "UAH")


# Задание 9 **
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.

sales1 = int(input("Enter the sales level of the first manager ($): "))
sales2 = int(input("Enter the sales level of the second manager ($): "))
sales3 = int(input("Enter the sales level of the third manager ($): "))
salary = 200
if sales1 < 500:
    salary1 = salary + (sales1 * 0.03)
elif sales1 > 1000:
    salary1 = salary + (sales1 * 0.08)
else:
    salary1 = salary + (sales1 * 0.05)
if sales2 < 500:
    salary2 = salary + (sales2 * 0.03)
elif sales2 > 1000:
    salary2 = salary + (sales2 * 0.08)
else:
    salary2 = salary + (sales2 * 0.05)
if sales3 < 500:
    salary3 = salary + (sales3 * 0.03)
elif sales3 > 1000:
    salary3 = salary + (sales3 * 0.08)
else:
    salary3 = salary + (sales3 * 0.05)
if salary1 > salary2 and salary1 > salary3:
    print("The best manager is the first one")
    salary1 += 200
elif salary2 > salary1 and salary2 > salary3:
    print("The best manager is the second one")
    salary2 += 200
elif salary3 > salary1 and salary3 > salary2:
    print("The best manager is the third one")
    salary3 += 200
print("Salary of the first manager is ", salary1, "$")
print("Salary of the second manager is ", salary2, "$")
print("Salary of the second manager is ", salary3, "$")

