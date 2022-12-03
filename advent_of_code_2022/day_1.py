from advent_of_code_2022.utils import line_iterator

FILE = 'data/day1.txt'


def get_calories():
    calories = []
    current_calories = 0
    for line in line_iterator(FILE):
        try:
            current_calories += int(line)
        except:
            calories.append(current_calories)
            current_calories = 0
    return sorted(calories, reverse=True)


def first_problem_solution():
    return get_calories()[0]


def second_problem_solution():
    return sum(get_calories()[:3])


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')
