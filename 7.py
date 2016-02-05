#! /usr/bin/env python
from sys import argv
from ctypes import c_uint16

def and_or(line):
  pass

def shift(line):
  pass

def invert(line):
  pass

def assign(line):
  pass

def parse(line):
  line = line.split()
  if 'AND' in line or 'OR' in line:
    and_or(line)
  elif 'LSHIFT' in line or 'RSHIFT' in line:
    shift(line)
  elif 'NOT' in line:
    invert(line)
  else:
    assign(line)
    

if __name__ == '__main__':
    with open(argv[1]) as wires:
      for line in wires:
        parse(line)
        
        
      
