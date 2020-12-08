import fileinput

lines = [line.replace("\n", "").split() for line in fileinput.input()]


# Part 1
i = 0
done_indices = []
acc = 0

while not i in done_indices:
    cmd, n = lines[i]
    num = int(n)
    done_indices.append(i)
    if cmd == "acc":
        acc += num
        i += 1
    elif cmd == "nop":
        i += 1
    elif cmd == "jmp":
        i += num

print("part1", acc)


# Part2

idx_to_swap = [i for i, line in enumerate(lines) if line[0] in ["nop", "jmp"]]

for i_swap in idx_to_swap:
    done_indices = []
    acc = 0
    i = 0
    while not i in done_indices:
        if i >= len(lines):
            break
        cmd, n = lines[i]
        num = int(n)
        done_indices.append(i)
        if cmd == "acc":
            acc += num
            i += 1
        elif cmd == "nop":
            if i == i_swap:
                i += num
            else:
                i += 1
        elif cmd == "jmp":
            if i == i_swap:
                i += 1
            else:
                i += num
    if i == len(lines):
        break

print("Part2", acc)
