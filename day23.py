from utils import get_input
from collections import defaultdict
import numpy as np

d = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
d_steps = [[(-1,0),(-1,1),(-1,-1)], [(1,0),(1,1),(1,-1)], [(0,-1),(-1,-1),(1,-1)], [(0,1),(1,1),(-1,1)]]

def part1(data):
    elves = read_elves(data)
    for n in range(10):
        elves, _ = simulate_round(elves.copy(), n)
    elf_array = np.array(elves)
    return (elf_array[:,0].max()-elf_array[:,0].min()+1)*(elf_array[:,1].max()-elf_array[:,1].min()+1)-len(elves)

def part2(data):
    elves = read_elves(data)
    n, moved = 0, True
    while moved:
        elves, moved = simulate_round(elves, n)
        n += 1
    return n

def read_elves(data):
    return list(zip(*np.where(np.array([list(x) for x in data]) == "#")))

def simulate_round(elves, n):

    positions, props, new_elves = defaultdict(lambda: False), defaultdict(list), []
    moved = False

    for elf in elves:
        positions[elf] = True

    for elf in elves:
        neighbors, i = False, 0
        while not neighbors and i<=7:
            neighbors = positions[(elf[0]+d[i][0],elf[1]+d[i][1])]
            i += 1
        if not neighbors:
            new_elves.append(elf)
        else:
            proposed = False
            for dirs in range(4):
                adjacent = False
                for j in range(3):
                    step = d_steps[(dirs+n)%4][j]
                    adjacent = positions[(elf[0]+step[0],elf[1]+step[1])]
                    if adjacent: break
                if not adjacent:
                    proposed = True
                    step = d_steps[(dirs+n)%4][0]
                    props[(elf[0]+step[0],elf[1]+step[1])].append((elf[0],elf[1]))
                    break
            if not proposed: new_elves.append(elf)

    for prop in props:
        if len(props[prop])==1:
            moved = True
            new_elves.append(prop)
        else:
            for e in props[prop]:
                new_elves.append(e)

    return new_elves, moved


if __name__ == "__main__":
    day = 23
    data = get_input(day)
    print(part1(data))
    print(part2(data))
