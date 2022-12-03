import sys
from advent_of_code_2022.day_1 import main as day_1
from advent_of_code_2022.day_2 import main as day_2
from advent_of_code_2022.day_3 import main as day_3


if __name__ == '__main__':
    day = sys.argv[1]
    if day == 'day1':
        day_1()
    elif day == 'day2':
        day_2()
    elif day == 'day3':
        day_3()
