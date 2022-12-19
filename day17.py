from utils import get_input
import numpy as np

shapes = [ np.array([(0,0),(0,1),(0,2),(0,3)]),
        np.array([(-1,0),(0,1),(-1,1),(-1,2),(-2,1)]),
        np.array([(0,0),(0,1),(0,2),(-1,2),(-2,2)]),
        np.array([(0,0),(-1,0),(-2,0),(-3,0)]),
        np.array([(0,0),(0,1),(-1,0),(-1,1)]) ]

d = {">": np.array([0,1]), "<": np.array([0,-1])}

def part1(data):
    depth = 5000
    grid = np.zeros((depth,9))
    grid[:,0] = 1
    grid[:,-1] = 1
    grid[-1,:] = 1
    max_pos = depth-1

    t = 0
    L = len(data)
    height = [0]
    #visited = set()
    for i in range(2022):
        rock_pos = shapes[i%5]+np.array([max_pos-4, 3])

        while True:
            rock_pos += d[data[t]]
            if not (grid[rock_pos[:,0], rock_pos[:,1]]==0).all():
                rock_pos -= d[data[t]]

            t = (t+1)%L
            rock_pos += np.array([1,0])
            if not (grid[rock_pos[:,0], rock_pos[:,1]]==0).all():
                rock_pos -= np.array([1,0])
                grid[rock_pos[:,0], rock_pos[:,1]]=1
                max_pos = min(max_pos,rock_pos[-1][0])
                break
        height.append(depth-max_pos-1)
        
    return height[-1]

def part2(data):
    depth = 50000
    grid = np.zeros((depth,9))
    grid[:,0] = 1
    grid[:,-1] = 1
    grid[-1,:] = 1
    max_pos = depth-1

    t = 0
    L = len(data)
    visited = []
    height = [0]
    prev_t = 0
    tracking = False
    t_start, i_start, h_increase_start, h_start = 0, 0, 0, 0
    N = 1000000000000

    for i in range(N):
        rock_pos = shapes[i%5]+np.array([max_pos-4, 3])

        while True:
            rock_pos += d[data[t]]
            if not (grid[rock_pos[:,0], rock_pos[:,1]]==0).all():
                rock_pos -= d[data[t]]
            t = (t+1)%L
            rock_pos += np.array([1,0])
            if not (grid[rock_pos[:,0], rock_pos[:,1]]==0).all():
                rock_pos -= np.array([1,0])
                grid[rock_pos[:,0], rock_pos[:,1]]=1
                max_pos = min(max_pos,rock_pos[-1][0])
                break

        height.append(depth-max_pos-1)
        h_increase = height[-1]-height[-2]
        
        if (t, i%5, h_increase) in visited and not tracking:
            t_start, i_start, h_increase_start = t, i, h_increase
            tracking = True
        elif (t_start, i_start%5, h_increase_start) == (t, i%5, h_increase):
            len_cycle = i-i_start
            h_increase_cycle = height[-1]-height[i_start+1]
            break

        visited.append((t, i%5, h_increase))

    return (N-i_start)//len_cycle*h_increase_cycle + height[i_start+(N-i_start)%len_cycle]

if __name__ == "__main__":
    day = 17
    data = get_input(day, splitlines=False).strip()
    print(part1(data))
    print(part2(data))
