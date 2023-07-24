def sum(n):
    s = 0
    while n:
        s += n
        n -= 1
        return s


print(sum(3))

def rsum(n):
    if n:
        return n + rsum(n - 1)
    else:
        return 0

print(rsum(3))

def fac(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac

print(fac(5))

def rfac(n):
    if n == 0:
        return 1
    return rfac(n - 1) * n


print(rfac(5))

# Написать рекурсивную функцию нахождения степени числа.
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b. Пользователь вводит a и b.
# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.

def rdeg(a, b):
    if b == 1:
        return a
    if b != 1:
     return rdeg(a, b - 1) * a


print(rdeg(5, 3))


def rnum(c, d):
    if c > d:
        return 0
    return c + rnum(c + 1, d)

print (rnum(1, 2))

def rsum (a, b):
    if a >= b:
        return 0
    return a + rsum(a + 1, b)


print(rsum(1, 10))

add = lambda a , b: a + b
print(add(2, 2))

myNumbers = [2, 6, 8, 4]
newNum = lambda x: x + 10
for num in myNumbers:
    print(newNum(num))
print(myNumbers)

for num in myNumbers:
    print((lambda x: x + 10)(num))

students = [['Bob', 80],
            ['Jane', 70],
            ['Andy', 50]]
print(students)
sortedStudents = sorted(students, key=lambda x: x[1])
print(sortedStudents)

# grnToDollar = 37
# discount = 0.15
#
# priceDol = lambda x:x/grnToDollar * (1-discount)
# priceGrn1 = float((input("Input price in grn: ")))
# print(f"price: {priceDol(priceGrn1)} $")

# userName = lambda firstName, lastName: f"Full name: {firstName.title()} {lastName.title()}"
# print(userName("ilon", "mask"))

# Напишите функцию, вычисляющую сумму элементов списка целых. Список передаётся в качестве параметра.

myNumbers = [2, 6, 8, 4]
sum1 = lambda myNumbers: sum(myNumbers)
print(sum1)

# for i in myNumbers:
#     print(myNumbers(sum1))




