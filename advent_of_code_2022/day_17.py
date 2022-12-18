from advent_of_code_2022.utils import line_iterator
import numpy
import sys

FILE = 'data/day17.txt'

MAX_WIDTH = 7


def get_rock(index, height):
    if index == 0:
        return [(2, height), (3, height), (4, height), (5, height)]
    if index == 1:
        return [(3, height), (2, height + 1), (3, height + 1), (4, height + 1), (3, height + 2)]
    if index == 2:
        return [(2, height), (3, height), (4, height), (4, height + 1), (4, height + 2)]
    if index == 3:
        return [(2, height), (2, height + 1), (2, height + 2), (2, height + 3)]
    if index == 4:
        return [(2, height), (3, height), (2, height + 1), (3, height + 1)]


def jets():
    jets_direction = open(FILE).read().strip()
    i = 0
    while True:
        if i >= len(jets_direction):
            i = 0
        yield -1 if jets_direction[i] == '<' else 1
        i += 1


def collision(rock, rock_structure):
    if any([r in rock_structure for r in rock]):
        return True
    return False


def move_horizontaly(rock, jet_direction, rock_structure):
    new_rock_position = [(r[0] + jet_direction, r[1]) for r in rock]
    if all([0 <= r[0] < MAX_WIDTH for r in new_rock_position]) and not collision(new_rock_position, rock_structure):
        return new_rock_position
    return rock


def move_verticaly(rock, rock_structure):
    new_rock_position = [(r[0], r[1] - 1) for r in rock]
    if collision(new_rock_position, rock_structure):
        return rock
    return new_rock_position


def detect_loop(cache, rock_num, jet_index, height, max_iteration):
    key = (rock_num % 5, jet_index)
    if key in cache:
        old_rock_num, old_height = cache[key]
        if (max_iteration - rock_num) % (rock_num - old_rock_num) == 0:
            return (height +
                    int((max_iteration - rock_num) / (rock_num - old_rock_num)) * (height - old_height))
    else:
        cache[key] = (rock_num, height)
    return None


def first_problem_solution():
    current_rock = 0
    height = -1
    rock_structure = set([(i, -1) for i in range(MAX_WIDTH)])
    jets_generator = jets()
    while current_rock < 2022:
        rock = get_rock(current_rock % 5, height + 4)
        while True:
            direction = next(jets_generator)
            rock = move_horizontaly(rock, direction, rock_structure)
            previous_rock = rock
            rock = move_verticaly(rock, rock_structure)
            if previous_rock == rock:
                break
        rock_structure = rock_structure.union(set(rock))
        height = max([height] + [r[1] for r in rock])
        current_rock += 1
    return height + 1


def second_problem_solution():
    current_rock = 0
    height = -1
    rock_structure = set([(i, -1) for i in range(MAX_WIDTH)])
    cache = {}
    all_jets = open(FILE).read().strip()
    jets_generator = jets()
    jet_index = 0
    while not (answer := detect_loop(cache, current_rock, jet_index % len(all_jets), height, 1000000000000)):
        rock = get_rock(current_rock % 5, height + 4)
        while True:
            direction = next(jets_generator)
            jet_index += 1
            rock = move_horizontaly(rock, direction, rock_structure)
            previous_rock = rock
            rock = move_verticaly(rock, rock_structure)
            if previous_rock == rock:
                break
        rock_structure = rock_structure.union(set(rock))
        height = max([height] + [r[1] for r in rock])
        current_rock += 1
    return answer + 1


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 3173
    print(f'Solution to second problem is {second_problem_solution()}') # 1570930232582
