import functools
import numpy as np
from advent_of_code_2022.utils import line_iterator

FILE = 'data/day25.txt'

snafu_value = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}


def from_SNAFU(snafu):
    number = 0
    for i, char in enumerate(snafu[::-1]):
        number += (5 ** i) * snafu_value[char]
    return number


def to_snafu(number):
    if number == 0:
        return ''
    remainder = number % 5
    for k, v in snafu_value.items():
        if (v + 5) % 5 == remainder:
            number = (number - v) // 5
            return to_snafu(number) + k
    return ''


def convert_input():
    return [from_SNAFU(line) for line in line_iterator(FILE)]


def first_problem_solution():
    numbers = convert_input()
    return to_snafu(sum(numbers))



def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 2-2=21=0021=-02-1=-0
