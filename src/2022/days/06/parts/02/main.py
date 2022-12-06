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


f = open('src/2022/days/06/input.txt', 'r')
lines = f.readlines()
r = find_start_of_packet(lines[0].strip())

print(r)
