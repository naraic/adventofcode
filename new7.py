#! /usr/bin/env python

from sys import argv, stdin, exit
from ctypes import c_uint16

cache = {}
wires = {}

def evaluate(ident):
  print 'evaluating ident', ident
  if ident.isdigit():
    return c_uint16(int(ident))
  elif ident in cache:
    return  c_uint16(int(cache[ident]))
  elif ident in wires: 
    return wires[ident]
  else:
    return c_uint16(int(ident))

def assign(line):
  print line
  if line[0].isdigit():
    cache[line[2]] = int(line[0])
    print 'cache:', cache
  else:
    wires[line[2]] = line[0]
    print 'wires:', wires

def shift(line):
  print 'shifting', line
  op1 = evaluate(line[0])
  op2 = evaluate(line[2])
  var = line[4]
  operator = line[1]
  if operator == 'RSHIFT':
    result = op1.value << op2.value
  else:
    result = op1.value >> op2.value
  assign([str(result), '', var])

def invert(line):
  op1 = evaluate(line[1])
  var = line[3]
  result = ~op1.value
  assign([var, '', result])

def parse(line):
    print 'parsing', line
    if line[1] == '=':
      assign(line)
    elif line[0] == 'NOT':
      invert(line)
    elif line[1] == 'AND' or line[1] == 'OR':
      bitwise(line)
    elif line[1] == 'LSHIFT' or line[1] == 'RSHIFT':
      shift(line)
    else:
      print 'something is wrong, unknown statement type'
      sys.exit(1)

if __name__ == '__main__':
  line = stdin.readline()
  while line:
    line = line.split()
    if len(line) > 1:
      parse(line)
    else:
      print evaluate(line[0])
    line = stdin.readline()
