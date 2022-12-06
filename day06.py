from utils import get_input

def detect_marker(data, n):
    for i in range(len(data)-n+1):
        if len(set(data[i:i+n]))==n: return i+n

if __name__ == "__main__":
    day = 6
    data = get_input(day, splitlines=False)
    print(detect_marker(data,4))
    print(detect_marker(data,14))