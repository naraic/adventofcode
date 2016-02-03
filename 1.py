#! /usr/bin/env python
from sys import argv

if __name__ == '__main__':
	floor = 0;
	with open(argv[1]) as input:
		input = input.readline()	
		for bracket in input:
			if bracket == '(':
				floor += 1
			elif bracket == ')':
				floor -= 1
			else:
				pass
	print(floor)
			


