# class Car:
#     # атрибуты класса
#     # color = "black"
#     # countWheels = 4
#     #
#     def __init__(self,color,name):
#         print("init working")
#         self.__color = color
#         self.__name = name
#     def __del__(self):
#       print("del car")
# myCar = Car("red","audi")
# # yCar.get_info()m
# myCar.color = "silver"
# #     def set__color(self,new_color):
# #        self.color = new_color
# #     # def get_info(self):
# #     #     print(self.color, self.name, self.speed)
# #     # def set_name(self, name):
# #     #     self.name = name
# #     # def set_speed(self, speed):
# #     #     self.speed = speed
# #     # def get_color(self):
# #         return self.__color
# #     def get_info(self):
# #         print(self.__color, self.color, self.name, self.speed)
# #
# # Car.color = "red"
# # print(Car.color)
# # #
# # myCar = Car()
# # # print(myCar.color)
# # # myCar.set_color("silver")
# # # myCar.__color = "test"
# # # # myCar2 = Car()
# # # #
# # # # myCar2.get_info()
# # #
# # # ferrary = Car()
# # # cadilac = Car()
# # # ferrary.set_name("ferrary")
# # # cadilac.set_name("cadilac")
# # # ferrary.set_speed("250 км/ч")
# # # cadilac.set_speed("200 км/ч")
# # # print(ferrary.get_info())
# # # print(cadilac.get_info())
# # #
# # # # Дополните класс автомобиля еще двумя атрибутами объекта –
# # # # названием автомобиля (name) и скорость (speed). Продемонстрируйте применение
# # # # атрибутов создав два объекта – ferrary со скоростью 250 км/ч и cadilac со скоростью 200 км/ч
# # # # Метод info должен выводить не только цвет автомобиля, но и его название и скорость.
# #
# # print(myCar.get_color())
#
#     def set__color(self,new_color):
#        self.__color = new_color
#     def set_name(self, name):
#         self.__name = name
#     def set_speed(self, speed):
#         self.__speed = speed
#     def get_color(self):
#         return self.__color
#     def get_info(self):
#         print(self.__color, self.color, self.__name, self.__speed)
#
#
# ferrary = Car()
# cadilac = Car()
# ferrary.set_name("ferrary")
# cadilac.set_name("cadilac")
# ferrary.set_speed("250 км/ч")
# cadilac.set_speed("200 км/ч")
# print(ferrary.get_info())
# print(cadilac.get_info())

# class Car:
#     def __init__(self,color="red",name,speed="120 км/ч"):
#         print("init working")
#         self.__color = color
#         self.__name = name
#         self.__speed = speed
#
#     def __del__(selfs):
#       print("del car")

# Реализуйте класс “Точка”. Необходимо хранить координаты
# x, y, z в переменных-членах класса. Реализуйте функции-члены
# класса для ввода данных, вывода данных

class Point:
    x = ""
    y = ""
    z = ""
    def set_x(self,x):
        self.__x = x
    def set__y(self,y):
        self.__y = y
    def set__z(self,z):
        self.__z = z
    def get_info(self):
        print(self.__x, self.__y, self.__z)




    # def __int__(self, x,y,z):
    #     self.__x = x
    #     self.__y = y
    #     self.__z = z