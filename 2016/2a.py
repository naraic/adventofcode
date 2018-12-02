#! /usr/bin/env python
from sys import argv

if __name__ == '__main__':
	total = 0
	with open(argv[1]) as input:
		for present in input:
			l, w, h = map(int, present.split('x'))
			vol = l*w*h
			total += vol
			smallest_perimeter = min([2*(l+w), 2*(w+h), 2*(h+l)])
			total += smallest_perimeter
	print(total)
