#! /usr/bin/env python
from sys import argv

if __name__ == '__main__':
    light = [[0]*1000]*1000
    with open(argv[1]) as clist:
        for command in clist:
            command = command.replace(',', ' ')
            coords = [int(s) for s in command.split() if s.isdigit()]
            print(coords)
            for i in range(coords[0], coords[2]):
                for j in range(coords[1], coords[3]): 
                    if 'turn on' in command:
                        light[i][j] = 1
                    elif 'turn off' in command:
                        light[i][j] = 0
                    else:
                        if light[i][j] == 0:
                            light[i][j] = 1
                        if light[i][j] == 1:
                            light[i][j] = 0

    print(sum(x.count(1) for x in light))
