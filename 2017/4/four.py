passphrases = open("input").read().splitlines()

def valid(passphrase):
  words = passphrase.split(' ')
  words_sorted = list(map(''.join, map(sorted, words)))
  return len(words_sorted) == len(set(words_sorted))

  
count = 0
for passphrase in passphrases:
  if valid(passphrase):
    count += 1

    
print(count)
  
