# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

with open("HW1.txt", "r") as file1:
    line1 = set(file1.read().split())
with open("HW2.txt", "r") as file2:
    line2 = set(file2.read().split())
print(line1.difference(line2))

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# Количество символов;
# Количество строк;
# Количество цифр.

with open("HW1.txt", 'r') as file1:
    strings = file1.readlines()
    for line in file1:
        strings += 1
    text = str(strings)
    count_numbers = 0
    i = 0
    while i < len(text):
        if text[i].isdigit():
            count_numbers += 1
        i += 1
with open("HW2.txt", 'w') as file2:
    file2.write(f"Strings: {len(strings)}, symbols: {len(text)}, numbers: {count_numbers}")

# Задание 3
# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.

with open("HW1.txt", 'r') as file:
    lines = file.readlines()
    lines = lines[:-1]

with open("HW2.txt", 'w') as file:
    file.writelines(lines)

# Задание 4
# Дан текстовый файл. Найти длину самой длинной строки.

with open("HW1.txt", 'r') as file:
    x = len(max(file.readlines()))
print("The longest string is: ", x)

# Задание 5
# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

with open("HW1.txt", 'w') as file:
    while True:
        user_str = input("Enter the string: ")
        if not user_str:
            break
    file.write(user_str)

# Задание 6
# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество
# в ней символов и слов.

with open("HW1.txt", 'r') as file:
    string = 0
    for line in file:
        string += 1
        x = line.split()
        print(line, "symbols: ", len(line), ",", "words: ", len(x))
    print("strings: ", string)
