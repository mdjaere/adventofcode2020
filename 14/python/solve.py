import fileinput
import re
from itertools import chain

lines = [line for line in fileinput.input()]

# PART 1:

mem = dict()

for line in lines:
    if "mask" in line:
        mask = line.split()[-1]
    if "mem" in line:
        addr, value = re.findall(r"\d+", line)
        str_bin = [c for c in f"{int(value):036b}"]
        for i, m in enumerate(mask):
            if m != "X":
                str_bin[i] = m
        mem[addr] = int("".join(str_bin), base=2)

print("Part 1:", sum(mem.values()))


# PART 2

mem = dict()


def find_addresses(addr_bin):
    if "X" not in addr_bin:
        return [addr_bin]
    index = addr_bin.index("X")
    new_addresses = []
    for bit in ["0", "1"]:
        new_addr = list(addr_bin)
        new_addr[index] = bit
        new_addresses.append(new_addr)
    return list(chain.from_iterable([find_addresses(addr) for addr in new_addresses]))


for line in lines:
    if "mask" in line:
        mask = line.split()[-1]
    if "mem" in line:
        addr, value = re.findall(r"\d+", line)
        addr_bin = [c for c in f"{int(addr):036b}"]
        for i, m in enumerate(mask):
            if m == "1":
                addr_bin[i] = "1"
            if m == "X":
                addr_bin[i] = "X"

        all_addr = find_addresses(addr_bin)

        for addr in all_addr:
            mem[int("".join(addr), base=2)] = int(value)

print("Part 2:", sum(mem.values()))
