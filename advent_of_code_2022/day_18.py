from advent_of_code_2022.utils import line_iterator, to_int

FILE = 'data/day18.txt'


def get_cubes():
    return [tuple(to_int(line.split(','))) for line in line_iterator(FILE)]


def get_adjacent(cube):
    x, y, z = cube
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]


def first_problem_solution():
    cubes = get_cubes()
    score = 0
    for cube in cubes:
        for adj in get_adjacent(cube):
            if adj not in cubes:
                score += 1
    return score


def second_problem_solution():
    cubes = set(get_cubes())
    x, y, z = [], [], []
    for c in cubes:
        x.append(c[0])
        y.append(c[1])
        z.append(c[2])
    cube_min = (min(x) - 1, min(y) - 1, min(z) - 1)
    cube_max = (max(x) + 1, max(y) + 1, max(z) + 1)
    scanned = set()
    queue = [cube_min]
    score = 0
    while queue:
        water = queue.pop()
        if water in scanned:
            continue
        scanned.add(water)
        for adj in get_adjacent(water):
            if adj in cubes:
                score += 1
            if adj not in cubes and adj not in scanned and all(c_min <= c <= c_max for c_min, c, c_max in zip(cube_min, adj, cube_max)):
                queue.append(adj)
    return score


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 4500
    print(f'Solution to second problem is {second_problem_solution()}') # 2558

