import sys
from advent_of_code_2022.day_1 import main as day_1
from advent_of_code_2022.day_2 import main as day_2
from advent_of_code_2022.day_3 import main as day_3
from advent_of_code_2022.day_4 import main as day_4
from advent_of_code_2022.day_5 import main as day_5
from advent_of_code_2022.day_6 import main as day_6
from advent_of_code_2022.day_7 import main as day_7
from advent_of_code_2022.day_8 import main as day_8


if __name__ == '__main__':
    day = sys.argv[1]
    if day == 'day1':
        day_1()
    elif day == 'day2':
        day_2()
    elif day == 'day3':
        day_3()
    elif day == 'day4':
        day_4()
    elif day == 'day5':
        day_5()
    elif day == 'day6':
        day_6()
    elif day == 'day7':
        day_7()
    elif day == 'day8':
        day_8()
