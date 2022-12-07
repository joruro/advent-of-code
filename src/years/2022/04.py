import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 4)


def find_pairs_part_one(lines):
    p = 0
    for line in lines:
        line = line.strip().split(',')
        for i in range(len(line)):
            line[i] = line[i].split('-')
            for j in range(len(line[i])):
                line[i][j] = int(line[i][j])
        if line[0][0] <= line[1][0] and line[0][1] >= line[1][1]:
            p += 1
            continue
        if line[1][0] <= line[0][0] and line[1][1] >= line[0][1]:
            p += 1
            continue
    return p


def find_pairs_part_two(lines):
    p = 0
    for line in lines:
        line = line.strip().split(',')
        for i in range(len(line)):
            line[i] = line[i].split('-')
            for j in range(len(line[i])):
                line[i][j] = int(line[i][j])
        if line[0][0] <= line[1][0] and line[0][1] >= line[1][0]:
            p += 1
            continue
        if line[1][0] <= line[0][0] and line[1][1] >= line[0][0]:
            p += 1
            continue
    return p


part_one = find_pairs_part_one(input.split('\n'))
part_two = find_pairs_part_two(input.split('\n'))
print(part_one)
print(part_two)
