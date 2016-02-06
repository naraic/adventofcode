#! /usr/bin/env python

from sys import argv
from ctypes import c_uint16

wire = {}

def lookup(var):
  return wire[var]

def eval(var):
  try:
    n = int(var)
  except:
    try:
      n = int(lookup(var))
    except:
      try:
        eval(lookup(var))
      except:
        print("can't evaluate %s" % var)
        exit(0)
  return c_uint16(n).value

def and_or(line):
    left = c_uint16(eval(line[0]))
    right = c_uint16(eval(line[2]))
    if line[1] == 'AND':
      n = left.value & right.value
    else:
      n = left.value | right.value
    assign([n, None, line[-1]])

def shift(line):
  n = c_uint16(eval(line[0]))
  if line[1] == 'RSHIFT':
    n.value >>= int(line[2])
  else:
    n.value <<= int(line[2])
  assign([n.value, None, line[-1]]) 


def invert(line):
  try:
    n = ~eval(line[1])
  except:
    n = ~eval(line[1]).value
  assign([c_uint16(n).value, None, line[-1]])

def assign(line):
  wire[line[2]] = int(line[0])

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
      for line in wire:
        print(c_uint16(wire[line]).value)
