#! /usr/bin/env python
from sys import argv
import re

def num_escapes(s):
  regexes = [(r'\\x[0-9A-Fa-f]{2}', 3),
             (r'\\\\x[0-9A-Fa-f]{2}', -3),
             (r'\\\"', 1),
             (r'\\\"$', -1),
             (r'\\\\', 1)]
  matches = 2
  #muliply the number of chars to remove from the memory of the string with the number of matches per regex
  print s, 
  for pattern, chars in regexes:
    m = len(re.compile(pattern).findall(s)) 
    #print pattern, m
    if m > 0:
      print pattern, m, 
    matches += m * chars
  memory_usage = num_chars(s) - matches
  print 'chars:', num_chars(s), 
  print memory_usage
  return memory_usage

def num_chars(s):
  return len(s)

if __name__ == '__main__':
    total = 0
    with open(argv[1]) as strings:
      for string in strings:
        string = string.strip()
        total += (num_chars(string) - num_escapes(string))
      print total 
