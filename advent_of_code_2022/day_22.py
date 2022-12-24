import numpy as np
import re

FILE = 'data/day22.txt'

r_rotation = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
l_rotation = {(0, 1): (-1, 0), (1, 0): (0, 1), (0, -1): (1, 0), (-1, 0): (0, -1)}
direction_score = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}


class Tile:
    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column
        self.bottom_neighbour = None
        self.left_neighbour = None
        self.right_neighbour = None
        self.top_neighbour = None

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __repr__(self):
        return f'{self.value} {self.row} {self.column}'


def parse_input():
        map_, instructions = open(FILE).read().split('\n\n')
        parsed_map = []
        for line in map_.split('\n'):
            row = []
            for char in line:
                if char == '.':
                    row.append(0)
                elif char == '#':
                    row.append(1)
                else:
                    row.append(-1)
            parsed_map.append(row)
        max_len = 0
        for r in parsed_map:
            max_len = max(max_len, len(r))
        for r in parsed_map:
            if len(r) < max_len:
                r += [-1] * (max_len - len(r))
        tiled_map = []
        for i, row in enumerate(parsed_map):
            tiled_row = []
            for j, column in enumerate(row):
                tiled_row.append(Tile(column, i, j))
            tiled_map.append(tiled_row)
        return tiled_map, re.findall(r"[^\W\d_]+|\d+", instructions)


def find_neighbour(current_i, current_j, direction, tiled_map):
    neighbour_i, neighbour_j = (current_i + direction[0]) % len(tiled_map), (current_j + direction[1]) % len(tiled_map[0])
    while tiled_map[neighbour_i][neighbour_j].value == -1:
        neighbour_i, neighbour_j = (neighbour_i + direction[0]) % len(tiled_map), (neighbour_j + direction[1]) % len(tiled_map[0])
    return tiled_map[neighbour_i][neighbour_j]


def connect_tiled_map(tiled_map):
    for i in range(len(tiled_map)):
        for j in range(len(tiled_map[i])):
            tiled_map[i][j].top_neighbour = find_neighbour(i, j, (-1, 0), tiled_map)
            tiled_map[i][j].right_neighbour = find_neighbour(i, j, (0, 1), tiled_map)
            tiled_map[i][j].bottom_neighbour = find_neighbour(i, j, (1, 0), tiled_map)
            tiled_map[i][j].left_neighbour = find_neighbour(i, j, (0, -1), tiled_map)
    return tiled_map


def connect_until_wall(tiled_map):
    for i in range(len(tiled_map)):
        for j in range(len(tiled_map[i])):
            if i - 1 >= 0 and tiled_map[i - 1][j].value >= 0:
                tiled_map[i][j].top_neighbour = find_neighbour(i, j, (-1, 0), tiled_map)
            if j + 1 < len(tiled_map[i]) and tiled_map[i][j + 1].value >= 0:
                tiled_map[i][j].right_neighbour = find_neighbour(i, j, (0, 1), tiled_map)
            if i + 1 < len(tiled_map) and tiled_map[i + 1][j].value >= 0:
                tiled_map[i][j].bottom_neighbour = find_neighbour(i, j, (1, 0), tiled_map)
            if j - 1 >= 0 and tiled_map[i][j - 1].value >= 0:
                tiled_map[i][j].left_neighbour = find_neighbour(i, j, (0, -1), tiled_map)
    return tiled_map


def move(current_position, direction, edges):
    if (current_position, direction) in edges:
        if edges[(current_position, direction)][0].value != 1:
            return edges[(current_position, direction)]
        else:
            return current_position, direction
    if direction == (0, 1) and current_position.right_neighbour.value == 0:
        return current_position.right_neighbour, direction
    if direction == (1, 0) and current_position.bottom_neighbour.value == 0:
        return current_position.bottom_neighbour, direction
    if direction == (0, -1) and current_position.left_neighbour.value == 0:
        return current_position.left_neighbour, direction
    if direction == (-1, 0) and current_position.top_neighbour.value == 0:
        return current_position.top_neighbour, direction
    return current_position, direction


def revert_direction(direction):
    return direction[0] * (-1), direction[1] * (-1)


def create_edge(first_edge, second_edge, first_direction, second_direction, edges):
    assert first_edge.shape == second_edge.shape
    for f, s in zip(first_edge, second_edge):
        edges[(f, first_direction)] = (s, second_direction)
        edges[(s, revert_direction(second_direction))] = (f, revert_direction(first_direction))


def first_problem_solution():
    tiled_map, instructions = parse_input()
    current_position = None
    direction = (0, 1)
    for i in range(len(tiled_map)):
        for j in range(len(tiled_map[i])):
            if tiled_map[i][j].value == 0:
                current_position = tiled_map[i][j]
                break
        if current_position is not None:
            break
    connect_tiled_map(tiled_map)
    for instruction in instructions:
        if instruction == 'R':
            direction = r_rotation[direction]
        elif instruction == 'L':
            direction = l_rotation[direction]
        else:
            instruction = int(instruction)
            while instruction > 0:
                current_position, direction = move(current_position, direction, {})
                instruction -= 1
    return 1000 * (current_position.row + 1) + 4 * (current_position.column + 1) + direction_score[direction]


def second_problem_solution():
    tiled_map, instructions = parse_input()
    current_position = None
    direction = (0, 1)
    for i in range(len(tiled_map)):
        for j in range(len(tiled_map[i])):
            if tiled_map[i][j].value == 0:
                current_position = tiled_map[i][j]
                break
        if current_position is not None:
            break
    connect_until_wall(tiled_map)
    tiled_map = np.array(tiled_map)
    edges = {}

    create_edge(tiled_map[0, 50:100], tiled_map[150:200, 0], (-1, 0), (0, 1), edges)
    create_edge(tiled_map[0, 100:150], tiled_map[199, 0:50], (-1, 0), (-1, 0), edges)
    create_edge(tiled_map[49, 100:150], tiled_map[50:100, 99], (1, 0), (0, -1), edges)
    create_edge(tiled_map[100, 0:50], tiled_map[50:100, 50], (-1, 0), (0, 1), edges)
    create_edge(tiled_map[149, 50:100], tiled_map[150:200, 49], (1, 0), (0, -1), edges)
    create_edge(tiled_map[0:50, 149], np.flip(tiled_map[100:150, 99]), (0, 1), (0, -1), edges)
    create_edge(tiled_map[100:150, 0], np.flip(tiled_map[0:50, 50]), (0, -1), (0, 1), edges)

    for instruction in instructions:
        if instruction == 'R':
            direction = r_rotation[direction]
        elif instruction == 'L':
            direction = l_rotation[direction]
        else:
            instruction = int(instruction)
            while instruction > 0:
                current_position, direction = move(current_position, direction, edges)
                instruction -= 1
    return 1000 * (current_position.row + 1) + 4 * (current_position.column + 1) + direction_score[direction]


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 159034
    print(f'Solution to second problem is {second_problem_solution()}') # 147245