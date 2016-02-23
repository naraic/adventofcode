#! /usr/bin/env python
from sys import argv
import re

def find_escapes(s):
  regexes = [(re.compile(r'\\x[0-9A-F]{2}', re.IGNORECASE), 3),
             (re.compile(r'\\\"'), 1),
             (re.compile(r'\\\\'), 1)]
  matches = 2
  #muliply the number of chars to remove from the memory of the string with the number of matches per regex
  for pattern, chars in regexes:
    matches += len(pattern.findall(s)) * chars
    print s, matches
  memory_usage = num_chars(s) - matches
  return memory_usage

def num_chars(s):
  return len(s)

if __name__ == '__main__':
    chars = 0
    memory = 0
    with open(argv[1]) as strings:
      for string in strings:
        string = string.strip()
        chars += num_chars(string)
        memory += find_escapes(string)
      print chars - memory
