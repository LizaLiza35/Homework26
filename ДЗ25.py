# Задание 1
# Есть некоторый словарь, который хранит названия стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку данных (используя упаковку и распаковку).

import json
countryCapital = {
    "Ukraine": ["Kyiv"],
    "Greece": ["Athens"]
}
def writeFile(file,data):
    with open(file, 'w') as file:
        json.dump(data, file, indent=4)

def readFile(file):
    with open(file, 'r') as file:
        return json.load(file)




# Задание 2
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

# import pickle
# class Employee:
#     def __init__(self, name, surname, age, position):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.position = position
# class EmployeeSystem:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.employees = []
#     def load(self):
#         try:
#             with open(self.file_path, 'rb') as file:
#                 self.employees = pickle.load(file)
#         except:
#             pass
#     def save(self):


