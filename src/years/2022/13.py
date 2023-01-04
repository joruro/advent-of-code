import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 13)

def parse_line(line, start=1):
    signal = []
    for i in range(len(line[start:])):
        c = line[i]
        if c == '[':
            items = line[start:(i-1)].split(',')
            for item in items:
                signal.append(int(item))
            items = parse_line(line, i)
            signal.append(items)

        if c == ']':
            items = line[start:(i-1)].split(',')
            signal.append(parse_line(line, i))

        


parse_line("[1,1,3,1,1]")


# WRITE YOUR SOLUTION HERE

