values = []
with open("input") as f:
	values = [int(line.strip()) for line in f.readlines()]


print(sum(values))	

sums = []   
found = False
while not found:
    for val in values:
        if len(sums) is not 0:
            new = sums[-1]+val
        else:
            new = val
        if new not in sums:
            sums.append(new)
        else:
            found = True
            print(new)
            break

