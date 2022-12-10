from advent_of_code_2022.utils import line_iterator

FILE = 'data/day10.txt'


def run_instructions():
    value = 1
    cycle = 1
    for line in line_iterator(FILE):
        split = line.split(' ')
        if split[0] == 'noop':
            yield cycle, value
            cycle += 1
        else:
            yield cycle, value
            cycle += 1
            yield cycle, value
            cycle += 1
            value += int(split[1])


def first_problem_solution():
    cycles = [20, 60, 100, 140, 180, 220]
    score = 0
    for cycle, value in run_instructions():
        if cycle in cycles:
            score += cycle * value
    return score


def second_problem_solution():
    screen = ['']
    for cycle, value in run_instructions():
        if (cycle-1) % 40 == 0:
            screen.append('')
        screen[-1] += '#' if (cycle - 1) % 40 in [value - 1, value, value + 1] else '.'
    return '\n'.join(screen)


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
