#find the odd square less than your number and work from there

from math import floor, sqrt

n = int(read(open("input")).strip())
s = floor(sqrt(n))
if s % 2 == 0:
#even
  s -= 1

s*s

