from advent_of_code_2022.utils import read_all

FILE = 'data/day6.txt'


def find_marker(line, length):
    for i in range(len(line) - length):
        if len(set(line[i: i + length])) == length:
            return i + length
    return None


def first_problem_solution():
    return find_marker(read_all(FILE)[0], 4)


def second_problem_solution():
    return find_marker(read_all(FILE)[0], 14)


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
