# 1

def simpleDecorator(myFunction):
    print("Hello! I am first decorator!")
    def simpleWrapper():
        print("Func starts working!")
        myFunction()
        print("end func")
    return simpleWrapper

# #2
# def simpleDecorator_v2(myFunction):
#     print("Hello! I am first decorator!")
#     def simpleWrapper():
#         print("Func starts working! 2")
#         myFunction()
#         print("end func 2")
#     return simpleWrapper
#
#
#
#
# @simpleDecorator
# @simpleDecorator_v2
# def sayHi():
#     print("Welcome!")
#
#
#
# sayHiAdvanced = simpleDecorator(sayHi)
# sayHiAdvanced()
#
# def sayBye():
#     print("Buy")
#
# sayBye = simpleDecorator(sayBye)
# sayBye()


# #3
# def simpleDecorator_v3(myFunction):
#     print("Hello! I am first decorator!")
#     def simpleWrapper():
#         print("Func starts working! ")
#         res = myFunction()
#         print("end func ")
#         return res
#
#     return simpleWrapper
# #
# def sum():
#     num1 = 1
#     num2 = 5
#     return num1 + num2
#
# sum = simpleDecorator_v3(sum)
# print(sum())
#
#
# #3
# def simpleDecorator_v4(myFunction):
#     print("Hello! I am first decorator!")
#     def simpleWrapper(x, y):
#         print("Func starts working with params", x, y)
#         res = myFunction(x, y)
#         print("end func ")
#         return res
#
#     return simpleWrapper
#
#
# def sum_v2(num1, num2):
#     return num1 + num2
#
# sum_v2 = simpleDecorator_v4(sum_v2)
# print(sum_v2(5, 5))
#
# #5
# def decoratorWrapper(argfordec):
#     print("got", argfordec)
#     def simpleDecorator_v5(myFunction):
#       print("Hello! I am first decorator!")
#       def simpleWrapper(x, y):
#          print("Func starts working with params", x, y)
#          res = myFunction(x, y)
#          print("end func ")
#          return res
#
#       return simpleWrapper
#     return simpleDecorator_v5
#
# decWithArg = decoratorWrapper(30)
#
# sum_v3 = decWithArg(sum_v2)
# print(sum_v3(4, 4))
#
# pricesUSD = [100, 234, 65, 48]
# print(pricesUSD)
#
# def toPriceNew(priceList):
#     return list(map(lambda x: x * 37, priceList))
#
# print(toPriceNew(pricesUSD))
#
#
# def setDiscountDecoratorWrapper(discount):
#     def changePriceDecorator_v1(myFunction):
#         print("Lets change your price!")
#         def simpleWrapper(argList):
#             print("got", argList)
#             res = myFunction(argList)
#             resWithDisc = list(map(lambda x: int(x * (1 - discount)), res))
#             return resWithDisc
#         return simpleWrapper
#     return changePriceDecorator_v1
#
# # priceToGrn = changePriceDecorator_v1(toPriceNew)
# # print(priceToGrn(pricesUSD))
#
# changePriceDecorator_v2 = setDiscountDecoratorWrapper(0.30)
# priceToGrn = changePriceDecorator_v2(toPriceNew)
# print(priceToGrn(pricesUSD))
#
# import time
# def checkTime(function):
#     def wrapper(*args, **kwargs):
#         startTime = time.time()
#         res = function(*args, **kwargs)
#         print(f"Working time - {time.time() - startTime}")
#         return res
#     return wrapper
# @checkTime
# def testFunc():
#     print("func working")
#     time.sleep(1)
#
# testFunc()

# def avgTimeWorking(count):
#     def checkTime(function):
#         def wrapper(*args, **kwargs):
#             totalTime = 0
#             res = 0
#             for i in range(count):
#               startTime = time.time()
#               res = function(*args, **kwargs)
#               endTime = time.time()
#               totalTime = totalTime + (endTime - startTime)
#             print(f" avg Working time - {totalTime / count}")
#             return res
#         return wrapper
#     return checkTime
#
# import random
#
# @avgTimeWorking(3)
# def testFunc2():
#     rand = random.choice([0.1, 0.3, 0.5, 0.7, 1, 2])
#     time.sleep(rand)
#     print("func working", rand)
#
# testFunc2()

# Создайте декоратор, который проверяет входные параметры функции.
# def checkPar(function):
#     def wrapper(*args, **kwargs):
#         if
#         return function(args)
#
#     return wrapper

# Реализуйте декоратор, который подсчитывает количество вызовов функции.

# def count(function):
#     def wrapper(*args, **kwargs):
#         count = 0
#         count += 1
#         return function(*args, **kwargs)
#
#     wrapper.count = 0
#     return wrapper
#
# @count
# def f():
#     print("Hello")
#
#
# f()
# f()
# f()
#
# print(f.count)


