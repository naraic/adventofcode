#! /usr/bin/env python3

wires = []

filename = "input"
#filename = "test_input1"

with open(filename) as f:
    for line in f.readlines():
        wires.append(line.strip().split(','))


def get_length(move):
    return int(move[1:])


def get_delta(move):
    length = get_length(move) #length of current segment
    if move[0] == 'U':
        x_delta = 0
        y_delta = length
    elif move[0] == 'D':
        x_delta = 0
        y_delta = -length
    elif move[0] == 'R':
        x_delta = length
        y_delta = 0
    else:
        x_delta = -length
        y_delta = 0
    return (x_delta, y_delta)


def parse_wires(wires):
    segments = [[],[]]
    for wire_no, wire in enumerate(wires):
        x = 0
        y = 0
        curr = (x, y) 
        for move in wire:
            delta = get_delta(move)
            prev = curr
            curr = tuple(map(sum, zip(prev, delta)))
            segments[wire_no].append((prev, curr))
    return segments

def vertical(segment):
    '''segment: ((x1, y1), (x2, y2)) == (p1, p2)'''
    (x1, _), (x2, _) = segment
    #no change in x means vertical
    if x1 == x2:
        return True
    else:
        return False
    

def separate(segments):
    verticals = []
    horizontals = []
    for segment in segments: 
        if vertical(segment): 
            verticals.append(segment)
        else:
            horizontals.append(segment)
    return verticals, horizontals


def overlap(h_line, v_line):
    (h_xs, h_y1), (_, h_y2) = h_line
    (v_x1, v_ys), (v_x2, _) = v_line
    if min(v_x1, v_x2) <= h_xs <= max(v_x1, v_x2) and \
       min(h_y1, h_y2) <= v_ys <= max(h_y1, h_y2):
        return (h_xs, v_ys)
    else:
        return None
        
def check(verticals, horizontals):
    overlaps = []
    for v_line in verticals:
        for h_line in horizontals:
            res = overlap(v_line, h_line)
            if res:
                overlaps.append(res)
    return overlaps



def man_dist(coord):
    (x, y) = coord
    return abs(x) + abs(y)


def find_min(coords):
    min = man_dist(coords.pop())
    min_point = (0,0)
    for point in coords:
        if point != (0,0):
            if min > man_dist(point):
                min = man_dist(point)
                min_point = point
    return min


segments = parse_wires(wires)
#separate into wire 1 verticals etc (so we're not checking for overlap on wires that begin/end at the same points)
segments_wire1 = segments[0]
segments_wire2 = segments[1]
verticals1, horizontals1 = separate(segments_wire1)
verticals2, horizontals2 = separate(segments_wire2)
overlaps = check(verticals1, horizontals2)
overlaps += check(verticals2, horizontals1)
print(find_min(overlaps))
