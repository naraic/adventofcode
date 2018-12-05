jumps = list(map(int, open("input").read().splitlines()))

steps = 0
n_jmps = len(jumps)

pc = 0
count = 0

while(True):
  offset = jumps[pc]
  if offset >= 3:
    jumps[pc] -= 1
  else:
    jumps[pc] += 1
  pc += offset
  count += 1
  if pc >= n_jmps or pc < 0:
    break
print(count)


