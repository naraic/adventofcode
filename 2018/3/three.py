size = 1000
claims = open("input").read().splitlines()

def lay_claims(claims):
  col = ['.']*size
  fabric = [col.copy() for _ in range(size)]
  for claim in claims:
    id, x, y, n, m = parse_claim(claim)
    for i in range(x, x+n):
      for j in range(y, y+m):
        if fabric[i][j] == '.':
          fabric[i][j] = id
        else:
          fabric[i][j] = 'x'
  return fabric

def count_overlaps(fabric):
  overlaps=0
  for row in fabric:
    for inch in row:
      if inch == 'x':
        overlaps += 1
  return overlaps

def find_uncovered(claims, fabric):
  for claim in claims:
    id, x, y, n, m = parse_claim(claim)
    covered = False
    for i in range(x, x+n):
      for j in range(y, y+m):
        if fabric[i][j] != id:
          covered = True
    if not covered:
      return id
  return ''

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
print("not covered: ", find_uncovered(claims, master))
  
