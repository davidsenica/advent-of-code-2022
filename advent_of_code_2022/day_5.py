import re
from advent_of_code_2022.utils import line_iterator

FILE = 'data/day5.txt'
MOVE_PATTERN = re.compile("move (\d+) from (\d+) to (\d+)")


def create_crates(tmp_crates):
    crates = [[] for _ in range(9)]
    for i in range(7, -1, -1):
        for j in range(1, 36, 4):
            crate_position = (j - 1) // 4
            crate_letter = tmp_crates[i][j]
            if crate_letter != " ":
                crates[crate_position].append(crate_letter)
    return crates


def read_and_parse():
    crates = [[] for _ in range(9)]
    tmp_crates = []
    parse_moves = False

    for line in line_iterator(FILE):
        if parse_moves:
            yield crates, line
        else:
            if line == '':
                parse_moves = True
                continue
            elif '1' in line:
                crates = create_crates(tmp_crates)
                continue
            else:
                tmp_crates.append(line)


def first_problem_solution():
    for crates, move in read_and_parse():
        match = MOVE_PATTERN.match(move)
        num_of_crates, from_position, to_position = int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) - 1
        for _ in range(num_of_crates):
            crates[to_position].append(crates[from_position].pop())
    return "".join(crates[i][-1] for i in range(9))


def second_problem_solution():
    for crates, move in read_and_parse():
        match = MOVE_PATTERN.match(move)
        num_of_crates, from_position, to_position = int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) - 1
        to_move = crates[from_position][-num_of_crates:]
        crates[from_position] = crates[from_position][:-num_of_crates]
        crates[to_position] = crates[to_position] + to_move
    return "".join(crates[i][-1] for i in range(9))


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
