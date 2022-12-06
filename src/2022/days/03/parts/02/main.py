
def get_priority(c):
  c = ord(c)

  if c >= 65 and c <= 90:
    return c - ord('A') + 27
  else:
    return c - ord('a') + 1

def sum_priorities(rucksacks):
  p = 0
  i = 0
  m = {}
  for r in rucksacks:
    r = r.strip()

    if i > 2:
      i = 0
      m = {}
    
    for c in r:
      m_i = m.get(c, {})
      m_i[i] = True
      m[c] = m_i
      if len(m_i) == 3:
        p += get_priority(c)
        break
    i += 1
  return p

f = open('2022/days/03/parts/02/input.txt', 'r')
lines = f.readlines()
r = sum_priorities(lines)

print(r)


