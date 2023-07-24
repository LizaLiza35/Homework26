# text = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system,\
# and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself,\
# because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.\
# Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which\
# toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some\
# advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain\
# that produces no resultant pleasure?"
# try:
#     print("We are opening file...")
#     fileObj = open("test.txt", 'r')
#     if fileObj:
#         print("file is open!")
#     # print(fileObj.read(10))
#     # print(fileObj.read())
#     # str1 = fileObj.readline()
#     # print(str1)
#     # rawStr = repr(str1)
#     # print(rawStr)
#     # lines = fileObj.readlines()
#     # print(lines)
#     for line in fileObj:
#         print(line)
# except:
#     print("We cant open this file!")
# try:
#     file = open("test.txt", 'w+')
#     for i in range(5):
#         file.write(str(i)+ "\n")
# finally:
#     file.close()
#
# with open("test.txt") as f:
#     print(f.read())
#
# with open("text.txt") as infile, open("result.txt", 'w') as outfile:
#     data = infile.read()
#     dataRes = data.lower()
#     outfile.write(dataRes)
#
#
# def replaceTextInFile(fileName, oldText, newText):
#     with open(fileName) as file:
#         data = file.read()
#         data = data.replace(oldText, newText)
#     with open(fileName, 'w') as file:
#         file.write(data)
# def readFromFile(fileName):
#     with open(fileName) as file:
#         data = file.read()
#         print(data)
# print("old text")
# readFromFile("test.txt")
# replaceTextInFile("test.txt", 'you', 'we')
# print("new text")
# readFromFile("test.txt")
#
# def wordCounter(fileName):
#     words = 0
#     with open(fileName) as file:
#         data = file.read()
#         lines = data.split()
#         for word in lines:
#             if not word.isnumeric():
#                 words += 1
#     return words
# # print("old text")
# readFromFile("test.txt")
#
# print(f"Count words: {wordCounter('test.txt')}")

# def removeLine(fileIn, fileOut, lineNumber):
#     with open(fileIn) as file:
#         lines = file.readlines()
#         counter = 1
#         with open(fileOut, 'w') as file:
#             for line in lines:
#                 if counter != lineNumber:
#                     file.write(line)
#                 counter += 1
#
# removeLine("test.txt", "test.txt", 1)

# Задание 1
#
# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся,
# чья оценка меньше 3 баллов и посчитать средний балл по классу.
#
# Примерное содержание файла:
#
# Иванов О. 4
# Петров И. 3
# Дмитриев Н. 2
# Смирнова О. 4
# Керченских В. 5
# Котов Д. 2
# Бирюкова Н. 1
# Данилов П. 3
# Аранских В. 5
# Лемонов Ю. 2
# Олегова К. 4

def studentGrade (name, grade):
  with open(name) as file:
      data = file.readlines()
      lines = data.split()
      if lines.len -1  < 3:
          grade += 1
  return grade

print (studentGrade("test.txt", 1))


