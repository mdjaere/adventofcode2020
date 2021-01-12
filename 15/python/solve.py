import fileinput
from collections import defaultdict

start_numbers = [int(x) for x in next(fileinput.input()).split(",")]

# PART 1

record = list(start_numbers)
turn = len(start_numbers)

while turn < 2020:
    last = record[-1]
    prev = record[0:-1]
    prev_rev = prev[::-1]
    if last not in prev_rev:
        new = 0
    else:
        new = prev_rev.index(last) + 1
    record.append(new)
    turn += 1

print("PART 1:", new)


# Part 2

seen = defaultdict(int)
turn = 1

for said in start_numbers:
    last_seen = seen[said]
    seen[said] = turn
    turn += 1

while turn < 30000001:
    if last_seen == 0:
        # Never seen
        said = 0
    else:
        # Seen before
        said = turn - 1 - last_seen
    last_seen = seen[said]
    seen[said] = turn
    turn += 1

print("Part 2:", said)
