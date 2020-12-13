import fileinput
import numpy as np

lines = [line.strip() for line in fileinput.input()]
seats = np.array([[c for c in line] for line in lines])

# Part 1

def count_adjacent(c_seats, c, r):
    padded = np.pad(c_seats, 1)

    surr = padded[c:c+3, r:r+3]
    surr[1, 1] = "O"

    count = surr[surr == "#"]

    return len(count)


last_count = -1
unstable = True

n_rows, n_cols = seats.shape

ref_seats = seats.copy()

while unstable:
    new_seats = ref_seats.copy()
    for r in range(n_rows):
        for c in range(n_cols):
            if new_seats[r, c] != ".":
                if new_seats[r, c] == "L" and count_adjacent(ref_seats, r, c) == 0:
                    new_seats[r, c] = "#"
                elif new_seats[r, c] == "#" and count_adjacent(ref_seats, r, c) >= 4:
                    new_seats[r, c] = "L"
    count = len(new_seats[new_seats == "#"])
    print(count)
    if count == last_count:
        unstable = False
    ref_seats = new_seats.copy()
    last_count = count

print("p1", last_count)

# Part 2

directions = {
    "n": [0, -1],
    "ne": [1, -1],
    "e": [1, 0],
    "se": [1, 1],
    "s": [0, 1],
    "sw": [-1, 1],
    "w": [-1, 0],
    "nw": [-1, -1]
}


def count_visible(c_seats, r, c):
    padded_seats = np.pad(c_seats, 1)
    place = np.array([r+1, c+1])
    padded_seats[place[0], place[1]] = "O"

    count = 0

    for d in directions.values():
        current = place.copy()
        done_dir = False
        while not done_dir:
            current += d
            v = padded_seats[current[0], current[1]]
            if v == "#":
                count += 1
                done_dir = True
            elif v == "L" or v == "0":
                done_dir = True

    return count


last_count = -1
unstable = True

n_rows, n_cols = seats.shape

ref_seats = seats.copy()

while unstable:
    new_seats = ref_seats.copy()
    for r in range(n_rows):
        for c in range(n_cols):
            if new_seats[r, c] != ".":
                if new_seats[r, c] == "L" and count_visible(ref_seats, r, c) == 0:
                    new_seats[r, c] = "#"
                elif new_seats[r, c] == "#" and count_visible(ref_seats, r, c) >= 5:
                    new_seats[r, c] = "L"
    count = len(new_seats[new_seats == "#"])
    print(count)
    if count == last_count:
        unstable = False
    ref_seats = new_seats.copy()
    last_count = count

print("p2", last_count)
