from advent_of_code_2022.utils import line_iterator, to_int

FILE = 'data/day4.txt'


def contains(a, b):
    if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]):
        a, b = b, a
    if a[0] <= b[0] and a[1] >= b[1]:
        return True
    return False


def overlaps(a, b):
    if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]):
        a, b = b, a
    if a[0] <= b[0] <= a[1]:
        return True
    return False


def first_problem_solution():
    score = 0
    for line in line_iterator(FILE):
        first_range, second_range = list(map(lambda x: to_int(x.split('-')), line.split(',')))
        if contains(first_range, second_range) > 0:
            score += 1
    return score


def second_problem_solution():
    score = 0
    for line in line_iterator(FILE):
        first_range, second_range = list(map(lambda x: to_int(x.split('-')), line.split(',')))
        if overlaps(first_range, second_range):
            score += 1
    return score


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
