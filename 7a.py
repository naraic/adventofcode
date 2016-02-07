#! /usr/bin/env python

from sys import argv
from ctypes import c_uint16

wires = {}

def evaluate(wire):
  try:
    if wire.isdigit():
      return c_uint16(int(wire))
  except:
    pass
  value = wires[wire]
  #print(wires[wire])
  if len(value) is 1:
    try:
      return c_uint16(int(value[0]))
    except:
      return evaluate(value[0])
  elif 'NOT' in value:
    if value[-1].isdigit():
      return c_uint16(~c_uint16(int(value[-1])).value)
    else:
      return c_uint16(~evaluate(value[-1]).value)
  elif 'LSHIFT' in value:
    return c_uint16(evaluate(value[0]).value << int(value[2])) 
  elif 'RSHIFT' in value:
    return c_uint16(evaluate(value[0]).value >> int(value[2]))
  elif 'AND' in value:
    return c_uint16(evaluate(value[0]).value & evaluate(value[2]).value)
  elif 'OR' in value:
    return c_uint16(evaluate(value[0]).value | evaluate(value[2]).value)

if __name__ == '__main__':
    with open(argv[1]) as wire_file:
      for line in wire_file:
        line = line.split()
        wires[line[-1]] = line[:-2]
      for wire in wires:
        print(evaluate(wire))
      print(evaluate('a'))
