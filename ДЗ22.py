# 1. Напишите программу, которая принимает список кортежей (имя, возраст) и выводит только те имена,
# у которых возраст больше 18.
# Пример входных данных: [("Анна", 22), ("Иван", 16), ("Мария", 20), ("Петр", 25)]
# Ожидаемый вывод: Анна Мария Петр

nameAge = [("Анна", 22), ("Иван", 16), ("Мария", 20), ("Петр", 25)]
print([x for x, y, *z in nameAge if y > 18])

# 2. Напишите программу, которая принимает два кортежа с координатами точек в двумерном пространстве и вычисляет
# расстояние между ними.
# Пример входных данных: (3, 4), (6, 8)

coordinates1 = (3, 4)
coordinates2 = (6, 8)
distance = ((coordinates2[0] - coordinates1[0]) ** 2) + ((coordinates2[1] - coordinates1[1]) ** 2)
print("distance: ", distance)


# 3. Напишите программу, которая принимает список кортежей (название товара, количество) и считает общее
# количество товаров.
# Пример входных данных: [('Яблоки', 10), ('Молоко', 5), ('Хлеб', 3), ('Масло', 2)]
# Ожидаемый вывод: Общее количество товаров: 20

def calculate_total_quantity(product):
    total_quantity = sum(map(lambda x: x[1], product))
    return total_quantity
product = [('Яблоки', 10), ('Молоко', 5), ('Хлеб', 3), ('Масло', 2)]
print(f"Общее количество товаров: {calculate_total_quantity(product)}")


# 4. Напишите программу, которая принимает список кортежей с информацией о фильмах (название, год выпуска, режиссер)
# и выводит фильмы, выпущенные после 2000 года.
# Пример входных данных: [('Интерстеллар', 2014, 'Кристофер Нолан'), ('Матрица', 1999, 'Лана Вачовски'),
# ('История игрушек', 1995, 'Джон Лассетер'), ('Гравитация', 2013, 'Альфонсо Куарон')]
# Ожидаемый вывод: Фильмы, выпущенные после 2000 года:
# Интерстеллар (2014), реж. Кристофер Нолан
# Гравитация (2013), реж. Альфонсо Куарон


movies = [('Интерстеллар', 2014, 'Кристофер Нолан'), ('Матрица', 1999, 'Лана Вачовски'),
          ('История игрушек', 1995, 'Джон Лассетер'), ('Гравитация', 2013, 'Альфонсо Куарон')]
print("Фильмы, выпущенные после 2000 года: ", ([(x, y, z) for x, y, *z in movies if y > 2000]))


# 5.Напишите программу, которая принимает список кортежей с данными о студентах (имя, группа, средний балл)
# и выводит студентов с наивысшим и наименьшим средним баллом.
# Пример входных данных: [('Иванов', 'Группа 1', 4.5), ('Петров', 'Группа 2', 3.8), ('Сидорова', 'Группа 1', 4.2),
# ('Смирнов', 'Группа 2', 4.1)]
# Ожидаемый вывод: Студент с наивысшим средним баллом:
# Иванов, Группа 1, 4.5
# Студент с наименьшим средним баллом:
# Петров, Группа 2, 3.8

def max_grade_student(student_data):
    max_grade = max(map(lambda x: x[2], student_data))
    return max_grade
student_data = [('Иванов', 'Группа 1', 4.5), ('Петров', 'Группа 2', 3.8), ('Сидорова', 'Группа 1', 4.2),
                ('Смирнов', 'Группа 2', 4.1)]
def min_grade_student(student_data):
    min_grade = min(map(lambda x: x[2], student_data))
    return min_grade

print("Студент с наивысшим средним баллом: ", max_grade_student(student_data))
print("Студент с наименьшим средним баллом: ", min_grade_student(student_data))


# 6. Напишите программу, которая принимает список кортежей с информацией о футбольных командах (название,
# количество побед, количество поражений) и выводит команды со 100 и более победами.
# Пример входных данных: [('Барселона', 120, 20), ('Реал Мадрид', 110, 30), ('Манчестер Юнайтед', 90, 40),
# ('Бавария', 100, 20)]
# Ожидаемый вывод: Команды с 100 и более победами:
# Барселона: 120 побед
# Реал Мадрид: 110 побед
# Бавария: 100 побед

football_team = [('Барселона', 120, 20), ('Реал Мадрид', 110, 30), ('Манчестер Юнайтед', 90, 40), ('Бавария', 100, 20)]
print("Команды с 100 и более победами: ", ([(x, y) for x, y, *z in football_team if y > 100]))

# 7. Напишите программу, которая принимает список кортежей с информацией о книгах (название, автор, год издания)
# и выводит список авторов без повторений.
# Пример входных данных: [('Мастер и Маргарита', 'Михаил Булаков', 1967),
# ('Преступление и наказание', 'Федор Достоевский', 1866), ('Война и мир', 'Лев Толстой', 1869),
# ('1984', 'Джордж Оруэлл', 1949)]
# Ожидаемый вывод: Список авторов без повторений:
# Михаил Булгаков
# Федор Достоевский
# Лев Толстой
# Джордж Оруэлл

books = [('Мастер и Маргарита', 'Михаил Булаков', 1967), ('Преступление и наказание', 'Федор Достоевский', 1866),
         ('Война и мир', 'Лев Толстой', 1869), ('1984', 'Джордж Оруэлл', 1949)]

print([y for x, y, *z in books])