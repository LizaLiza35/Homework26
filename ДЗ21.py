# 1. Реализуйте декоратор, который повторяет выполнение функции заданное количество раз,
# если она завершилась неудачно.

import random
import time
from functools import wraps

def repeat(num_repeat, exception_to_check, sleep_time=0):
    def decorate(function):
        def wrapper(*args, **kwargs):
            for i in range(1, num_repeat+1):
                try:
                    return function(*args, **kwargs)
                except exception_to_check:
                  print("One more time")
                if i < num_repeat:
                 time.sleep(sleep_time)
                raise exception_to_check
        return wrapper
    return decorate

@repeat(3,ValueError,1)
def random_value():
    value = random.randint(1, 5)
    return value
random_value()


# 2. Напишите декоратор, который ограничивает частоту вызова функции.

import time
def frequency(function):
    def wrapper_2(*args, **kwargs):
        time.sleep(1)
        return function(*args, **kwargs)
    return wrapper_2

@frequency
def countdown(number):
    if number < 1:
        print("Go!")
    else:
        print(number)
        countdown(number - 1)

# 3. Напишите декоратор, который записывает входные и выходные данные функции для целей отладки.

import time
from functools import wraps
def checkout(function):
   def wrapper(*args, **kwargs):
      start = time.perf_counter()
      result = function(*args, **kwargs)
      end = time.perf_counter()
      return result
   return wrapper

@checkout
def process_data():
   time.sleep(1)

process_data()
