
def find_pairs(lines):
  p = 0
  for l in lines:
    l = l.strip().split(',')
    for i in range(len(l)):
      l[i] = l[i].split('-')
      for j in range(len(l[i])):
        l[i][j] = int(l[i][j]) 
    if l[0][0] <= l[1][0] and l[0][1] >= l[1][1]:
      p += 1
      continue
    if l[1][0] <= l[0][0] and l[1][1] >= l[0][1]:
      p += 1
      continue
  return p

f = open('2022/days/04/parts/01/input.txt', 'r')
lines = f.readlines()
r = find_pairs(lines)

print(r)


