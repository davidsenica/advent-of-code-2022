import re

FILE = 'data/day11.txt'


class Monkey:
    def __init__(self, items, op, test, true_monkey, false_monkey):
        self.items = items
        self.op = lambda old: eval(op)
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspected_items = 0

    def get_next_item(self):
        self.inspected_items += 1
        return self.items.pop(0)


def parse_input():
    monkeys = []
    with open(FILE) as f:
        input_data = f.read().split('\n\n')
        for i in input_data:
            regex = re.compile('Monkey (\d):\s+Starting items: (.*)\s+Operation: new = (.*)\s+Test: divisible by (.*)\s+If true: throw to monkey (\d)\s+If false: throw to monkey (\d)')
            match = regex.match(i)
            items = list(map(lambda x: int(x), match.group(2).split(', ')))
            monkeys.append(Monkey(items, match.group(3), int(match.group(4)), int(match.group(5)), int(match.group(6))))
    return monkeys


def solution(monkeys, steps, modulo=None):
    for _ in range(steps):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.get_next_item()
                worry = monkey.op(item)
                if modulo is None:
                    worry = worry // 3
                else:
                    worry = worry % modulo
                if worry % monkey.test == 0:
                    monkeys[monkey.true_monkey].items.append(worry)
                else:
                    monkeys[monkey.false_monkey].items.append(worry)
    sorted_scores = list(
        map(lambda x: x.inspected_items, sorted(monkeys, key=lambda x: x.inspected_items, reverse=True)))
    return sorted_scores[0] * sorted_scores[1]


def first_problem_solution():
    monkeys = parse_input()
    return solution(monkeys, 20, None)


def second_problem_solution():
    monkeys = parse_input()
    common_modulo = 1
    for m in monkeys:
        common_modulo *= m.test
    return solution(monkeys, 10000, common_modulo)


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
