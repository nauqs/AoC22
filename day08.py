from utils import get_input
import numpy as np

def part1(data):
    n, m = data.shape
    vis_map = np.zeros((n,m))
    # horizontal
    for rng in [((0,n),(0,m)),((n-1,0,-1),(m-1,0,-1))]:
        for i in range(*rng[0]):
            visible = -1
            for j in range(*rng[1]):
                if data[i][j] > visible:
                    visible = data[i][j]
                    vis_map[i][j] += 1
    # vertical
    for rng in [((0,m),(0,n)),((m-1,0,-1),(n-1,0,-1))]:
        for j in range(*rng[0]):
            visible = -1
            for i in range(*rng[1]):
                if data[i][j] > visible:
                    visible = data[i][j]
                    vis_map[i][j] += 1
    return np.sum(vis_map!=0)

def part2(data):
    n, m = data.shape
    max_score = 0
    for row in range(n):
        for col in range(m):
            score = 1
            # vertical
            for rng in [range(row-1, 0, -1), range(row+1,n)]:
                c = 1 
                for i in rng:
                    if data[i][col] >= data[row][col]: break
                    c += 1
                    if i == 0 or i==n-1: c-= 1
                score *= c 
            # horizontal
            for rng in [range(col+1, m), range(col-1, 0, -1)]:
                c = 1         
                for j in rng:
                    if data[row][j] >= data[row][col]: break
                    c += 1
                    if j==0 or j==m-1: c-= 1
                score *= c
            max_score = max(max_score, score)
    return max_score

if __name__ == "__main__":
    day = 8
    data = get_input(day)
    data = np.array([[int(t) for t in row] for row in data])
    print(part1(data))
    print(part2(data))