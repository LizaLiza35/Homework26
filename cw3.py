# num1 = 1
# num2 = 11
# print("while start")
# while num1 < num2:
#     if num1 % 2 == 0:
#      print(num1, end=" | ")
#     num1 += 1
#     if num1 == 8:
#         break
# else:
#     print("\nwhile finished")
#
# count = 0
# while True:
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(count)
#     if count >= 10:
#         break

# user_num = int(input("Enter the number"))
# i = 0
# while i <= user_num:
#     user_num +=1
#     if i == user_num:
#     break
#     print(user_num)
#
#     num = 0
#     user_num = int(input("Enter the number"))
#     while num < user_num:
#         num += 1
#         print(num)

#
# count = 0
# i = 0
# while True:
#    count += 1
#     count += 1
#     if count >= 10:
#         break
#     if count % 2 == 0:
#         continue
#     print(count)
#
# print("count i = ", i)
#
# sum = 0
#
# while True:
#     num = int(input("enter num"))
#     sum += num
#     if num == 0:
#         print("sum =", sum)
#         break
#
# sum = 0
# count = 0
# while True:
#     mark = int(input("enter mark"))
#     sum += mark
#     count += 1
#     if mark == 0:
#         print("avg mark - ", sum / count)
#         break
#        count += 1

import random
i = 0
while i < 5:
   print(random.randint(1,10))
   i +=1

while True:
 rand_num = random.randint(1,100)
 user_num = 0
 tries = 0
 while rand_num != user_num:
     tries += 1
     user_num = int(input("Enter num - "))
     if user_num < rand_num:
         print("Try bigger")
     elif user_num > rand_num:
         print("Try lower")
 print(f"You guessed at {tries} tries")
 answear = input("Enter y - yes or n - no for continue")
 if answear == 'y':
     print ("New game")
     continue
 else:
     print("Game over!")
     break

# num1 = int(input("Enter the first number"))
# num2 = int(input("Enter the second number"))
# while num1 < num2:
#     num1 += 1
#     print(num1)
#     if num1 > num2:
#         temp = num1
#         num1 = num2
#         num2 = temp
# while num1 < num2:
#     num1 += 1
#     if num1 % 2 == 0:
#         print("Even", num1)
#     if num1 % 2 != 0:
#         print("Odd", num1)
#     if num1 % 7 ==0:
#         print("7", num1)
