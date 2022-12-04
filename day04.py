from utils import get_input
import numpy as np

def part1(data):
    c = 0
    for e1, e2 in data:
        e1_c_e2 = (int(e1[0])<=int(e2[0]) and int(e1[1])>=int(e2[1]))
        e2_c_e1 = (int(e2[0])<=int(e1[0]) and int(e2[1])>=int(e1[1]))
        if e1_c_e2 or e2_c_e1: c+=1
    return c

def part2(data):
    c = 0
    for e1, e2 in data:
        if not (int(e1[1])<int(e2[0]) or int(e2[1])<int(e1[0])): c+=1
    return c


if __name__ == "__main__":
    day = 4
    data = get_input(day)
    data = [(pair[0].split("-"),pair[1].split("-")) for pair in 
            [row.split(',') for row in data]]
    print(part1(data.copy()))
    print(part2(data.copy()))

