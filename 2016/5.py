#! /usr/bin/env python
from sys import argv

def vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for c in v:
        count += s.count(c)
    if count < 3:
        return False
    return True

def doubles(s):
    for n in range(1, len(s)):
        if s[n-1] == s[n]:
            return True
    return False

def too_close(s):
    strings = ['ab', 'cd', 'pq', 'xy']
    for pair in strings:
        if pair in s:
            return False
    return True
    
if __name__ == '__main__':
    with open(argv[1]) as slist:
        nice = 0
        for line in slist:
            if too_close(line) and doubles(line) and vowels(line):
                nice += 1
    print(nice)
