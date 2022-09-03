from time import time
import random

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
def num_prime_1(start_num=0, end_num=1001):
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
def num_prime_2(list=[i for i in range(0, 1001)]):
    # list = [i for i in range(start_num, end_num)]
    prime_list = []
    for num in list:
        if all(num % i != 0 for i in range(2, num)):
            prime_list.append(num)
    return prime_list


print('Задание 2', end='\n\n')
print(num_prime_2(num_range()), end='\n\n')


# Задание 3


def report_head(fun):
    def decor():
        res = 'Отчет по продажам магазина за день\n'
        res += fun()
        return res

    return decor


# отчет общий
def report_all(fun):
    def decor():
        res = fun()
        res += f'Продано товаров за день: {sum(sales)} шт.\n' \
               f'Доход от продаж: {sum(sum_sales)} грн.\n'
        return res

    return decor


# отчет по макс и мин проданому товару
def report_max_nim_product(fun):
    def decor():
        res = fun()
        index_max = sales.index(max(sales))
        index_min = sales.index(min(sales))
        res += f'Отчет по продажам товара: \n' \
               f'Наибольшие продажи: Товар {product[index_max]} - {sales[index_max]} шт.' \
               f' Цена: {price[index_max]} грн. - Сумма продаж: {sum_sales[index_max]} \n' \
               f'Наименьшие продажи: Товар {product[index_min]} - {sales[index_min]} шт.' \
               f' Цена: {price[index_min]} грн. - Сумма продаж: {sum_sales[index_min]} \n'
        return res

    return decor


# отчет по макс и мин доходу от продаж товара
def report_max_nim_income(fun):
    def decor():
        res = fun()
        index_max = sum_sales.index(max(sum_sales))
        index_min = sum_sales.index(min(sum_sales))
        res += f'Отчет по доходу от продаж: \n' \
               f'Наибольший доход: Товар {product[index_max]} - Цена: {price[index_max]} грн. ' \
               f' - Количество: {sales[index_max]} шт. - Сумма продаж: {sum_sales[index_max]} \n' \
               f'Наименьший доход: Товар {product[index_min]} - Цена: {price[index_min]} грн.' \
               f' - Количество: {sales[index_min]} шт. - Сумма продаж: {sum_sales[index_min]} \n'
        return res

    return decor


# товары
product = [i+1 for i in range(10)]
# цена товара
price = [random.randrange(100, 1000) for i in range(10)]
# количество проданного в день
sales = [random.randrange(0, 20) for i in range(10)]
# сумма продаж в день
sum_sales = [x * y for x, y in zip(price, sales)]


@report_head
@report_max_nim_income
@report_max_nim_product
@report_all
def day_sales(product=product, price=price, sales=sales, sum_sales=sum_sales):
    report = ''
    for i in range(10):
        report += f'Товар {product[i]}' \
                      f' - Цена: {price[i]} грн.' \
                      f' - Количество проданного товара: {sales[i]} шт.' \
                      f' - Сумма продаж товара в день: {sum_sales[i]} грн.\n'
    return report


print('Задание 3', end='\n\n')
print(day_sales())



