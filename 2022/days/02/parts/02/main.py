

def calculate_score(matches):

  translation = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
  }

  rules_to_loose = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
  }

  rules_to_win = {v: k for k, v in rules_to_loose.items()}

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
    a = m[0]

    # To loose
    if m[1] == 'X':
      h = rules_to_loose[a]
    # To draw
    elif m[1] == 'Y':
      s += 3
      h = a
    else:
      h = rules_to_win[a]
      s += 6
 
    s += scores[h]
    
  return s

f = open('days/02/parts/02/input.txt', 'r')
lines = f.readlines()
r = calculate_score(lines)

print(r)


