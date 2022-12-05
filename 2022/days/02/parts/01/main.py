

def calculate_score(matches):

  translation = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
  }

  rules = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
  }

  scores = {
    'A': 1,
    'B': 2,
    'C': 3
  }

  s = 0
  for m in matches:
    m = m.strip()
    m = m.split(" ")
    
    # Translate dict
    h = translation[m[1]]
    a = m[0]

    s += scores[h]
    
    # Draw
    if h == a:
      s += 3
    # Check if my action outscore opponent
    elif rules[h] == a:
      s += 6
    else:
      s += 0
    
  return s

f = open('days/02/parts/01/input.txt', 'r')
lines = f.readlines()
r = calculate_score(lines)

print(r)


