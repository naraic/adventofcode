#! /usr/bin/env python

from sets import Set
from copy import deepcopy
   
def arrange(s, l):
    if not s:
        yield l
    new_s = deepcopy(s)
    for item in s:
        arrange(new_s.remove(item), l.append(item))

dist = [] 
destinations = Set()
with open('input.9') as distances:
    for places in distances:
        start, _, end, _, distance = places.split()
        destinations.add(start)
        dist.append((start, end, distance))
    destinations = list(destinations)
    for combination in arrange(destinations, []):
        print combination
