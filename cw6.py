# nums = [1, 2, 3, 4, 5]
# print(type(nums))
# print(nums)
# #
# print(nums[0])
#
# mylist = ['10', 123, 4.15, True, nums]
# print(mylist)
#
# nums[0] = 10
#
# for value in nums:
#     print(value, end=" | ")
# print("\n----len----")
# print(len(nums))

# for i in range(0, 7, 2):

# salary = [12345, 14532, 17523, 23421, 21345, 32124, 36214, 34214, 31245, 30123, 29313, 20235]
# sum = 0
# for i in salary:
#     sum += i
#     print(sum)
# print(sum / 12 )
# print(min(salary))
# print(max(salary))
#
# maxv = nums[0]
# for num in nums:
#     if maxv < num:
#         maxv = num
# print("max = ", maxv)
# print(max(nums))

# newlist = []
#
# newlist.append("Ilon Mask")
# print(newlist)

# numbers = []
#
# for i in range(10):
#     numbers.append(i)
# print(numbers)

# numbers = [i for i in range(10)]
# numbers.insert(0, 1)
# if 104 in numbers:
#   numbers.remove(104)
# else:
#     print("no elem")
# print(numbers)
# numbers.pop(5)
# print(numbers)
#
# print(numbers.count(-10))
#
# print(numbers.index(2, 4))
#
# list1 = [17, 45, 8, 3, -5, 4000, 0]
# # list1.sort()
# # list1.reverse()
# print(sorted(list1))
# print(list1)

import random
randNums = []
for i in range(10):
    randNums.append(random.randint(-100, 100))
print(randNums)
for i in randNums:
   if i < 0:
    print('negative:', sum(randNums))









