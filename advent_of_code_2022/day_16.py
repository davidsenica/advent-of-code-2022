import math
from collections import defaultdict
from itertools import combinations

from advent_of_code_2022.utils import line_iterator
import re

FILE = 'data/day16.txt'


class Valve:
    def __init__(self, id, name, flow, tunnels):
        self.name = name
        self.id = id
        self.flow = flow
        self.tunnels = tunnels

    def update_tunnels(self, valves):
        tmp = []
        for t in self.tunnels:
            for v in valves:
                if v.name == t:
                    tmp.append(v)
                    break
        self.tunnels = tmp

    def __repr__(self):
        return f'{self.name}-[{self.flow}]'

    def __hash__(self):
        return hash(self.name)


def parse_input():
    regex = re.compile('Valve (\w\w) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)')
    valves = []
    best_valves = []
    start = None
    for i, line in enumerate(line_iterator(FILE)):
        (valve, flow, tunnels) = regex.findall(line)[0]
        valve = Valve(i, valve, int(flow), tunnels.split(', '))
        valves.append(valve)
    for v in valves:
        if v.name == 'AA':
            start = v
        v.update_tunnels(valves)
        if v.flow > 0:
            best_valves.append(v)
    distances = defaultdict(lambda: math.inf)
    for v1 in valves:
        distances[v1.id, v1.id] = 0
        for v2 in v1.tunnels:
            distances[v1.id, v2.id] = 1
    for k in range(len(valves)):
        for i in range(len(valves)):
            for j in range(len(valves)):
                distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])
    return valves, best_valves, distances, start


def search(distance, valves, current, opened, score, time):
    for v in valves:
        new_time = time - distance[current.id, v.id] - 1
        if new_time < 2 or v in opened:
            continue
        yield from search(distance, valves, v, opened.union({v}), score + new_time * v.flow, new_time)
    yield opened, score


def first_problem_solution():
    valves, best_valves, distances, start = parse_input()
    return max(map(lambda x: x[1], search(distances, best_valves, start, set(), 0, 30)))


def second_problem_solution():
    valves, best_valves, distances, start = parse_input()
    best_scores = defaultdict(int)
    for opened, score in search(distances, best_valves, start, set(), 0, 26):
        opened = frozenset(opened)
        if score > best_scores[opened]:
            best_scores[opened] = score
    return max(me_score + elephant_score for (me, me_score), (elephant, elephant_score) in combinations(best_scores.items(), 2) if not me & elephant)


def main():
    print(f'Solution to first problem is {first_problem_solution()}')  # 1488
    print(f'Solution to second problem is {second_problem_solution()}')  # 2111
