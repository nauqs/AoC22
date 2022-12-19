from utils import get_input
import numpy as np

def part1(cubes):
    return sum([6-np.sum(np.sum(np.abs(cubes-cube), axis=1)==1) for cube in cubes])

def part2(cubes):
    return part1(np.array(cubes+interior_cubes(cubes)).astype(int))

def interior_cubes(cubes):
    mod_cubes = np.array(cubes).astype(int)+1
    queue = []
    visited = set()
    N = np.max(mod_cubes)+1

    start_cell = (0, 0, 0)
    queue.append(start_cell)
    visited.add(start_cell)

    while queue:
        x, y, z = queue.pop() 
        neighbors = []
        
        if x > 0 and np.min(np.sum(np.abs(np.array([x-1,y,z])-mod_cubes),axis=1))!=0: 
            neighbors.append((x-1, y, z))
        if x < N and np.min(np.sum(np.abs(np.array([x+1,y,z])-mod_cubes),axis=1))!=0: 
            neighbors.append((x+1, y, z))
        if y > 0 and np.min(np.sum(np.abs(np.array([x,y-1,z])-mod_cubes),axis=1))!=0: 
            neighbors.append((x, y-1, z))
        if y < N and np.min(np.sum(np.abs(np.array([x,y+1,z])-mod_cubes),axis=1))!=0: 
            neighbors.append((x, y+1, z))
        if z > 0 and np.min(np.sum(np.abs(np.array([x,y,z-1])-mod_cubes),axis=1))!=0: 
            neighbors.append((x, y, z-1))
        if z < N and np.min(np.sum(np.abs(np.array([x,y,z+1])-mod_cubes),axis=1))!=0: 
            neighbors.append((x, y, z+1))

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    points = set([(x, y, z) for x in range(N) for y in range(N) for z in range(N)])
    visited = {(x-1,y-1,z-1) for (x,y,z) in visited}
    return list(points-visited-{(int(x), int(y), int(z)) for (x,y,z) in cubes})

if __name__ == "__main__":
    day = 18
    data = get_input(day)
    data = [l.split(',') for l in data]
    print(part1(np.array(data).astype(int)))
    print(part2(data))
