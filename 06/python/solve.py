import fileinput

lines = [line.strip() for line in fileinput.input()]
lines.append("")  # Ensuring last line is empty

p1 = 0
s = set()
for line in lines:
    if not line:
        # print(s)
        p1 += len(s)
        s = set()
    else:
        s = s.union(set(line))

print(p1, "should be 6782")

p2 = 0
s = set()
new_group = True
for line in lines:
    if not line:
        # print(s)
        p2 += len(s)
        s = set()
        new_group = True
    else:
        if new_group:
            s = set(set(line))
            new_group = False
        else:
            s = s.intersection(set(line))

print(p2, "should be 3596")
