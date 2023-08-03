# Задание 1
# Есть некоторый словарь, который хранит названия стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку данных (используя упаковку и распаковку).

# import json
# countryCapital = {
#     "Ukraine": ["Kyiv"],
#     "Greece": ["Athens"]
# }
# def writeFile(file,data):
#     with open(file, 'w') as file:
#         json.dump(data, file, indent=4)
#
# def readFile(file):
#     with open(file, 'r') as file:
#         return json.load(file)
#
# writeFile("ДЗ25.json",countryCapital)
#
# choice = int(input("Enter 1- add, 2- delete, 3- search, 4 - editing, 5 - saving, 6 - loading : "))
# if choice == 1:
#     country = input("Enter country: ")
#     capital = input("Enter the capital: ")
#     def addInformation(file,country,capital):
#         if country in file:
#             print("The country is found")
#         else:
#             countryCapital[country] = [capital]
#     addInformation("ДЗ25.json",country,capital)
#
#     writeFile("ДЗ25.json",countryCapital)
# if choice == 2:
#     country = input("Enter country to delete: ")
#     def deleteInformation(file,country):
#        del countryCapital[country]
#     deleteInformation("ДЗ25.json",country)
#
#     writeFile("ДЗ25.json",countryCapital)
# if choice == 3:
#     country = input("Enter country to search: ")
#     def searchInformation(file,country):
#         if country in countryCapital:
#           print(f"{country} : {country[capital]}")
#         else:
#           print(f"{country} is not found.")
#     searchInformation("ДЗ25.json",country)
# if choice == 4:
#     country = input("Enter country to edit: ")
#     capital = input("Enter the capital to edit: ")
#     def editInformation(file, country, capital):
#       countryCapital[country] = [capital]
#     editInformation("ДЗ25.json", country, capital)
#
#     writeFile("ДЗ25.json", countryCapital)
# if choice == 5:
#







# Задание 2
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

import json
employees = {
    "id1": ["Kyiv"],
    "Greece": ["Athens"]


