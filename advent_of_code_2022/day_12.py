from advent_of_code_2022.utils import line_iterator

FILE = 'data/day12.txt'


def generate_world():
    world = []
    start_position = (0, 0)
    end_position = (0, 0)

    for i, line in enumerate(line_iterator(FILE)):
        tmp = []
        for j, letter in enumerate(line):
            if letter == 'S':
                start_position = (i, j)
                tmp.append(ord('a'))
            elif letter == 'E':
                end_position = (i, j)
                tmp.append(ord('z'))
            else:
                tmp.append(ord(letter))
        world.append(tmp)
    return world, start_position, end_position


def can_step(world, from_pos, to_pos):
    if 0 > to_pos[0] or to_pos[0] >= len(world) or 0 > to_pos[1] or to_pos[1] >= len(world[0]):
        return False
    return (world[to_pos[0]][to_pos[1]] - world[from_pos[0]][from_pos[1]]) <= 1


def bfs(world, end, queue):
    visited = set()
    while len(queue) > 0:
        pos, s = queue.pop(0)
        if pos == end:
            return s
        if pos in visited:
            continue
        visited.add(pos)
        for to_pos in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
            if can_step(world, pos, to_pos):
                queue.append((to_pos, s + 1))
    return None


def first_problem_solution():
    world, start, end = generate_world()
    return bfs(world, end, [(start, 0)])


def second_problem_solution():
    world, _, end = generate_world()
    starts = []
    for i, row in enumerate(world):
        for j, letter in enumerate(row):
            if letter == ord('a'):
                starts.append((i, j))
    return min([v for start in starts if (v := bfs(world, end, [(start, 0)])) is not None])


def main():
    print(f'Solution to first problem is {first_problem_solution()}')  # 449
    print(f'Solution to second problem is {second_problem_solution()}')  # 443
