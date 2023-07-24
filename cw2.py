'''
num = 1
if num ==2:
    print("test if")
else:
    print("else work")

age = 10

if age > 0 and age < 6:
    print("1")
elif age >= 6 and age < 18:
    print ("2")
elif age >=18 and age < 18:
    print("3")
else:
    print("end")

#четное нечетне
user_num = int(input("Enter num - "))
if user_num % 2 == 0:
    print("even")
else:
    print("odd")

#меньшее большее число

user_num1 = int(input("Enter num 1 -"))
user_num2 = int(input("Enter num 2 -"))
if user_num1 < user_num2:
    print(user_num1)
else:
    print(user_num2)
'''
'''
user_num3 = int(input("Enter num 3 - "))
if user_num3 > 0:
    print("positive")
elif user_num3 < 0:
    print("negative")
else:
    print("zero")
'''
'''
user_num5 = int(input("Enter num 5 -"))
user_num6 = int(input("Enter num 6 -"))
if user_num5 == user_num6:
    print("equals")
if user_num5 > user_num6:
    print(user_num5, user_num5)
else:
    print(user_num6, user_num5)
'''
'''
user_num11 = int(input("Enter num 1 -"))
user_num12 = int(input("Enter num 2- "))
user_num13 = int(input("Enter num 3 -"))
user_num14 = int(input("Enter num 4 -"))
user_num15 = int(input("Enter num 5 -"))
if (user_num11 + user_num12 + user_num13 + user_num14 +user_num15) // 5 >= 4:
   print("Yes")
else:
   print("No")
'''
'''
user_num15 = int(input("Enter num - "))
if (user_num15 % 2 == 0):
    print(user_num15 *3)
else:
    print(user_num15 / 2)
'''

# user_num1 = int(input("Enter num 1 -"))
# user_num2 = int(input("Enter num 2 -"))
# sign = type(input("Enter 1 +  2 -  3 *  4 /"))
# if sign == 1:
#     print(user_num1 + user_num2)
# elif sign == 2:
#     print(user_num1 - user_num2)
# elif sign == 3:
#     print(user_num1 * user_num2)
# elif sign == 4:
#     print(user_num1 / user_num2)

# user_second = int(input("Enter seconds -"))
# user_chose = int(input("Enter 1- hour, 2- minutes or 3- seconds -"))
# if user_chose == 1:
#     print(24 - (user_second) / 60 /60)
# if user_chose == 2:
#     print(1440 - (user_second)/60)
# if user_chose == 3:
#     print(86400 - user_second)

# user_diameter = int(input("Enter diameter -"))
# user_chose = int(input("Enter 1-area; 2-perimeter -"))
# if user_chose == 1:
#     print(3.14 * (user_diameter / 2)**2)
# if user_chose == 2:
#     print(2 * 3.14 * (user_diameter / 2))

user_num1 = input("Enter num 1 -")
user_num2 = input("Enter num 2 -")
if user_num1.isdigit() and user_num2.isdigit():
    user_num1 = float(user_num1)
    user_num2 = float(user_num2)
else:
    print("error input")
sign = type(input("Enter 1- mod  2 - pov 3 - div:"))
if sign == 1:
    print(user_num1 % user_num2)
elif sign == 2:
    print(user_num1 ** user_num2)
elif sign == 3:
    print(user_num1 // user_num2)
elif sign == 3 and user_num2 == 0:
    print("Деление на 0!")



