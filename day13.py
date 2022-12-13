from utils import get_input

def part1(data):
    return sum([(i+1)*int(compare(l1,l2)) for i, (l1, l2) in enumerate(data)])

def compare(left, right):
    if type(left)==int and type(right)==int:
        if left<right: return True
        elif left>right: return False
    elif type(left)==list and type(right)==list:
        for i in range(max(len(left), len(right))):
            if i>=len(left) and i<len(right): return True
            elif i<len(left) and i>=len(right): return False
            elif i<len(left) and i <len(right):
                if compare(left[i], right[i]) is not None:
                    return compare(left[i], right[i])
            else: break
    else:
        if type(left)==int: left = [left]
        elif type(right)==int: right = [right]
        return compare(left, right)
    return None

def part2(data):
    # bubble sort! hahahahahaha
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if not compare(data[j],data[j+1]): 
                data[j], data[j+1] = data[j+1], data[j]
    return (data.index([[2]])+1)*(data.index([[6]])+1)

if __name__ == "__main__":
    day = 13
    data = get_input(day)
    print(part1([[(eval(data[3*i])),eval((data[3*i+1]))] for i in range(len(data)//3+1)]))
    print(part2([[[2]]]+[[[6]]]+[eval(data[3*i]) for i in range(len(data)//3+1)]+[eval(data[3*i+1]) for i in range(len(data)//3+1)]))
