import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402
from collections import defaultdict

input = get_input(2023, 3)

# WRITE YOUR SOLUTION HERE

adjacent_map = defaultdict(list)

def is_symbol(char):
    return char.isascii() and not char.isalnum() and char != '.' 

def get_adjacent_to_symbol(y, x, m):
    for i in range(-1,2):
        y1 = y+i
        if y1 < 0 or y1 >= len(m):
            continue
        for j in range(-1,2):
            x1 = x+j
            if x1 < 0 or x1 >= len(m[0]):
                continue
            if x1 == 0 and y1 == 0:
                continue
            if is_symbol(m[y1][x1]):
                return (y1, x1)
    return None

def get_numbers_per_line(y, m):
    line = m[y]
    numbers = []
    x = 0
    while x < len(line):
        if not line[x].isalnum():
            x += 1
        else:
            number = []
            adjacents = defaultdict(bool)
            while x < len(line) and line[x].isalnum():
                adjacent = get_adjacent_to_symbol(y, x, m)
                if adjacent:
                    adjacents[adjacent] = True
                number.append(line[x])
                x += 1
            for a in list(adjacents.keys()):
                adjacent_map[a].append(int(''.join(number)))
        

def get_sum(input):
    total = 0
    for y in range(0, len(input)):
        get_numbers_per_line(y, input)
    
    for a in adjacent_map:
        if len(adjacent_map[a]) == 2:
            total += adjacent_map[a][0] * adjacent_map[a][1]
    
    return total
print(get_sum(input.split('\n')))