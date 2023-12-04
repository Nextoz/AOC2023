import sys

import re

def f(line):
    for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        line = line.replace(n, n + str(i+1) + n)
    x = re.findall(r'(\d)', line)
    return int(x[0] + x[-1])

def calculate_sum(filename):

    return sum(map(f, open(filename, 'r')))
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculate_sum.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    result = calculate_sum(filename)

    print(f"The sum of all of the calibration values is: {result}")
