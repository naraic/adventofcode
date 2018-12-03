size = 1000
claims = open("input").read().splitlines()

def lay_claims(claims):
  col = ['.']*size
  fabric = [col.copy() for _ in range(size)]
  for claim in claims:
    _, x, y, n, m = parse_claim(claim)
    for i in range(x, x+n):
      for j in range(y, y+m):
        if fabric[i][j] == 'x':
          fabric[i][j] = 'X'
        elif fabric[i][j] == '.':
          fabric[i][j] = 'x'
  return fabric

def count_overlaps(fabric):
  overlaps=0
  for row in fabric:
    for inch in row:
      if inch == 'X':
        overlaps += 1
  return overlaps

def count_area(fabric):
  area=0
  for row in fabric:
    for inch in row:
      if inch == 'X' or inch == 'x':
        area += 1
  return area

def parse_claim(claim):
  pieces = claim.split(' ')
  id = int(pieces[0][1:])
  x, y = pieces[2][:-1].split(',')
  x = int(x)
  y = int(y)
  n, m = pieces[3].split('x')
  n = int(n)
  m = int(m)
  return id, x, y, n, m

master = lay_claims(claims)
print("overlaps: ",count_overlaps(master))
master_area = count_area(master)
for claim in claims:
  id, _, _, n, m = parse_claim(claim)
  target = n*m
  less_claims = claims.copy()
  less_claims.remove(claim)
  diff = lay_claims(less_claims)
  diff_area = count_area(diff)
  if master_area - diff_area == target:
    print("non-overlapping id:", id)
  
