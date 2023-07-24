# Задание 1
# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и его рост.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь
# для хранения информации.
#
while 1:
    basketballs_players = {"Чак Невит": 226, "Марк Итон": 224, "Кристапс Порзингис": 221}
    choice = int(input("Enter 1- add, 2- delete, 3- search, 4 - replace: "))
    if choice == 1:
        name = input("Enter a player's name to add: ")
        height = int(input("Enter the player's height: "))
        basketballs_players[name] = height
        print(basketballs_players)
    elif choice == 2:
        name = input("Enter a player`s name to delete: ")
        del basketballs_players[name]
        print(basketballs_players)
    elif choice == 3:
        name = input("Enter a player`s name to search: ")
        if name in basketballs_players:
            print(f"{name}  {basketballs_players[name]} см")
        else:
            print(f"{name} is not found.")
    elif choice == 4:
        name = input("Enter a player name to replace: ")
        height = int(input("Enter the new height: "))
        basketballs_players[name] = height
        print(basketballs_players)

# Задание 2
# Создайте программу «Англо-французский словарь». Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

while 1:
    translater = {"smile": "sourire", "laugh": "rire"}
    choice_word = int(input("Enter 1- add, 2- delete, 3- search, 4 - replace: "))
    if choice_word == 1:
        English = input("Enter a word in English: ")
        French = input("Enter a word in French: ")
        translater[English] = French
        print(translater)
    elif choice_word == 2:
        English = input("Enter a word in English to delete: ")
        del translater[English]
        print(translater)
    elif choice_word == 3:
        name = input("Enter a word in English to search: ")
        if English in translater:
            print(f"{English}  {translater[English]} ")
        else:
            print(f"{English} is not found.")
    elif choice_word == 4:
        English = input("Enter a word in English to replace: ")
        French = input("Enter the new translation: ")
        translater[English] = French
        print(translater)

# Задание 3
# Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется реализовать возможность добавления, удаления,
# поиска, замены данных. Используйте словарь для хранения информации.

while 1:
    firm = {"name": "Иванов Иван Иванович", "phone number": "0975555555", "work email": "ivanov@firm",
            "position": "manager", "room number": "228", "skype": "Ivan738"}
    option = int(input("Enter 1- add, 2- delete, 3- search, 4 - replace: "))
    if option == 1:
        inform = input("Enter a new information: ")
        detail = input("Enter the detail: ")
        firm[inform] = detail
        print(firm)
    elif option == 2:
        inform = input("Enter information to delete: ")
        del firm[inform]
        print(firm)
    elif option == 3:
        inform = input("Enter information to search: ")
        if inform in firm:
            print(f"{inform}  {firm[inform]}")
        else:
            print(f"{inform} is not found.")
    elif option == 4:
        inform = input("Enter information to replace: ")
        detail = input("Enter the new detail: ")
        firm[inform] = detail
        print(firm)

# Задание 4
# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь для хранения информации.

while 1:
    book = {"author": "George Orwell", "title": "1984", "genre": "dystopia",
            "year of issue": "1949", "number of pages": "500", "publishing house": "Secker and Warburg"}
    option = int(input("Enter 1- add, 2- delete, 3- search, 4 - replace: "))
    if option == 1:
        inform = input("Enter a new information about book: ")
        detail = input("Enter the detail: ")
        book[inform] = detail
        print(book)
    elif option == 2:
        inform = input("Enter information to delete: ")
        del book[inform]
        print(book)
    elif option == 3:
        inform = input("Enter information to search: ")
        if inform in book:
            print(f"{inform}  {book[inform]}")
        else:
            print(f"{inform} is not found.")
    elif option == 4:
        inform = input("Enter information to replace: ")
        detail = input("Enter the new detail: ")
        book[inform] = detail
        print(book)



