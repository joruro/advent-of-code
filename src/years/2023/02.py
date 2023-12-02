import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2023, 2)

# WRITE YOUR SOLUTION HERE

colors_game = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def get_game(line):
    [game, sets] = line.split(':')
    game = int(game.split(' ')[1])
    sets = sets.split(';')
    # print(sets)

    min_colors = {
        'blue': 0,
        'red': 0,
        'green': 0
    }

    for s in sets:
        colors = s.split(',')
        for c in colors:
            [total, color] = c.strip().split(' ')
            total = int(total)

            if min_colors[color] < total:
                min_colors[color] = total

    t = 1
    for c in min_colors:
        t *= min_colors[c]

    return t


def get_sum(input):
    t = 0
    for line in input:
        t += get_game(line)
    return t

print(get_sum(input.split('\n')))