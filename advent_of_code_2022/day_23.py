from collections import defaultdict

from advent_of_code_2022.utils import line_iterator

FILE = 'data/day23.txt'


def parse_input():
    elves_position = set()
    for i, line in enumerate(line_iterator(FILE)):
        for j, char in enumerate(line):
            if char == '#':
                elves_position.add((i, j))
    return elves_position


def get_all_neighbours(current):
    return {
        'S': (current[0] + 1, current[1]),
        'SE': (current[0] + 1, current[1] + 1),
        'SW': (current[0] + 1, current[1] - 1),
        'N': (current[0] - 1, current[1]),
        'NE': (current[0] - 1, current[1] + 1),
        'NW': (current[0]- 1, current[1] - 1),
        'E': (current[0], current[1] + 1),
        'W': (current[0], current[1] - 1)
    }


def get_new_position(starting_rule, elf, elves_position, neighbours):
    rules = [
        (all(n not in elves_position for n in [neighbours['N'], neighbours['NE'], neighbours['NW']]), (elf[0] - 1, elf[1])),
        (all(n not in elves_position for n in [neighbours['S'], neighbours['SE'], neighbours['SW']]), (elf[0] + 1, elf[1])),
        (all(n not in elves_position for n in [neighbours['W'], neighbours['NW'], neighbours['SW']]), (elf[0], elf[1] - 1)),
        (all(n not in elves_position for n in [neighbours['E'], neighbours['NE'], neighbours['SE']]), (elf[0], elf[1] + 1)),
        ]
    k = 0
    while k < 4:
        if rules[starting_rule][0]:
            return rules[starting_rule][1]
        k += 1
        starting_rule = (starting_rule + 1) % 4
    return None


def first_problem_solution():
    elves_position = parse_input()
    starting_rule = 0
    for _ in range(10):
        new_positions = defaultdict(list)
        for elf in elves_position:
            neighbours = get_all_neighbours(elf)
            if all(n not in elves_position for n in neighbours.values()):
                new_positions[elf] = [elf]
                continue
            new_elf_position = get_new_position(starting_rule, elf, elves_position, neighbours)
            if new_elf_position is None:
                new_positions[elf] = [elf]
                continue
            new_positions[new_elf_position].append(elf)
        new_elves_position = set()
        for k, i in new_positions.items():
            if len(i) > 1:
                new_elves_position = new_elves_position.union(set(i))
            else:
                new_elves_position.add(k)
        elves_position = new_elves_position
        starting_rule = (starting_rule + 1) % 4
    top = min(p[0] for p in elves_position)
    bottom = max(p[0] for p in elves_position)
    left = min(p[1] for p in elves_position)
    right = max(p[1] for p in elves_position)
    score = 0
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if (i, j) not in elves_position:
                score += 1
    return score


def second_problem_solution():
    elves_position = parse_input()
    starting_rule = 0
    round_num = 0
    while True:
        new_positions = defaultdict(list)
        for elf in elves_position:
            neighbours = get_all_neighbours(elf)
            if all(n not in elves_position for n in neighbours.values()):
                new_positions[elf] = [elf]
                continue
            new_elf_position = get_new_position(starting_rule, elf, elves_position, neighbours)
            if new_elf_position is None:
                new_positions[elf] = [elf]
                continue
            new_positions[new_elf_position].append(elf)
        new_elves_position = set()
        if all(k == i[0] and len(i) == 1 for k, i in new_positions.items()):
            break
        for k, i in new_positions.items():
            if len(i) > 1:
                new_elves_position = new_elves_position.union(set(i))
            else:
                new_elves_position.add(k)
        assert len(elves_position) == len(new_elves_position)
        elves_position = new_elves_position
        starting_rule = (starting_rule + 1) % 4
        round_num += 1
    return round_num + 1


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 4082
    print(f'Solution to second problem is {second_problem_solution()}') # 1065
