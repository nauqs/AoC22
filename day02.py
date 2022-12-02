from utils import get_input
import numpy as np

scores = {"A": 1, "B": 2, "C": 3}

def part1(data):
    score = 0
    d = {"X": "A", "Y": "B", "Z": "C"}
    for o, p  in [rnd.split() for rnd in data]:
        if o==d[p]: 
            score += 3
        elif (o=="A" and d[p]=="B") or (o=="B" and d[p]=="C") or (o=="C" and d[p]=="A"):
            score += 6
        score += scores[d[p]]
    return score

def part2(data):
    score = 0
    symbols = ["A", "B", "C"]
    for o, outcome  in [rnd.split() for rnd in data]:
        if outcome=="Y":  
            score += 3
            p = o
        elif outcome=="Z": 
            score += 6
            p = symbols[(symbols.index(o)+1)%3]
        elif outcome=="X":
            p = symbols[(symbols.index(o)-1)%3]
        score += scores[p]
    return score


if __name__ == "__main__":
    day = 2
    data = get_input(day)
    print(part1(data.copy()))
    print(part2(data.copy()))

