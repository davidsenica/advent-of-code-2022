from advent_of_code_2022.utils import line_iterator, Point
import re

FILE = 'data/day15.txt'


def manhattan_distance(first, second):
    return abs(first.x - second.x) + abs(first.y - second.y)


class Pair:
    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon
        self.distance = manhattan_distance(sensor, beacon)


def first_problem_solution():
    visited_x = set()
    beacons_x = set()
    y = 2000000
    for line in line_iterator(FILE):
        coordinates = list(map(int, re.findall(r"-?\d+", line)))
        beacon = Point(coordinates[2], coordinates[3])
        pair = Pair(Point(coordinates[0], coordinates[1]), beacon)
        if beacon.y == y:
            beacons_x.add(beacon.x)
        dist = pair.distance - abs(pair.sensor.y - y)
        if dist < 0:
            continue
        visited_x = visited_x.union(set(range(pair.sensor.x - dist, pair.sensor.x + dist + 1)))
    return len(visited_x - beacons_x)


def second_problem_solution():
    pairs = []
    for line in line_iterator(FILE):
        coordinates = list(map(int, re.findall(r"-?\d+", line)))
        pairs.append(Pair(Point(coordinates[0], coordinates[1]), Point(coordinates[2], coordinates[3])))
    for y in range(3000000, 4000000+1):
        intervals = []
        for pair in pairs:
            dist = pair.distance - abs(pair.sensor.y - y)
            if dist < 0:
                continue
            intervals.append((pair.sensor.x - dist, pair.sensor.x + dist))
        intervals.sort()
        lines = []
        start_x, end_x = intervals[0]
        for s_x, e_x in intervals[1:]:
            if s_x - 1 <= end_x:
                end_x = max(end_x, e_x)
            else:
                lines.append((start_x, end_x))
                start_x, end_x = s_x, e_x
        lines.append((start_x, end_x))

        if len(lines) != 1:
            (a, b), _ = lines
            x = b + 1
            return x * 4000000 + y


def main():
    print(f'Solution to first problem is {first_problem_solution()}')  # 5525847
    print(f'Solution to second problem is {second_problem_solution()}')  # 13340867187704
