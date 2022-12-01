from utils import get_input
import numpy as np

def part1(data):
    max_cal, current_cal = 0, 0
    for cal in data:
        if cal: current_cal += int(cal)
        else:
            max_cal = max(current_cal, max_cal)
            current_cal = 0
    return max_cal

def part2(data):
    cal_list, current_cal = [], 0
    for cal in data:
        if cal: current_cal += int(cal)
        else:
            cal_list.append(current_cal)
            current_cal = 0
    return np.sum(sorted(cal_list)[-3:])


if __name__ == "__main__":
    day = 1
    data = get_input(day)
    print(part1(data.copy()))
    print(part2(data.copy()))

