from utils import get_input
from collections import deque

def mix(d, original_d):
    for i, el in original_d:
        d.rotate(-d.index((i,el)))
        d.rotate(-d.popleft()[1])
        d.appendleft((i,el))
    return d

def get_sum(d, idx0):
    d.rotate(-idx0)
    s = 0
    for _ in range(3):
        d.rotate(-1000)
        s += d[0][1]
    return s

def part1(data):
    d = mix(deque(enumerate(data)), deque(enumerate(data))) # save original indices, as values not unique in input
    return get_sum(d, d.index((data.index(0), 0))) # assume 0 is unique tho...

def part2(data, key):
    d2 = deque([(i,el*key) for i, el in enumerate(data)]) 
    for _ in range(10):
        d2 = mix(d2, deque([(i,el*key) for i, el in enumerate(data)]))
    return get_sum(d2, d2.index((data.index(0), 0)))

if __name__ == "__main__":
    day = 20
    data = get_input(day)
    data = list(map(int, data))
    print(part1(data))
    print(part2(data, key=811589153))
