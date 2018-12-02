f = open ("input") 
string_lines = [line.strip().split('\t') for line in f.readlines()]
lines = [[int(y) for y in x] for x in string_lines]

s1 = 0
s2 = 0
for line in lines:
  s1 += max(line) - min(line)
  for i in line:
    for j in line:
      if i % j == 0 and i != j:
        s2 += i // j



print(s1)
print(s2)
