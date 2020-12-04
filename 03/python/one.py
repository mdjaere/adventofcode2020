with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

direction = 3
pos = 0
tree_count = 0

for index, line in enumerate(lines[::1]):
    # print(line)
    remainder = pos % len(line)
    item = line[remainder]
    if index != 0:
        tree_count += item == "#"
    if index < 40:
        print(
            f"{index} {line[0:remainder]}[{item}]{line[remainder + 1:]} {remainder:4} -> {item} {tree_count}")
    pos += direction

print(f"{tree_count} trees hit")
