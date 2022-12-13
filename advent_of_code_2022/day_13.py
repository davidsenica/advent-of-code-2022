FILE = 'data/day13.txt'


def read_input():
    signal_pairs = []
    with open(FILE) as f:
        for pair in f.read().split('\n\n'):
            splited = pair.split('\n')
            signal_pairs.append((eval(splited[0]), eval(splited[1])))
    return signal_pairs


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left < right) - (left > right)
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            comparison = compare(left[i], right[i])
            if comparison != 0:
                return comparison
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    else:
        return compare([left], right)


def first_problem_solution():
    signal_pairs = read_input()
    score = 0
    for i, pair in enumerate(signal_pairs):
        if compare(pair[0], pair[1]) == 1:
            score += (i + 1)
    return score


def second_problem_solution():
    signals = [signal for signal_pair in read_input() for signal in signal_pair]
    c_2 = 0
    c_6 = 0
    for signal in signals:
        if compare(signal, [[2]]) == 1:
            c_2 += 1
        if compare(signal, [[6]]) == 1:
            c_6 += 1
    return c_2 * c_6


def main():
    print(f'Solution to first problem is {first_problem_solution()}')  # 6187
    print(f'Solution to second problem is {second_problem_solution()}')  # 23520
