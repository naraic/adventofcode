events = open("input").read().splitlines()

events.sort()


def get_guard(event):
  guard = event.split('#')[1].split(' ')[0]
  return guard

def get_minute(event):
  minute = event.split(':')[1][:2]
  return int(minute)

records = {}
record = [0]*60

for event in events:
  if "Guard" in event:
    curr_guard = get_guard(event)
    if curr_guard not in records:
      records[curr_guard] = record.copy()
  elif "falls asleep" in event:
    falls_asleep = get_minute(event)
  else:
    wake_up = get_minute(event)
    for time in range(falls_asleep, wake_up+1):
      records[curr_guard][time] += 1 

maximum = 0
worst_minute = 0
for elf, record in records.items():
  curr = sum(record)
  curr_minute = max(record)
  if curr > maximum:
    sleepy = elf
    maximum = curr
  if curr_minute > worst_minute:
    momentarily_sleepy = elf
    worst_minute = curr_minute

sleepiest_minute = records[sleepy].index(max(records[sleepy]))
print(int(sleepy) * sleepiest_minute)
print(records[momentarily_sleepy].index(worst_minute) * int(momentarily_sleepy))
