import sys
import os
import math
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 10)


def sum_signal_strength(instructions):
    x = 1
    cycles = 0
    result = 0
    for i in instructions:
        if i == 'noop':
            cycles += 1
            if cycles == 20 or (cycles - 20) % 40 == 0:
                result += (x * cycles)
            continue

        for _ in range(2):
            cycles += 1
            if cycles == 20 or (cycles - 20) % 40 == 0:
                result += (x * cycles)
        x += int(i.split(' ')[1])

    return result


def get_crt_image(instructions):
    x = 1
    cycle = 1
    width = 40
    heigth = 6
    display = [['#' for _ in range(width)] for _ in range(heigth)]
    for i in instructions:
        if i == 'noop':
            row = (cycle // width) - \
                1 if cycle % width == 0 else math.floor(cycle / width)
            column = cycle - 1 - row * width
            char = '#'
            if column not in range(x - 1, x + 2):
                char = '.'
            display[row][column] = char
            cycle += 1
            continue

        for _ in range(2):
            row = (cycle // width) - \
                1 if cycle % width == 0 else math.floor(cycle / width)
            column = cycle - 1 - row * width
            char = '#'
            if column not in range(x - 1, x + 2):
                char = '.'
            display[row][column] = char
            cycle += 1
        x += int(i.split(' ')[1])

    return '\n'.join([''.join(line) for line in display])


lines = input.split("\n")
part_one = sum_signal_strength(lines)
part_two = get_crt_image(lines)
print(part_one)
print(part_two)
