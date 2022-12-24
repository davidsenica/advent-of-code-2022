from copy import deepcopy

from advent_of_code_2022.utils import line_iterator, to_int

FILE = 'data/day20.txt'


def solve(sequence, iteration):
    sequence_copy = deepcopy(sequence)
    for _ in range(iteration):
        for s in sequence:
            sequence_copy.pop(pos := sequence_copy.index(s))
            sequence_copy.insert((pos + s[0]) % (len(sequence_copy)), s)
    mixed_sequence = [s[0] for s in sequence_copy]
    zero_position = mixed_sequence.index(0)
    return sum([mixed_sequence[(zero_position + offset) % len(mixed_sequence)] for offset in [1000, 2000, 3000]])


def first_problem_solution():
    sequence = [(int(line), i) for i, line in enumerate(line_iterator(FILE))]
    return solve(sequence, 1)


def second_problem_solution():
    sequence = [(int(line) * 811589153, i) for i, line in enumerate(line_iterator(FILE))]
    return solve(sequence, 10)


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 4426
    print(f'Solution to second problem is {second_problem_solution()}') # 8119137886612
