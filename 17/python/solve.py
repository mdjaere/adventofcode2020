import fileinput
import numpy as np

lines = [line.strip().replace(".", "0").replace("#", "1")
         for line in fileinput.input()]

# Part1

start = np.array([[[int(c) for c in line] for line in lines]])

current = np.pad(start.copy(), 2)
iteration = 0

while iteration < 6:
    new = current.copy()
    z_size, y_size, x_size = current.shape
    for z in range(1, z_size-1):
        for y in range(1, y_size-1):
            for x in range(1, x_size-1):
                active = current[z, y, x]
                sample = current[z-1:z+2, y-1:y+2, x-1:x+2]
                sample_count = np.sum(sample) - active
                if active:
                    if not sample_count in [2, 3]:
                        new[z, y, x] = 0
                else:
                    if sample_count == 3:
                        new[z, y, x] = 1
    current = np.pad(new, 1)
    iteration += 1

print("PART 1:", np.sum(new))

# PART 2

start = np.array([[[[int(c) for c in line] for line in lines]]])
current = np.pad(start.copy(), 2)
iteration = 0

while iteration < 6:
    new = current.copy()
    w_size, z_size, y_size, x_size = current.shape
    for w in range(1, w_size-1):
        for z in range(1, z_size-1):
            for y in range(1, y_size-1):
                for x in range(1, x_size-1):
                    active = current[w, z, y, x]
                    sample = current[w-1:w+2, z-1:z+2, y-1:y+2, x-1:x+2]
                    sample_count = np.sum(sample) - active
                    if active:
                        if not sample_count in [2, 3]:
                            new[w, z, y, x] = 0
                    else:
                        if sample_count == 3:
                            new[w, z, y, x] = 1
    current = np.pad(new, 1)
    iteration += 1

print("PART 2:", np.sum(new))
