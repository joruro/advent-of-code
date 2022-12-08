from functools import reduce
import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 8)


def parse_row(row):
    return list(map(int, list(row)))


def count_visible_trees_per_row(row_index, row, max_per_column, visible_trees):
    left, right = 0, len(row) - 1
    max_left, max_right = -1, -1
    for _ in range(len(row)):
        if row[left] > max_left or row[left] > max_per_column[left]:
            max_left = max(max_left, row[left])
            max_per_column[left] = max(max_per_column[left], row[left])
            visible_trees[(row_index, left)] = True

        if row[right] > max_right or row[right] > max_per_column[right]:
            max_right = max(max_right, row[right])
            max_per_column[right] = max(max_per_column[right], row[right])
            visible_trees[(row_index, right)] = True

        left += 1
        right -= 1

    # print(visible_trees)
    return max_per_column, visible_trees


def count_visible_trees(rows):
    top, bottom = 0, len(rows) - 1
    max_top, max_bottom = None, None
    visible_trees = dict()
    for _ in range(len(rows)):
        top_row = parse_row(rows[top])
        bottom_row = parse_row(rows[bottom])

        if not max_top:
            max_top = [-1] * len(top_row)
        if not max_bottom:
            max_bottom = [-1] * len(bottom_row)

        max_top, visible_trees = count_visible_trees_per_row(
            top, top_row, max_top, visible_trees)
        max_bottom, visible_trees = count_visible_trees_per_row(
            bottom, bottom_row, max_bottom, visible_trees)

        top += 1
        bottom -= 1

    return len(visible_trees)


def build_grid(rows):
    grid = []
    for row in rows:
        grid.append(parse_row(row))
    return grid


def get_highest_scenic_score(rows):
    grid = build_grid(rows)
    max_score = 0
    for row_index in range(len(grid)):
        row = grid[row_index]
        for column_index in range(len(row)):
            column = row[column_index]
            y, x = row_index, column_index
            score = []
            # Left
            trees = 0
            x -= 1
            while x > -1:
                if row[x] >= column:
                    trees += 1
                    break
                trees += 1
                x -= 1
            score.append(trees)
            # Right
            x = column_index
            trees = 0
            x += 1
            while x < len(row):
                if row[x] >= column:
                    trees += 1
                    break
                trees += 1
                x += 1
            score.append(trees)
            # Top
            trees = 0
            y -= 1
            while y > -1:
                if grid[y][column_index] >= column:
                    trees += 1
                    break
                trees += 1
                y -= 1
            score.append(trees)
            # Down
            y = row_index
            trees = 0
            y += 1
            while y < len(grid):
                if grid[y][column_index] >= column:
                    trees += 1
                    break
                trees += 1
                y += 1
            score.append(trees)
            max_score = max(max_score, reduce(lambda x, y: x * y, score))

    return max_score


lines = input.split("\n")
part_one = count_visible_trees(lines)
part_two = get_highest_scenic_score(lines)
print(part_one)
print(part_two)
