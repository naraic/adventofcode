#! /usr/bin/env python
'''
  watch out! this answer is incorrect! out by one :(
  can't remember why :P 
'''
from sys import argv
from sets import Set

if __name__ == '__main__':
  with open(argv[1]) as input:
    input = input.readline()
    santa_pos = (0, 0)
    robot_pos = (0, 0)
    visited = Set(santa_pos)
    santa_turn = True
    for direction in input:
      if santa_turn:
        pos = santa_pos
        santa_turn = False
      else:
        pos = robot_pos
        santa_turn = True
      x, y = pos
      if direction is '^':
        y += 1
      if direction is 'v':
        y -= 1
      if direction is '>':
        x += 1
      if direction is '<':
        x -= 1
      pos = (x, y)

      visited.add(pos)
      if santa_turn:
        robot_pos = pos
      else:
        santa_pos = pos

  print len(visited)
      
      
        
      
      
