"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List
import sympy


def power_numbers(*numbers) -> List:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    try:
        result = [x**2 for x in numbers]
        return result
    except Exception:
        print('Only lists or tuples are available')

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers,how_to_filter: str) -> List:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    try:
        if how_to_filter == ODD:
            return [x for x in numbers if x % 2 != 0]
        if how_to_filter == EVEN:
            return [x for x in numbers if x % 2 == 0]
        if how_to_filter == PRIME:
            return list(filter(sympy.isprime,numbers))
    except Exception:
        print('Only lists or tuples are available')

