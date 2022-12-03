from advent_of_code_2022.utils import line_iterator, read_all
import string

FILE = 'data/day3.txt'

char_value = {
    c: i + 1 for i, c in enumerate(string.ascii_letters)
}


def get_score(strings):
    common = ''.join(set(strings[0]).intersection(*strings[1:]))
    return char_value[common]


def first_problem_solution():
    score = 0
    for line in line_iterator(FILE):
        half_size = len(line) // 2
        score += get_score([line[:half_size], line[half_size:]])
    return score


def second_problem_solution():
    score = 0
    lines = read_all(FILE)
    i = 0
    while i < len(lines):
        score += get_score(lines[i:i+3])
        i += 3
    return score


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
