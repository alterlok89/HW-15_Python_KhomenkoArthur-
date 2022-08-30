from time import time

# Задание 1


class DecoratorPrime:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self):
        start_time = time()
        self.fn()
        end_time = time()
        def_time = end_time - start_time
        return f'Время выполнения функции (сек): {def_time}\n' \
               f'Список простых чисел: {self.fn()}'


# функция определения простых чисел от 0 до 1000
@DecoratorPrime
def num_prime_1(start_num=0, end_num=1000):
    list = [i for i in range(start_num, end_num)]
    prime_list = []
    for num in list:
        if all(num % i != 0 for i in range(2, num)):
            prime_list.append(num)
    return prime_list


print('Задание 1', end='\n\n')
print(num_prime_1(), end='\n\n')


# Задание 2

class DecoratorPrimeRange:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, list):
        start_time = time()
        self.fn(list)
        end_time = time()
        def_time = end_time - start_time
        return f'Время выполнения функции (сек): {def_time}\n' \
               f'Список простых чисел: {self.fn(list)}'


def num_range():
    num_start = int(input('Введите начало диапазона: '))
    num_end = int(input('Введите конец диапазона: '))
    if num_start < num_end:
        list = [i for i in range(num_start, num_end)]
    else:
        list = [i for i in range(num_end, num_start)]
    return list


# print(num_range())
# функция определения простых чисел от 0 до 1000 (идентична первому заданию)
@DecoratorPrimeRange
def num_prime_2(list=[i for i in range(0, 1000)]):
    # list = [i for i in range(start_num, end_num)]
    prime_list = []
    for num in list:
        if all(num % i != 0 for i in range(2, num)):
            prime_list.append(num)
    return prime_list

print('Задание 2', end='\n\n')
print(num_prime_2(num_range()), end='\n\n')



