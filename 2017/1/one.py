f = open("input")

line = f.read().strip()

captcha = [x for x in map(int, list(line))]

l = len(captcha)
half = l//2

captcha.append(captcha[0])

sum1 = 0
sum2 = 0
for i in range(len(captcha)-1):
  if captcha[i] == captcha[i]:
    sum1 += captcha[i]
  if captcha[i] == captcha[(i+half)%l]:
    sum2 += captcha[i]

print(sum1)
print(sum2)


