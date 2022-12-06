
def get_priority(c):
    c = ord(c)

    if c >= 65 and c <= 90:
        return c - ord('A') + 27
    else:
        return c - ord('a') + 1


def sum_priorities(rucksacks):
    p = 0

    for r in rucksacks:
        r = r.strip()
        part_length = len(r) // 2
        left = r[:part_length]
        right = r[part_length:]

        left_items = {}
        right_items = {}

        for i in range(len(left)):
            left_items[left[i]] = True
            right_items[right[i]] = True

            if left[i] in right_items:
                p += get_priority(left[i])
                break

            if right[i] in left_items:
                p += get_priority(right[i])
                break

    return p


f = open('2022/days/03/parts/01/input.txt', 'r')
lines = f.readlines()
r = sum_priorities(lines)

print(r)
