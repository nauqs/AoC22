from utils import get_input

A_to_27 = (ord("A")-27)
a_to_1 = (ord("a")-1-(ord("A")-27))

def part1(data):
    priority = 0
    for rucksack in data:
        L = int(len(rucksack)/2)
        common = set(rucksack[:L]).intersection(set(rucksack[L:])).pop()
        # Map ord("a")-ord("z") to 1-26 and ord("A")-ord("Z") to 27-52
        priority += ord(common)-A_to_27-a_to_1*(ord(common)>=ord("a"))
    return priority

def part2(data):
    priority = 0
    for i in range(int(len(data)/3)):
        common = set(data[3*i]).intersection(set(data[3*i+1])).intersection(set(data[3*i+2])).pop()
        priority += ord(common)-A_to_27-a_to_1*(ord(common)>=ord("a"))
    return priority


if __name__ == "__main__":
    day = 3
    data = get_input(day)
    print(part1(data.copy()))
    print(part2(data.copy()))

