from utils import get_input
import numpy as np
from collections import defaultdict

dirs = [np.array(x) for x in [(0,-1),(-1,0),(0,0),(1,0),(0,1)]]

def part1(data):
    grid = np.array([list(x) for x in data])
    m, n = grid.shape
    blizzards = [get_blizzards(grid)]
    grids = [grid]
    start, end = np.array((0,1)), np.array((m-1,n-2))
    return find_path(grid, start, end, grids, blizzards, m, n)[0]

def find_path(grid, start, end, grids, blizzards, m, n, start_time=0):

    possible_paths = [(np.array(start),start_time)]
    best_time = np.inf
    visited = defaultdict(list)

    while possible_paths:
        p, time = possible_paths.pop(0)
        if time + 1 >= len(grids):
            new_blizzards = advance_blizzards(blizzards[-1].copy(), m, n)
            blizzards.append(new_blizzards)
            grids.append(fill_grid(grid.copy(), new_blizzards))

        if np.all((p-end)==0):
            best_time = min(best_time, time)
            continue

        if np.sum(np.abs(p-end))+time+1 >= best_time:
            continue

        for d in dirs:
            new_p = p + d
            if new_p[0]>=m or new_p[1]>=n or new_p[0]<0 or new_p[1]<0: continue
            if grids[time+1][new_p[0],new_p[1]]=='.':
                if (new_p[0],new_p[1]) not in visited[time+1]:
                    possible_paths.append((new_p, time+1))
                    visited[time+1].append((new_p[0],new_p[1]))

    return best_time, grids, blizzards 

def fill_grid(grid, new_blizzards):
    for i in range(1,grid.shape[0]-1):
        for j in range(1,grid.shape[1]-1):
            grid[i,j] = "." 
    for b in new_blizzards:
        grid[b[1],b[2]] = b[0]
    return grid

def advance_blizzards(blizzards, m, n):
    for i in range(len(blizzards)):
        if blizzards[i][0] == ">":
            blizzards[i][2] += 1
            if blizzards[i][2] >= n-1: blizzards[i][2] = 1
        elif blizzards[i][0] == "<":
            blizzards[i][2] -= 1
            if blizzards[i][2] <= 0: blizzards[i][2] = n-2
        elif blizzards[i][0] == "v":
            blizzards[i][1] += 1
            if blizzards[i][1] >= m-1: blizzards[i][1] = 1
        elif blizzards[i][0] == "^":
            blizzards[i][1] -= 1
            if blizzards[i][1] <= 0: blizzards[i][1] = m-2
    return blizzards

def get_blizzards(grid):
    blizzards = [] 
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] in ["^",">","v","<"]:
                blizzards.append([grid[i,j], i, j])
    return blizzards

def part2(data):
    grid = np.array([list(x) for x in data])
    m, n = grid.shape
    blizzards = [get_blizzards(grid)]
    grids = [grid]
    start, end = np.array((0,1)), np.array((m-1,n-2))
    total_time, grids, blizzards = find_path(grid, start, end, grids.copy(), blizzards.copy(), m, n)
    total_time, grids, blizzards = find_path(grid, end, start, grids.copy(), blizzards.copy(), m, n, 
                                    start_time=total_time)
    return find_path(grid, start, end, grids.copy(), blizzards.copy(), m, n, 
                                    start_time=total_time)[0]

if __name__ == "__main__":
    day = 24
    data = get_input(day)
    print(part1(data))
    print(part2(data))
