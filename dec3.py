import re
import sys


def sum_part_numbers(schematic):
    symbols = ['*', '#', '+', '$']
    rows = schematic.split('\n')
    total = 0
    skip = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if skip > 0:
                skip -= 1
                continue
            if rows[i][j].isdigit():
                match = re.search(r'\d+', rows[i][j:])
                if match:
                    number = match.group()
                    print("Match :")
                    print(number)
                    skip = len(number) - 1
                    anysymbols = 0
                    for k in range(len(number)):
                        if any(rows[i+di][j+di+k] in symbols for di in range(-1, 2) if 0 <= i+di < len(rows) and 0 <= j+di < len(rows[i])) or \
                            any(rows[i+di][j-di+k] in symbols for di in range(-1, 2) if 0 <= i+di < len(rows) and 0 <= j-di < len(rows[i])) or \
                            any(rows[i+di][j+k] in symbols for di in range(-1, 2) if 0 <= i+di < len(rows) and 0 <= j+k < len(rows[i])) or \
                            any(rows[i+di+k][j] in symbols for di in range(-1, 2) if 0 <= i+di+k < len(rows) and 0 <= j < len(rows[i])):
                            anysymbols += 1
                            print(anysymbols)
                            
                    if anysymbols > 0:  
                        total += int(number)
                        print("Total er" + str(total))    
    return total
        
if __name__ == "__main__":

    with open(sys.argv[1], 'r') as file:
        schematic = file.read()

    print(sum_part_numbers(schematic))
