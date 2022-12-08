from advent_of_code_2022.utils import line_iterator
import numpy as np

FILE = 'data/day8.txt'


def grid():
    return [[int(num) for num in line] for line in line_iterator(FILE)]


def first_problem_solution():
    trees = np.array(grid())
    height, width = trees.shape
    score = 2 * height + 2 * width - 4
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            current, left, right, top, bottom = trees[i, j], trees[i, :j], trees[i, j+1:], trees[:i, j],trees[i+1:, j]
            if (current > left).all() or (current > right).all() or (current > top).all() or (current > bottom).all():
                score += 1
    return score


def second_problem_solution():
    trees = np.array(grid())
    height, width = trees.shape
    scores = []
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            score = 1
            current = trees[i, j]
            for arr in [trees[i, :j][::-1], trees[i, j + 1:], trees[:i, j][::-1], trees[i + 1:, j]]:
                arr_score = 0
                for a in arr:
                    arr_score += 1
                    if a >= current:
                        break
                score *= arr_score
            scores.append(score)
    return max(scores)


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
