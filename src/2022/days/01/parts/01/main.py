def get_most_calories(lines):
  r = 0
  c = 0
  for l in lines:
    l = l.strip()
    if l == "":
      r = max(r, c)
      c = 0
    else:
      c += int(l)
  
  return r

f = open('days/01/parts/01/input.txt', 'r')
lines = f.readlines()
r = get_most_calories(lines)

print(r)


