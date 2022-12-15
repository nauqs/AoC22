from utils import get_input
import re
import numpy as np
import tqdm

def parse_input(data):
    closest = {}
    for line in data:
        lsp = re.split(',|=|:',line)
        closest[(int(lsp[1]),int(lsp[3]))] = np.array((int(lsp[5]),int(lsp[7])))
    return closest 

def combine(ranges, x_min=-999999999, x_max=999999999):
  ranges = sorted(ranges, key=lambda x: x[0])
  result = [ranges[0]]
  for start, end in ranges[1:]:
    last_start, last_end = result[-1]
    if start <= last_end + 1: result[-1] = (last_start, max(last_end, end))
    else: result.append((start, end))

  s = 0
  for rng in result:
    s += np.clip(rng[1], x_min, x_max)-np.clip(rng[0], x_min, x_max)

  return result, s


def part1(closest, row=10):
    d = {}
    for s in closest:
        d[s] = np.sum(np.abs(np.array(s)-closest[s]))

    covered = []
    for s in d:
        s_pos = np.array(s)
        dist = np.abs(s_pos[1]-row)
        if dist<d[s]:
            covered.append((s_pos[0]-(d[s]-dist), s_pos[0]+(d[s]-dist)))

    return combine(covered)[1]

def part2(closest, y_min=0, y_max=20):
    d = {}
    for s in closest:
        d[s] = np.sum(np.abs(np.array(s)-closest[s]))

    for row in tqdm.tqdm(range(y_min,y_max)):
        covered = []
        for s in d:
            s_pos = np.array(s)
            dist = np.abs(s_pos[1]-row)
            if dist<d[s]:
                covered.append((s_pos[0]-(d[s]-dist), s_pos[0]+(d[s]-dist)))
        res, s = combine(covered, x_min=y_min, x_max=y_max)
        if y_max-y_min!=s:
            return 4000000*(res[0][1]+1)+row

if __name__ == "__main__":
    day = 15
    data = get_input(day)
    print(part1(parse_input(data), row=2000000))
    print(part2(parse_input(data), y_min=0, y_max=4000000))

