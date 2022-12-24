import functools
import numpy as np
from advent_of_code_2022.utils import line_iterator

FILE = 'data/day24.txt'


def parse_input():
    floor = []
    blizzards = []
    for i, line in enumerate(line_iterator(FILE)):
        row = []
        for j, char in enumerate(line):
            if char == '#':
                row.append(1)
            else:
                row.append(0)
            if char == '>':
                blizzards.append(((i, j), (0, 1)))
            if char == '<':
                blizzards.append(((i, j), (0, -1)))
            if char == '^':
                blizzards.append(((i, j), (-1, 0)))
            if char == 'v':
                blizzards.append(((i, j), (1, 0)))
        floor.append(row)
    return np.array(floor), blizzards


@functools.lru_cache
def move_blizzards(h, w, blizzards):
    blizzards_position = []
    new_blizzards = []
    for blizzard in blizzards:
        pos, direction = blizzard
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos[0] == 0:
            new_pos = (h - 1, new_pos[1])
        if new_pos[1] == 0:
            new_pos = (new_pos[0], w - 1)
        if new_pos[0] == h:
            new_pos = (1, new_pos[1])
        if new_pos[1] == w:
            new_pos = (new_pos[0], 1)
        blizzards_position.append(new_pos)
        new_blizzards.append((new_pos, direction))
    return blizzards_position, new_blizzards


def bfs(start, end, minutes, floor, blizzards):
    queue = [(start, minutes, blizzards)]
    visited = set()
    h, w = floor.shape
    h, w = h - 1, w - 1
    while queue:
        pos, minutes, blizz = queue.pop(0)
        if pos == end:
            return minutes, blizz
        if (pos, minutes) in visited:
            continue
        visited.add((pos, minutes))
        blizzards_position, blizz = move_blizzards(h, w, tuple(blizz))
        for to_pos in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1), pos]:
            if 0 <= to_pos[0] <= h and 0 <= to_pos[1] <= w and floor[to_pos] != 1 and to_pos not in blizzards_position:
                queue.append((to_pos, minutes + 1, blizz))


def first_problem_solution():
    floor, blizzards = parse_input()
    start = (0, 1)
    end = (len(floor) - 1, len(floor[0]) - 2)
    minutes, _ = bfs(start, end, 0, floor, blizzards)
    return minutes


def second_problem_solution():
    floor, blizzards = parse_input()
    start = (0, 1)
    end = (len(floor) - 1, len(floor[0]) - 2)
    minutes, blizzards = bfs(start, end, 0, floor, blizzards)
    minutes, blizzards = bfs(end, start, minutes, floor, blizzards)
    minutes, blizzards = bfs(start, end, minutes, floor, blizzards)
    return minutes


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 245
    print(f'Solution to second problem is {second_problem_solution()}') # 798
