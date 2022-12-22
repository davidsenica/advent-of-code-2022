from advent_of_code_2022.utils import line_iterator, to_int
import re
import sys

sys.setrecursionlimit(150000)

FILE = 'data/day19.txt'


def parse_input():
    regex = re.compile('(\d+)')
    blueprints = {}
    for line in line_iterator(FILE):
        blueprint_id, ore_robot_ore, clay_robot_ore, obsidian_robot_ore, obsidian_robot_clay, geode_robot_ore, geode_robot_obsidian = to_int(regex.findall(line))
        blueprints[blueprint_id] = ((ore_robot_ore, 0, 0, 0), (clay_robot_ore, 0, 0, 0), (obsidian_robot_ore, obsidian_robot_clay, 0, 0), (geode_robot_ore, 0, geode_robot_obsidian, 0))
    return blueprints


def make_robot(blueprint, robot, robots, minerals):
    if robot is None:
        return robots, minerals
    if all(r <= m for r, m in zip(blueprint[robot], minerals)):
        return tuple(robots[i] if i != robot else robots[i] + 1 for i in range(len(robots))), tuple(m - r for r, m in zip(blueprint[robot], minerals))
    else:
        return robots, minerals


def collect_ore(robots, minerals):
    return tuple(r+m for r, m in zip(robots, minerals))


def generate_actions(blueprint, minerals):
    actions = []
    for robot in [3, 2, 1, 0]:
        if all([r <= m for r, m in zip(blueprint[robot], minerals)]):
            actions.append(robot)
    return actions


def search(blueprint, time):
    score = 0
    start = ((1, 0, 0, 0), (0, 0, 0, 0), time)
    queue = [start]
    seen = set()

    max_ore_per_min = max(r[0] for r in blueprint)
    max_clay_per_min = max(r[1] for r in blueprint)
    max_obsidian_per_min = max(r[2] for r in blueprint)

    while queue:
        robots, minerals, minutes = queue.pop(0)
        score = max(score, minerals[3])
        if minutes == 0:
            continue
        ore_robot, clay_robot, obsidian_robot, geode_robot = robots
        # disregard exses robots
        if ore_robot > max_ore_per_min:
            ore_robot = max_ore_per_min
        if clay_robot > max_clay_per_min:
            clay_robot = clay_robot
        if obsidian_robot > max_obsidian_per_min:
            obsidian_robot = obsidian_robot
        ore, clay, obsidian, geode = minerals
        if ore >= minutes * max_ore_per_min - ore_robot * (minutes - 1):
            ore = minutes * max_ore_per_min - ore_robot * (minutes - 1)
        if clay >= minutes * max_clay_per_min - clay_robot * (minutes - 1):
            clay = minutes * max_obsidian_per_min - obsidian_robot * (minutes - 1)
        if obsidian >= minutes * max_obsidian_per_min - obsidian_robot * (minutes - 1):
            obsidian = minutes * max_obsidian_per_min - obsidian_robot * (minutes - 1)

        robots = (ore_robot, clay_robot, obsidian_robot, geode_robot)
        minerals = (ore, clay, obsidian, geode)
        if (robots, minerals, minutes) in seen:
            continue
        seen.add((robots, minerals, minutes))

        if all(r <= m for r, m in zip(blueprint[3], minerals)):
            new_robots, new_minerals = make_robot(blueprint, 3, robots, minerals)
            new_minerals = collect_ore(robots, new_minerals)
            queue.append((new_robots, new_minerals, minutes - 1))
        else:
            queue.append((robots, collect_ore(robots, minerals), minutes - 1))
            for action in generate_actions(blueprint, minerals):
                new_robots, new_minerals = make_robot(blueprint, action, robots, minerals)
                new_minerals = collect_ore(robots, new_minerals)
                queue.append((new_robots, new_minerals, minutes - 1))
    return score


def first_problem_solution():
    blueprints = parse_input()
    score = 0
    for blueprint_id, blueprint in blueprints.items():
        max_amount = search(blueprint, 24)
        score += blueprint_id * max_amount
    return score


def second_problem_solution():
    blueprints = parse_input()
    score = 1
    for blueprint_id in [1, 2, 3]:
        max_amount = search(blueprints[blueprint_id], 32)
        score *= max_amount
    return score


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 600
    print(f'Solution to second problem is {second_problem_solution()}') # 6000


