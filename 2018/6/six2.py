from sys import exit
points = open("input").read().splitlines()

points = [tuple(map(int, (point.split(", ")))) for point in points]

empty = 'e'
overlap = '.'

def get_x(t):
  return t[0]

def get_y(t):
  return t[1]


def normalise(points):
  return [(x-min_x, y-min_y) for (x, y) in points]

def distance(p1, p2):
  return abs(get_x(p1) - get_x(p2)) + abs(get_y(p1) - get_y(p2))

grand_total = 0
max_x = max(map(get_x, points))
max_y = max(map(get_y, points))
for x in range(max_x+1):
  for y in range(max_y+1):
    sum = 0
    for point in points:
      sum += distance(point, (x, y))
    if sum < 10000:
      grand_total += 1

print(grand_total)

exit(0)

def initialise_grid(points):
  max_x = max(map(get_x, points))
  max_y = max(map(get_y, points))
  col = [empty]*(max_y+1)
  grid = []
  for x in range(max_x+2):
    grid.append(col.copy())
  for index, (x, y) in enumerate(points):
    grid[x][y] = str(index+1)
  return grid 

def has_empty(grid):
  for row in grid:
    if empty in row: 
      return True
  return False

def taxi_circle(x, y, r):
  points = set()
  for i in range(-r, r+1):
    for j in range(-r, r+1):
      x_cand = x+i
      y_cand = y+j
      if (abs(x - x_cand) + abs(y- y_cand)) == r:
        if x_cand >= 0 and x_cand <= max_x:
          if y_cand >= 0 and y_cand <= max_y:
            points.add((x+i, y+j))
  return list(points)
  

min_x = min(map(get_x, points))
min_y = min(map(get_y, points))

points = normalise(points)

max_x = max(map(get_x, points))
max_y = max(map(get_y, points))
grid = initialise_grid(points)


for x, row in enumerate(grid):
  print(x)
  for y, val in enumerate(row):
    if val == empty:
      radius = 1
      points = taxi_circle(x, y, radius)
      found = False
      while not found:
        dangers = [] 
        for px, py in points:
          r_point = grid[px][py]
          if r_point != empty and r_point != overlap:
            if r_point[0] != '0':
             dangers.append(r_point)
        if len(dangers) > 1:
          found = True
          grid[x][y] = overlap  
        elif len(dangers) == 1:
          found = True
          grid[x][y] = '0' + dangers[0]
        else:
          radius += 1
        points = taxi_circle(x, y, radius)

edges = set()
for coord in grid[0]:
  edges.add(coord)
for coord in grid[-1]:
  edges.add(coord)
for row in grid:
  edges.add(row[0])
  edges.add(row[-1])

scores = {}
for row in grid:
  for val in row:
    if val[0] == '0' and val not in edges:
      if val in scores:
        scores[val] += 1
      else:
        scores[val] = 1

max = 0
for key in scores:
  if scores[key] > max:
    max = scores[key]

print(max+1)
