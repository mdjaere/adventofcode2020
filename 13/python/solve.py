import fileinput

notes = [note.strip() for note in fileinput.input()]
time = int(notes[0])
busses = [{"id": int(route), "offset": int(offset)}
          for offset, route in enumerate(notes[1].split(",")) if route != "x"]

# Part 1

first_bus = sorted([[bus["id"], bus["id"] - time % bus["id"]]
                    for bus in busses], key=lambda x: x[1])[0]

print("Part 1:", first_bus[0] * first_bus[1])

# Part 2

time = 1
jump = 1
for bus in busses:
    while not (time + bus["offset"]) % bus["id"] == 0:
        time += jump
    jump *= bus["id"]

print("Part 2:", time)
