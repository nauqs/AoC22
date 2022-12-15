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
    # combine a list of ranges in a sorted, non-overlapping list (GPT helped haha)
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
        # for each sensor we store the size of the square it covers
        d[s] = np.sum(np.abs(np.array(s)-closest[s]))

    covered = []
    for s in d:
        s_pos = np.array(s)
        dist = np.abs(s_pos[1]-row)
        # for each sensor, we compute how far it is from the interest row
        # if the sensor covers the row, we compute which interval it covers
        if dist<d[s]:
            # => it covers an interval of range 2*(square_side-distance)
            covered.append((s_pos[0]-(d[s]-dist), s_pos[0]+(d[s]-dist)))

    return combine(covered)[1]

def part2(closest, y_min=0, y_max=20):
    d = {}
    for s in closest:
        d[s] = np.sum(np.abs(np.array(s)-closest[s]))

    # repeat part 1 for each distance
    for row in tqdm.tqdm(range(y_min,y_max)):
        covered = []
        for s in d:
            s_pos = np.array(s)
            dist = np.abs(s_pos[1]-row)
            if dist<d[s]:
                covered.append((s_pos[0]-(d[s]-dist), s_pos[0]+(d[s]-dist)))
        res, s = combine(covered, x_min=y_min, x_max=y_max)
        # if the covered interval s is not exactly y_max-y_min WE FOUND IT!
        if y_max-y_min!=s:
            # res = [(y_min, y_beacon-1), (y_beacon+1, y_max)]
            y_beacon = (res[0][1]+1)
            return y_beacon*4000000 + row

if __name__ == "__main__":
    day = 15
    data = get_input(day)
    print(part1(parse_input(data), row=2000000))
    print(part2(parse_input(data), y_min=0, y_max=4000000))

