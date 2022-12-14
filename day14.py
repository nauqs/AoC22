from utils import get_input
import numpy as np

dirs = {'D': np.array([1,0]),
        'L': np.array([1,-1]),
        'R': np.array([1,1])}

def parse_grid(data, floor):

    grid = np.zeros((200,400))
    max_depth = 0

    for line in data:
        points = line.split(' -> ')
        for i in range(len(points)-1):
            y0, x0 = (points[i].split(','))
            yc0, xc0 = int(y0)-300, int(x0)
            
            y1, x1 = (points[i+1].split(','))
            yc1, xc1 = int(y1)-300, int(x1)

            max_depth = max(max_depth, xc1)
            
            if xc0==xc1: 
                grid[xc0,min(yc0,yc1):max(yc0,yc1)+1] = 1
            elif yc0==yc1: 
                grid[min(xc0,xc1):max(xc0,xc1)+1,yc0] = 1

    if floor: grid[max_depth+2,:] = 1

    return grid, max_depth


def part1(data):
    grid, max_depth = parse_grid(data, floor=False)
    sand, c = True, 0
    while sand:
        sp = np.array([0,200])
        c += 1
        while True:
            if grid[(sp+dirs['D'])[0],(sp+dirs['D'])[1]] == 0: sp += dirs['D']
            elif grid[(sp+dirs['L'])[0],(sp+dirs['L'])[1]] == 0: sp += dirs['L']
            elif grid[(sp+dirs['R'])[0],(sp+dirs['R'])[1]] == 0: sp += dirs['R']
            else:
                grid[sp[0],sp[1]] = 2
                break
            if sp[0] > max_depth:
                sand = False
                break
    return c-1

def part2(data):
    grid, max_depth = parse_grid(data, floor=True)
    sand, c = True, 0
    while sand:
        sp = np.array([0,200])
        c += 1
        while True:
            if grid[(sp+dirs['D'])[0],(sp+dirs['D'])[1]] == 0: sp += dirs['D']
            elif grid[(sp+dirs['L'])[0],(sp+dirs['L'])[1]] == 0: sp += dirs['L']
            elif grid[(sp+dirs['R'])[0],(sp+dirs['R'])[1]] == 0: sp += dirs['R']
            else:
                grid[sp[0],sp[1]] = 2
                break
        if sp[0] == 0:
            sand = False
            break
    return c

if __name__ == "__main__":
    day = 14
    data = get_input(day)
    print(part1(data))
    print(part2(data))
