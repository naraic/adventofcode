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

def distance(p1, p2):
  return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))

def find_nearest(p1, points):
  min = max_x * max_y 
  nearest = []
  for p2 in points:
    d = distance(p1, p2)
    if min == d:
      nearest.append(p2)
    elif min > d:
      nearest = [p2]
      min = d
  return nearest

for x, row in enumerate(grid):
  for y, val in enumerate(row):
    if val == empty:
      nearest = find_nearest((x, y), points)
      if len(nearest) > 1:
        val = overlap
      else:
        new_val = grid[nearest[0][0]][nearest[0][1]]
        grid[x][y] = '0' + new_val 

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
