# import pickle
# #
# simpleObj = dict(int_list=[1, 2, 3], text = "test string", number=4.5, none=None, boolean=True)
# print(simpleObj)
#
# with open("test.txt", 'wb') as file:
#     serialData = pickle.dumps(simpleObj)
#     file.write(serialData)
#
# with open("test.txt", "wb") as file:
#     pickle.dump(simpleObj, file)
#
# with open("test.txt", "rb") as file:
#     decodeObj = pickle.load(file)
#
# print(decodeObj)
# #
# import json
# { "firstName": "Jane", "lastName": "Doe", "hobbies": ["running", "sky diving", "singing"], "age": 35, "children": [ { "firstName": "Alice", "age": 6 }, { "firstName": "Bob", "age": 8 } ] }
# with open ("data_file.json", "w") as file:
#     json.dump(simpleObj, file, indent=4)
#
# myTuple = (1, "r")
# encoded_tuple = json.dumps(myTuple)
# decoded_tuple = json.loads((encoded_tuple))
# print(myTuple == decoded_tuple)
# print(type(decoded_tuple))
#
# with open("data_file.json", "r") as file:
#     data = json.load(file)
#
# print(data)

# Есть некоторый словарь, который хранит названия музыкальных групп(исполнителей) и альбомов.
# Название группы используется в качестве ключа, название альбомов в качестве значения.
# Необходимо реализовать: добавление данных, удаление данных, поиск данных, редактирование данных, сохранение и загрузку данных
# (используя упаковку и распаковку).

import json
musecDict = {
    "Linckin Park": ['in the end'],
    "Lana Del Ray": ["Summertime"]
}
def writeFile(file,data):
    with open(file, 'w') as f:
        json.dump(data,f, indent=4)

def readFile(file):
    with open(file, 'r') as f:
        return json.load(f)

writeFile("data.file.json",musecDict)
# print(readFile("data_file.json"))

name = input("Enter your musician: ")
song = input("Enter the song: ")
def addMusicin(f,name,song):
    data = json.load(f)
     with open(writeFile, 'r'):
     if name in musecDict:
         print("The mucision is found")
     else:
       musecDict[name] = song
       return musecDict
print(addMusicin("data_file.json",name,song))

