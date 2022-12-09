from advent_of_code_2022.utils import line_iterator

FILE = 'data/day9.txt'


def move_tail(head, tail):
    diff_x = abs(head[0] - tail[0])
    diff_y = abs(head[1] - tail[1])
    if diff_x <= 1 and diff_y <= 1:
        return tail
    x = -1 if tail[0] < head[0] else 1
    y = -1 if tail[1] < head[1] else 1
    if diff_x >= 2 and diff_y >= 2:
        return (head[0] + x, head[1] + y)
    elif diff_x >= 2:
        return (head[0] + x, head[1])
    else:
        return (head[0], head[1] + y)


def first_problem_solution():
    tail_position = (0, 0)
    head_position = (0, 0)
    moves = {'D': (0, -1), 'U': (0, 1), 'R': (1, 0), 'L': (-1, 0)}
    all_tail_positions = set()
    for line in line_iterator(FILE):
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            head_position = (head_position[0] + moves[direction][0], head_position[1] + moves[direction][1])
            tail_position = move_tail(head_position, tail_position)
            if tail_position not in all_tail_positions:
                all_tail_positions.add(tail_position)
    return len(all_tail_positions)


def second_problem_solution():
    tail_positions = [(0, 0) for _ in range(9)]
    head_position = (0, 0)
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    all_tail_positions = set()
    for line in line_iterator(FILE):
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            head_position = (head_position[0] + moves[direction][0], head_position[1] + moves[direction][1])
            tail_positions[0] = move_tail(head_position, tail_positions[0])
            for i in range(1, 9):
                tail_positions[i] = move_tail(tail_positions[i - 1], tail_positions[i])
            if tail_positions[8] not in all_tail_positions:
                all_tail_positions.add(tail_positions[8])
    return len(all_tail_positions)


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
