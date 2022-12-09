from utils import get_input
import numpy as np

dirs = {"R": np.array([0,1]), "L": np.array([0,-1]), "U": np.array([1,0]),  "D": np.array([-1,0])}

def part1(data):
    h, t, visited = np.array([0,0]), np.array([0,0]), set()
    for d, n in data:
        for i in range(int(n)):
            h += dirs[d]
            t += np.sign(h-t)*(np.max(np.abs(h-t))>1)
            visited.add((t[0],t[1]))
    return len(visited)

def part2(data):
    knots, visited = np.array([np.array([0,0]) for _ in range(10)]), set()
    for d, n in data:
        for i in range(int(n)):
            knots[0] += dirs[d]
            for k in range(1,10):
                if np.max(np.abs(knots[k]-knots[k-1]))>1: 
                    knots[k] += np.sign(knots[k-1]-knots[k])
            visited.add((knots[-1][0],knots[-1][1]))
    return len(visited)

if __name__ == "__main__":
    day = 9
    data = [r.split() for r in get_input(day)]
    print(part1(data))
    print(part2(data))