#
# try:
#     amount = int(input("Enter thr amount of items - "))
#     items_type = input("Enter the type of product?")
#     parts_num = int(input("Enter number of parts?"))
#     parts = amount / parts_num
#     print("add", amount, "of type", items_type)
# except ValueError:
#     print("Amount should be an integer!")
# except ZeroDivisionError:
#     print("You cannot divide by zero!")
# except (TypeError, NameError):
#     print("")
# finally:
#     print("program finished")
#
# try:
#     file = open("text.txt", "w")
# finally:
#     file.close()
#
# try:
#     num = int(input("Enter amount"))
#     if num < 0:
#         raise Exception
#     print("You enter amount", num)
# except Exception:
#     print("num error ")

# try:
#     raise ValueError("some mistake")
# except ValueError as ex:
#     print("Value error", type(ex).__name__)
#     print("descript", ex)
# except Exception as ex:
#     print("soon error!", ex)

# try:
#     i = 0
#     num = int(input("Enter the number"))
#     if num <= 0:
#         raise Exception
#     while i < num:
#       print("*" * num)
#       i += 1
# except ValueError:
#       print("It is must be the number")
# except Exception:
#     print("num error ")

# try:
#         i = 0
#         num1 = int(input("Enter width"))
#         num2 = int(input("Enter height"))
#         if num1 and num2 <= 0:
#             raise Exception
#         if num1 == num2:
#             raise Exception
#         while i < num1:
#             print("*" * num2)
#             i += 1
# except ValueError:
#         print("It is must be the number")
# except Exception:
#         print("num error ")

try:
 i = 0
 num3 = int(input("Enter width"))
 if num3 <= 0:
  raise Exception
 while i < num3:
   if i == 0 or i == num3 - 1:
     print("*" * num3)
   else:
     print("*" + " " * (num3 - 2) + "*")
   i += 1
except ValueError:
     print("It is must be the number")
except Exception:
     print("num error ")
