from collections import Counter

f = open("input")

ids = [line.strip() for line in f.readlines()]

twos = 0
threes = 0

for id in ids:
  letters = Counter(id)
  if 2 in letters.values():
    twos += 1
  if 3 in letters.values():
    threes += 1

print(twos * threes)

for i in ids:
  for j in ids:
    diff = [a for a, b in zip(i, j) if a != b]
    if len(diff) is 1:
      l = list(i)
      l.remove(diff[0])
      print(''.join(l)) #.remove(diff[0]))

