#! /usr/bin/env python
from sys import argv
from pprint import pprint

if __name__ == '__main__':
    light = [[0 for x in range(1000)] for x in range(1000)] 
    with open(argv[1]) as clist:
        for command in clist:
            command = command.replace(',', ' ')
            coords = [int(s) for s in command.split() if s.isdigit()]
            print coords
            for i in range(coords[0], coords[2]+1):
                for j in range(coords[1], coords[3]+1): 
                    if 'turn on' in command:
                        light[i][j] += 1
                    elif 'turn off' in command:
                        if light[i][j] != 0:
                          light[i][j] -= 1
                    else:
                        light[i][j] += 2
    print(sum(sum(x) for x in light))
