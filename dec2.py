import sys
import re

def rounds(g):
    return [rs.split(",") for rs in g.split(":")[1].split(";")]

def parse_draw(d):
    return re.findall("\d+ \w+", d)[0].split()

## PART 1
constraints = { 'red': 12, 'green': 13, 'blue': 14 }

def round_ok(r):
    return all(int(n) <= constraints[c] for n, c in (parse_draw(d) for d in r))

## PART 2
def num_of_color(r, find_color):
    return next((int(n) for n, c in (parse_draw(d) for d in r) if c == find_color), 0)

def max_num(g, c):
    return max(num_of_color(r, c) for r in rounds(g))

def power(g):
    return max_num(g, 'red') * max_num(g, 'green') * max_num(g, 'blue')

## MAIN 

filename = sys.argv[1]
f = open(filename, "r")


I = f.readlines()

print(f'1: {sum(i for i, g in enumerate(I, 1) if all(round_ok(r) for r in rounds(g)))}')
print(f'2: {sum(map(power, I))}')
