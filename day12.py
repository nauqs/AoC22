from utils import get_input
from collections import defaultdict
from copy import copy

def get_graph(data):
    graph = defaultdict(list)
    n,m = len(data), len(data[0])
    for i in range(n):
        for j in range(m):
            n_val = data[i][j]
            node = f"{i},{j},{n_val}"
            if n_val == "S": start = node
            elif n_val == "E": end = node
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                if (i+d[0] in range(0,n)) and (j+d[1] in range(0,m)):
                    pos_n = data[i+d[0]][j+d[1]]
                    neighbors =  (((ord(pos_n)-ord(n_val))<=1) and pos_n!="E") or \
                        (n_val=="S" and pos_n in ["a","b"]) or\
                        (pos_n=="E" and n_val in ["y","z"])
                    if neighbors:
                        graph[node].append(f"{i+d[0]},{j+d[1]},{pos_n}")
    return graph, start, end

def part1(graph, start, end):
    queue, visited = [[start]], []
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour[-1] == end[-1]: 
                    return len(new_path)-1 
    # return big distance if path not found (for part 2)
    return 100000           

def part2(graph, start, end):
    min_dist = 10000
    for node in graph:
        if node[-1] =="a":
            min_dist = min(min_dist, part1(copy(graph), node, end))
    return min_dist

if __name__ == "__main__":
    day = 12
    data = get_input(day)
    print(part1(*get_graph(data)))
    print(part2(*get_graph(data)))

