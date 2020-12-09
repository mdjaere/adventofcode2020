import fileinput

lines = [line.replace("\n", "").split() for line in fileinput.input()]


# Part 1
i = 0
seen = []
acc = 0

while not i in seen:
    cmd, n = lines[i]
    num = int(n)
    seen.append(i)
    if cmd == "acc":
        acc += num
        i += 1
    elif cmd == "nop":
        i += 1
    elif cmd == "jmp":
        i += num

print("part1", acc)


# Part2

for line_to_swap in [idx for idx, line in enumerate(lines) if line[0] in ["jmp", "nop"]]:
    seen = []
    acc = 0
    i = 0
    while not i in seen:
        if not 0 <= i < len(lines):
            break
        cmd, n = lines[i]
        if i == line_to_swap:
            if cmd == "jmp":
                cmd = "nop"
            elif cmd == "nop":
                cmd = "jmp"
        num = int(n)
        seen.append(i)
        if cmd == "acc":
            acc += num
            i += 1
        elif cmd == "nop":
            i += 1
        elif cmd == "jmp":
            i += num
    if i == len(lines):
        break

print("Part2", acc)
