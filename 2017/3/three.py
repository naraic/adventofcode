#find the odd square less than your number and work from there

from math import ceil, sqrt

n = int(open("input").read().strip())

def spiral(n):
  if n == 1:
    return 0
  closest_sq = ceil(sqrt(n))
  if closest_sq % 2 == 0:
    closest_odd_sq = cloest_sq + 1
  else:
    closest_odd_sq = closest_sq
  edge = closest_odd_sq - 1
  inner_len = (edge-1)**2 
  half_edge = edge // 2
  offset = n - inner_len
  pos = offset % edge 
  if pos > half_edge:
    difference = half_edge - (pos % half_edge)
  else:
    difference = pos
  print(closest_sq - difference - 1)

spiral(n)
