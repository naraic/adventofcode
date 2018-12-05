polymer = open("input").read().strip()

magic_no = ord('a') - ord('A')


def react(polymer):
  polymer = list(map(ord,list(polymer)))
  while(True):
    found = False
    for index, mer in enumerate(polymer[:-1]):
      if abs(mer - polymer[index+1]) == magic_no:
        polymer = polymer[:index] + polymer[index+2:]
        found = True
        break
    if not found:
      break     
  return ''.join(map(chr,list(polymer)))

reacted = react(polymer)
import string
min = len(reacted)
print(min)

for c in string.ascii_lowercase:
  polymer = reacted.replace(c, "")
  polymer = polymer.replace(c.upper(), "")
  rereacted = react(polymer)
  if len(rereacted) < min:
    min = len(rereacted)
print(min)


