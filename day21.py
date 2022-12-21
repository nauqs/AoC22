from utils import get_input
from collections import deque
import re
from sympy.solvers import solve
from sympy import Symbol

def part1(data):
    stack, d = deque(data), {}
    while stack:
        l = stack.pop()
        if len(l)==2: d[l[0]] = int(l[1])
        else:
            if l[1] in d and l[3] in d:
                d[l[0]] = eval(f"d['{l[1]}'] {l[2]} d['{l[3]}']")
            else: stack.appendleft(l)
    return int(d["root"])

def part2(data):
    stack, d = deque(data), {}
    c = 0
    while stack and c>=0:
        l = stack.pop()
        if l[0]=="humn": d["humn"] = "x"
        elif len(l)==2: d[l[0]] = int(l[1])
        else:
            if l[1] in d and l[3] in d and l[1]!="humn" and l[3]!="humn":
                d[l[0]] = eval(f"d['{l[1]}'] {l[2]} d['{l[3]}']")
                c = 0
            else: 
                stack.appendleft(l)
                c += 1
        if c >= len(stack):
            break
    c = 5000
    while stack and c>=0:
        l = stack.pop()
        c-=1
        if l[0] == "root": l[2] = "-"
        if l[1] in d and l[3] in d:
            d[l[0]] = f"({d[l[1]]} {l[2]} {d[l[3]]})"
            stack.appendleft(l)
        else: 
            d[l[0]] = f"({l[1]} {l[2]} {l[3]})"
            stack.appendleft(l)
    return int(solve(d["root"], Symbol('x'))[0])

if __name__ == "__main__":
    day = 21
    data = get_input(day)
    data = [re.split(": | ", l) for l in data]
    print(part1(data))
    print(part2(data))

