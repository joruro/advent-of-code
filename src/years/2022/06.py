import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 6)

def find_start_of_packet(input, distinct_chars=14):
    l = 0
    m = set()

    o = 0
    for r in range(len(input)):
        while input[r] in m:
            m.remove(input[l])
            l += 1
        m.add(input[r])
        o += 1
        if len(m) == distinct_chars:
            return o


part_one = find_start_of_packet(input, 4)
part_two = find_start_of_packet(input, 14)
print(part_one)
print(part_two)