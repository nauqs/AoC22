from utils import get_input
from collections import defaultdict
import numpy as np

"""
This would work if no dirs like "fct/fct" lol
"""
def create_tree(data):
    children, parent, files = defaultdict(list), defaultdict(str), defaultdict(int)
    current_dir = "/"

    for line in data:
        line = line.split()
        if line[0]=="$": # inst
            if line[1] == "cd": 
                if line[2] == "..": 
                    current_dir = parent[current_dir]
                else: 
                    current_dir = line[2]
        else: # dir or file
            if line[0] == "dir":
                children[current_dir].append(line[1])
                parent[line[1]] = current_dir
            else: files[current_dir] += int(line[0])
                
    return children, parent, files

"""
updated version xd
"""
def compute_sizes(data):
    
    sizes = defaultdict(int)
    current_dir = []

    for line in data:
        line = line.split()
        if line[0] == "$": # instruction
            if line[1] == "cd":
                if line[2] == "..": # back
                    current_dir.pop()
                else:
                    current_dir.append(line[2])
        else:
            if line[0] != "dir":
                current_parent = current_dir.copy()
                while current_parent != ["/"]:
                    sizes["/".join(current_parent[1:])] += int(line[0])
                    current_parent.pop()
                sizes["/"] += int(line[0])

    return sizes

def part1(data):
    sizes = np.array(list(compute_sizes(data).values()))
    return np.sum(sizes*(sizes<=100000))

def part2(data):
    sizes = np.array(list(compute_sizes(data).values()))
    needed_space = 30000000 - (70000000 - np.max(sizes))
    return np.min(sizes[sizes-needed_space>=0])

if __name__ == "__main__":
    day = 7
    data = get_input(day)
    print(part1(data))
    print(part2(data))

