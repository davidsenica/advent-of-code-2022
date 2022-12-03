from advent_of_code_2022.utils import line_iterator

FILE = 'data/day2.txt'

mappings = {
    'A': 0,  # rock
    'B': 1,  # paper
    'C': 2,  # scissors
    'Y': 'B',
    'X': 'A',
    'Z': 'C',
}


def first_problem_solution():
    score = 0
    for line in line_iterator(FILE):
        opp, me = line.split(' ')
        opp_score = mappings[opp]
        me_score = mappings[mappings[me]]
        if opp_score == me_score:
            score += 3 + me_score + 1
        elif ((opp_score + 1) % 3) == me_score:
            score += 6 + me_score + 1
        else:
            score += me_score + 1
    return score


def second_problem_solution():
    score = 0
    for line in line_iterator(FILE):
        opp, me = line.split(' ')
        opp_score = mappings[opp]
        if me == 'X':
            # lose
            score += ((opp_score + 2) % 3) + 1
        elif me == 'Y':
            # draw
            score += 3 + opp_score + 1
        else:
            score += 6 + ((opp_score + 1) % 3) + 1
    return score


def main():
    print(f'Solution to first problem is {first_problem_solution()}')
    print(f'Solution to second problem is {second_problem_solution()}')