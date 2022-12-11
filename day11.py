from utils import get_input
import numpy as np

def parse_monkeys(data):
    items, ops, test, throw = [], [], [], []
    for i in range(len(data)//7+1):
        items.append(list(map(int,data[7*i+1].split(":")[1].split(", "))))
        ops.append(data[7*i+2].split("= ")[1])
        test.append(int(data[7*i+3].split()[-1]))
        throw.append((int(data[7*i+4][-1]), int(data[7*i+5][-1])))
    return items, ops, test, throw

def part1(items, ops, test, throw):

    count = np.zeros(len(items), int)

    for rnd in range(20):
        for m in range(len(items)):
            while items[m]:
                worry = eval(ops[m], {"old":items[m].pop(0)})//3
                if worry%test[m]==0: items[throw[m][0]].append(worry)
                else:  items[throw[m][1]].append(worry)
                count[m] += 1

    return sorted(count)[-2:][0]*sorted(count)[-2:][1]

def part2(items, ops, test, throw):

    count = np.zeros(len(items), int)
    mod_items = [[[i%test[m] for m in range(len(items))] for i in m_items] for m_items in items]

    for rnd in range(10000):
        for m in range(len(items)):
            while mod_items[m]:
                worry = np.remainder(np.array([eval(ops[m], {"old":mod_item}) for mod_item in mod_items[m].pop(0)]),test)
                if worry[m]==0: mod_items[throw[m][0]].append(worry)
                else: mod_items[throw[m][1]].append(worry)
                count[m] += 1

    return sorted(count)[-2:][0]*sorted(count)[-2:][1]

if __name__ == "__main__":
    day = 11
    data = get_input(day)
    print(part1(*parse_monkeys(data)))
    print(part2(*parse_monkeys(data)))
