from advent_of_code_2022.utils import line_iterator
import re
import numpy as np

FILE = 'data/day14.txt'


def build_cave():
    cave = np.zeros((800, 800))
    for line in line_iterator(FILE):
        previous = None
        for m in line.split(' -> '):
            x, y = map(int, m.split(','))
            cave[y, x] = -1  # rock
            if previous:
                first_y, second_y = min(y, previous[1]), max(y, previous[1]) + 1
                first_x, second_x = min(x, previous[0]), max(x, previous[0]) + 1
                cave[first_y:second_y, first_x:second_x] = -1
            previous = (x, y)
    lowest_points_y = max(np.argmin(cave, axis=0)) + 2
    cave[lowest_points_y, :] = -1
    return cave[0:lowest_points_y + 1, :]


def fill_sand(cave, start_x, start_y, max_y):
    x = start_x
    y = start_y
    while y + 1 < cave.shape[0] and not (cave[start_y + 1, start_x] != 0 and cave[start_y + 1, start_x - 1] != 0 and cave[start_y + 1, start_x + 1] != 0):
        if y >= max_y:
            return False
        if cave[y+1, x] == 0:
            y += 1
        elif cave[y+1, x-1] == 0:
            y += 1
            x -= 1
        elif cave[y+1, x+1] == 0:
            y += 1
            x += 1
        else:
            cave[y, x] = 1
            return True


def first_problem_solution():
    cave = build_cave()
    score = 0
    while fill_sand(cave, 500, 0, cave.shape[0] - 2):
        score += 1
    return score


def second_problem_solution():
    cave = build_cave()
    score = 0
    while fill_sand(cave, 500, 0, cave.shape[0]):
        score += 1
    return score + 1


def main():
    print(f'Solution to first problem is {first_problem_solution()}')  # 888
    print(f'Solution to second problem is {second_problem_solution()}')  # 26461
