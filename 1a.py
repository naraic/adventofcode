#! /usr/bin/env python
from sys import argv, exit

if __name__ == '__main__':
	floor = 0;
	with open(argv[1]) as input:
		input = input.readline()	
		for position, bracket in enumerate(input):
			if bracket == '(':
				floor += 1
			elif bracket == ')':
				floor -= 1
				if floor < 0:
					print position + 1
					exit(0)
			else:
				pass
	print(floor)
			


