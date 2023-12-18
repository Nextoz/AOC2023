import re
from functools import reduce

FILE = 'Input8.txt'

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * (b // gcd(a, b))

MAP = {}

with open(FILE) as f:
    instructions = f.readline()
    f.readline() # skip empty line

    starts = []
    for line in f.readlines():
       u, a, b =  re.search(r'(\w+) = \((\w+), (\w+)\)', line).groups()
       MAP[u] = {'L': a, 'R': b}
       if u[-1] == 'A':
           starts.append(u)
    
    ends = []
    for node in starts:
        steps = 0
        while node[-1] != 'Z': # we found the end
            i = steps % (len(instructions) - 1) # repeat the whole sequence of instructions as necessary
            node = MAP[node][instructions[i]]
            steps += 1
        ends.append(steps)

    print(reduce(lcm, ends))
