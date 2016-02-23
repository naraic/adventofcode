#! /usr/bin/env python
from sys import argv

def has_repeat(s):
  for i in range(2, len(s)):
    if s[i-2] == s[i]: 
      return True
  return False
  
def has_pairs(s):
  pairs = [] 
  prev = ''
  for i in range(1, len(s)):
    pair = (s[i-1], s[i])
    if pair in pairs and pair != prev:
      return True
    elif pair == prev:
      prev = ''
    else:
      pairs.append(pair) 
      prev = pair
  return False
    
if __name__ == '__main__':
    with open(argv[1]) as slist:
        nice = 0
        for line in slist:
            line = line.strip()
            if has_repeat(line):
              if has_pairs(line):
                nice += 1
    print(nice)
