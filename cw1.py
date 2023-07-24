'''
age = 10
# int float str Non Bool

number1 = 100
print(type(number1))
number2 = 4.5
print(type(number2))

str1= "test str"
print(type(str1))

# True False boolean
check = True
print(type(check))

# del age
# str() int() float() bool() преобразования типов
print("age:" + str(age))

print(int(8/2))


min = int(input("Enter minutes- "))
print("Seconds -", min * 60)

#1 Создайте переменную num и присвойте ей значение 3. Выведите значение этой переменной на экран с помощью метода print.
number = 3
print(type(number))
#2 Создайте переменные a=10 и b=2. Выведите на экран их сумму, разность, произведение и частное (результат деления).
a = 10
b = 2
print(int(a+b),int(a-b), int(a*b), int(a/b))
#3 Создайте переменные c=15 и d=2. Просуммируйте их, а результат присвойте переменной result. Выведите на экран значение переменной result.
c= 15
d= 2
result = c + d
print(type(result))
#4  Создайте переменные a=10, b=2 и c=5. Выведите на экран их сумму.
a=10
b=2
c=5
print(type(a+b+c))
#5 Создайте переменные a=17 и b=10. Отнимите от a переменную b и результат присвойте переменной c. Затем создайте п
# еременную d, присвойте ей значение 7. Сложите переменные c и d, а результат запишите в переменную result. Выведите на экран значение переменной result.
a=17
b=10
c= a - b
d= 7
result = c + d
print(type(result))
'''
#Задание 1.

#Пользователь вводит с клавиатуры расстояние до аэропорта и время, за которое нужно доехать. Вычислить скорость, с которой ему нужно ехать.
#distance = int(input("Enter distance- "))
#time = int(input("Enter time- "))
#print("Speed -", int(distance / time), "km/h")

#Задание 2.

#Пользователь вводит с клавиатуры время начала и время завершения телефонного разговора (часы, минуты и секунды). Посчитать стоимость разговора, если стоимость минуты – 30 копеек.

#timeStart = float(input("Enter start talk, minutes - "))
#timeEnd = float(input("Enter end talk, minutes - "))
#price = 30
#print("Cost-", int((timeEnd - timeStart)*30/100),"UAH")

time = int(input("Enter hours- "))
work = float(input("Enter the work rate - "))
print("Salary -", float(time * work), "UAH")




