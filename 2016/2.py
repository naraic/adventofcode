#! /usr/bin/env python
from sys import argv

if __name__ == '__main__':
	total = 0
	with open(argv[1]) as input:
		for present in input:
			l, w, h = map(int, present.split('x'))
			area = (2*l*w) + (2*w*h) + (2*h*l)
			dims = [l, w, h]
			dims.remove(max(dims))
			area += dims[0]*dims[1]  
			total += area
	print(total)
