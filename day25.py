from utils import get_input
import numpy as np

d = {"2": 2, "1": 1, "0": 0, "-":-1, "=":-2}
dr = {v: k for k, v in d.items()}
B = 5

def part1(data):
    s = sum([sum([d[digit] * B**(len(num)-(i+1)) for i, digit in enumerate(num)]) for num in data])
    m = round(np.log(s)/np.log(B))
    SNAFU = [0 for m in range(m+1)] 
    while m>=0:
        SNAFU[m] = s//B**m
        s -= (s//B**m)*B**m
        if SNAFU[m]>=3: SNAFU[m]-=B; SNAFU[m+1]+=1
        m -= 1
    for i in range(len(SNAFU)):
        if SNAFU[i]>=3: SNAFU[i]-=B; SNAFU[i+1]+=1
    return "".join([dr[x] for x in reversed(SNAFU)])

def part2(data):
    return "Start the blender!"

if __name__ == "__main__":
    day = 25
    data = get_input(day)
    print(part1(data))
    print(part2(data))
