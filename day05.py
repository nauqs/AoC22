from utils import get_input

def parse_stacks(data):
    inst_index = data.index('')
    n_stacks = int(data[inst_index-1].split()[-1])
    stacks = [[] for _ in range(n_stacks)]

    for row in data[:inst_index-1]:
        for i in range(n_stacks):
            if row[4*i+1] != ' ': stacks[i].insert(0, row[4*i+1])
    instructions = [(int(r.split()[1]), int(r.split()[3]), int(r.split()[5])) for r in data[inst_index+1:]]
    
    return stacks, instructions

def part1(stacks, instructions):
    for n, origin, dest  in instructions:
        for i in range(n): stacks[dest-1].append(stacks[origin-1].pop())
    return ''.join([s[-1] for s in stacks])

def part2(stacks, instructions):
    for n, origin, dest  in instructions:
        for i in range(n): 
            stacks[dest-1].insert(len(stacks[dest-1])-i,stacks[origin-1].pop())
    return ''.join([s[-1] for s in stacks])


if __name__ == "__main__":
    day = 5
    data = get_input(day, splitlines=False).splitlines()
    stacks, instructions = parse_stacks(data)
    print(part1(stacks, instructions))
    stacks, instructions = parse_stacks(data)
    print(part2(stacks, instructions))

