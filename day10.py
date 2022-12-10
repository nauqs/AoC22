from utils import get_input
import numpy as np

def part1(data):
    return (np.concatenate([np.array([x,0]) if x!=0 else np.array([x]) for x in data]).cumsum()[np.arange(20,221,40)-1]*[np.arange(20,221,40)]).sum()

def part2(data):
    X = np.concatenate([np.array([x,0]) if x!=0 else np.array([x]) for x in data]).cumsum()
    return ["".join(x.astype(str)) for x in np.array(["#" if p else "." for p in ((np.abs(X[:-2]-np.arange(240)%40))<=1)]).reshape(6,40)]

if __name__ == "__main__":
    day = 10
    data = get_input(day)
    data = np.array([1]+[int(l.split()[-1]) if len(l.split())==2 else 0 for l in data])
    print(part1(data))
    print(part2(data))