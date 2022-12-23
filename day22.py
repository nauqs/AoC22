from utils import get_input
import numpy as np
import re

symbols = {0:">", 1:"v", 2:"<", 3:"^"}

def part1(grid, row_limits, col_limits, instructions):
    p = np.array([0, row_limits[0][0]])
    d = np.array([0,1])
    for ins in instructions:
        if ins.isnumeric():
            for i in range(int(ins)):
                new_p = p+d
                if d[0] == 0:
                    if new_p[1] > row_limits[new_p[0]][1]: new_p[1] = row_limits[new_p[0]][0]
                    elif new_p[1] < row_limits[new_p[0]][0]: new_p[1] = row_limits[new_p[0]][1]
                else:
                    if new_p[0] > col_limits[new_p[1]][1]: new_p[0] = col_limits[new_p[1]][0]
                    elif new_p[0] < col_limits[new_p[1]][0]:  new_p[0] = col_limits[new_p[1]][1]
                if grid[new_p[0],new_p[1]] == "#": break
                p = new_p
                grid[p[0],p[1]] =  symbols[abs(d[0])*(2-d[0]) + abs(d[1])*(1-d[1])]
        else:
            if ins=="R": d = rot90(d,-1)
            else: d = rot90(d, 1)
            grid[p[0],p[1]] =  symbols[abs(d[0])*(2-d[0]) + abs(d[1])*(1-d[1])]

    return 1000*(p[0]+1) + 4*(p[1]+1) + abs(d[0])*(2-d[0]) + abs(d[1])*(1-d[1])

def part2(grid, row_limits, col_limits, instructions):
    p = np.array([0, row_limits[0][0]])
    d = np.array([0,1])
    L = 50
    for ins in instructions:
        if ins.isnumeric():
            for i in range(int(ins)):
                new_p = p+d
                new_d = d
                # HARDCODED MAPPINGS FOR MY INPUT...
                if d[1] == 1:
                    if new_p[1] > row_limits[new_p[0]][1]:
                        if new_p[0]<L: 
                            new_p = wrap(p,np.array([0,149]), np.array([49,149]),np.array([149,99]), np.array([100,99]))
                            new_d = np.array([0,-1])
                        elif new_p[0]<2*L: 
                            new_p = wrap(p, np.array([50,99]), np.array([99,99]), np.array([49,100]), np.array([49,149]))
                            new_d = np.array([-1,0])
                        elif new_p[0]<3*L:
                            new_p = wrap(p, np.array([100,99]), np.array([149,99]), np.array([49,149]), np.array([0,149]))
                            new_d = np.array([0,-1])
                        else:
                            new_p = wrap(p, np.array([150,49]), np.array([199,49]), np.array([149,50]), np.array([149,99]))
                            new_d = np.array([-1,0])
                elif d[1] == -1:
                    if new_p[1] < row_limits[new_p[0]][0]: 
                        if new_p[0]<L:
                            new_p = wrap(p, np.array([0,50]), np.array([49,50]), np.array([149,0]), np.array([100,0]))
                            new_d = np.array([0,1])
                        elif new_p[0]<2*L:
                            new_p = wrap(p, np.array([50,50]), np.array([99,50]), np.array([100,0]), np.array([100,49]))
                            new_d = np.array([1,0])
                        elif new_p[0]<3*L: 
                            new_p = wrap(p, np.array([100,0]), np.array([149,0]), np.array([49,50]), np.array([0,50]))
                            new_d = np.array([0,1])
                        else:
                            new_p = wrap(p, np.array([150,0]), np.array([199,0]), np.array([0,50]), np.array([0,99]))
                            new_d = np.array([1,0])
                elif d[0] == 1:
                    if new_p[0] > col_limits[new_p[1]][1]:
                        if new_p[1]<L: 
                            new_p = wrap(p, np.array([199,0]), np.array([199,49]), np.array([0,100]), np.array([0,149]))
                            new_d = np.array([1,0])
                        elif new_p[1]<2*L: 
                            new_p = wrap(p, np.array([149,50]), np.array([149,99]), np.array([150,49]), np.array([199,49]))
                            new_d = np.array([0,-1])
                        else:
                            new_p = wrap(p, np.array([49,100]), np.array([49,149]), np.array([50,99]), np.array([99,99]))
                            new_d = np.array([0,-1])
                elif d[0] == -1:
                    if new_p[0] < col_limits[new_p[1]][0]:  
                        if new_p[1]<L: 
                            new_p = wrap(p, np.array([100,0]), np.array([100,49]), np.array([50,50]), np.array([99,50]))
                            new_d = np.array([0,1])
                        elif new_p[1]<2*L: 
                            new_p = wrap(p, np.array([0,50]), np.array([0,99]), np.array([150,0]), np.array([199,0]))
                            new_d = np.array([0,1])
                        else:
                            new_p = wrap(p, np.array([0,100]), np.array([0,149]), np.array([199,0]), np.array([199,49]))
                            new_d = np.array([-1,0])
                if grid[new_p[0],new_p[1]] == "#": break
                p = new_p
                d = new_d
                #grid[p[0],p[1]] =  symbols[abs(d[0])*(2-d[0]) + abs(d[1])*(1-d[1])]
        else:
            if ins=="R": d = rot90(d,-1)
            else: d = rot90(d, 1)
            #grid[p[0],p[1]] =  symbols[abs(d[0])*(2-d[0]) + abs(d[1])*(1-d[1])]

    return 1000*(p[0]+1) + 4*(p[1]+1) + abs(d[0])*(2-d[0]) + abs(d[1])*(1-d[1])

def parse_input(data):
    i = data.index("")
    grid, instructions = data[:i], data[i+1:]
    max_len = max([len(list(x)) for x in grid])
    grid = np.array([list(x)+[' ' for _ in range(max_len-len(x))] for x in grid])
    row_limits = [(np.min(np.where(x)), np.max(np.where(x))) for x in grid]
    col_limits = [(np.min(np.where(x)), np.max(np.where(x))) for x in grid.T]
    instructions = re.split('(L|R)',"".join(instructions))
    return grid, row_limits, col_limits, instructions

def rot90(v, k=1):
    rot = np.array([[np.cos(k*np.pi/2.), -np.sin(k*np.pi/2.)], 
        [np.sin(k*np.pi/2.), np.cos(k*np.pi/2.)]])
    return np.dot(rot, v).astype(int)

def wrap(p, p_0, p_1, q_0, q_1):
    q_diff, p_diff = q_1 - q_0, p_1 - p_0
    if np.abs(q_diff[0]) == np.abs(p_diff[0]):
        o = q_diff / (np.maximum((p_diff),1))
        q = (p - p_0) * o + q_0
    else:
        o = q_diff / (np.maximum((p_diff[::-1]),1))
        q = (p[::-1] - p_0[::-1]) * o + q_0
    return q.astype(int)
        

if __name__ == "__main__":
    day = 22
    data = get_input(day, splitlines=False).splitlines()
    grid, row_limits, col_limits, instructions = parse_input(data)
    print(part1(grid, row_limits, col_limits, instructions))
    print(part2(grid, row_limits, col_limits, instructions))

