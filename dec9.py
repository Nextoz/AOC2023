def get_input():
    with open('Input9.txt', 'r') as f:
        input = [line.strip() for line in f.readlines()]
    return input

def a_b(b=False):
    ans = 0
    input = get_input()
    for line in input:
        line = [int(nr) for nr in line.split()]
        if b:
            line = line[::-1]
        last = line[-1]
        while line and any(e != 0 for e in line):
            for i in range(1, len(line)):
                line[i - 1] = line[i] - line[i - 1]
            line.pop()
            last += line[-1]
        ans += last

    return ans

if __name__ == '__main__':
    print(a_b())
    print(a_b(True))