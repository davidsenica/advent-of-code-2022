from copy import deepcopy

from advent_of_code_2022.utils import line_iterator, to_int

FILE = 'data/day21.txt'

class Node:
    def __init__(self):
        self.value = None
        self.operation = None


def parse_input():
    nodes = {}
    for line in line_iterator(FILE):
        node = Node()
        try:
            node.value = int(line[6:])
        except:
            node.operation = line[6:].split(' ')
        nodes[line[:4]] = node
    return nodes


def evaluate(node_name, nodes):
    node = nodes[node_name]
    if node.value is not None:
        return node.value
    n1 = evaluate(node.operation[0], nodes)
    n2 = evaluate(node.operation[-1], nodes)
    return int(eval(f'{n1} {node.operation[1]} {n2}'))


def bisection(nodes, a, b):
    m = (a + b) // 2

    nodes['humn'].value = a
    a_v = evaluate('root', nodes)
    nodes['humn'].value = b
    b_v = evaluate('root', nodes)
    nodes['humn'].value = m
    m_v = evaluate('root', nodes)

    if a_v == 0:
        return a

    if b_v == 0:
        return b

    if a_v * m_v >= 0:
        return bisection(nodes, m, b)
    else:
        return bisection(nodes, a, m)


def first_problem_solution():
    nodes = parse_input()
    return evaluate('root', nodes)


def second_problem_solution():
    nodes = parse_input()
    nodes['root'].operation = [nodes['root'].operation[0], '-', nodes['root'].operation[-1]]
    a = -10000000000000
    b = 10000000000000
    return bisection(nodes, a, b) - 1


def main():
    print(f'Solution to first problem is {first_problem_solution()}') # 21120928600114
    print(f'Solution to second problem is {second_problem_solution()}') # 3453748220116

