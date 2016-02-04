#! /usr/bin/env python

from sys import argv

if __name__ == '__main__':
  with open(argv[1]) as input:
    input = input.readline()
    pos = (0, 0)
    visited = [pos]
    for direction in input:
      x, y = pos
      print x, y
      if direction is '^':
        y += 1
      if direction is 'v':
        y -= 1
      if direction is '>':
        x += 1
      if direction is '<':
        x -= 1
      pos = [x, y]
      if pos not in visited:
        visited.append(pos)
  print len(visited)
      
      
        
      
      
