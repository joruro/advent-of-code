def get_most_calories(lines, top = 3):
  r = []
  c = 0
  for l in lines:
    l = l.strip()
    if l == "":
      r.append(c)
      c = 0
    else:
      c += int(l)
  
  r = sorted(r)
  return sum(r[-top:])

f = open('days/01/parts/02/input.txt', 'r')
lines = f.readlines()
r = get_most_calories(lines)

print(r)


