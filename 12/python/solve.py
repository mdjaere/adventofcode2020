import fileinput
import numpy as np

commands = [(line[0], int(line[1:].strip())) for line in fileinput.input()]

direction = np.array([1, 0, 1])
position = np.array([0, 0, 1])

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.


def get_translation(cmd, v):
    res = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    if cmd == "N":
        res[1, 2] = -v
    elif cmd == "S":
        res[1, 2] = v
    elif cmd == "E":
        res[0, 2] = v
    elif cmd == "W":
        res[0, 2] = -v
    return res


def get_rotation(cmd, vdeg):
    vrad = np.radians(vdeg)
    if cmd == "R":
        return np.array([
            [np.cos(-vrad), np.sin(-vrad), 0],
            [-np.sin(-vrad), np.cos(-vrad), 0],
            [0, 0, 1]
        ])
    if cmd == "L":
        return np.array([
            [np.cos(vrad), np.sin(vrad), 0],
            [-np.sin(vrad), np.cos(vrad), 0],
            [0, 0, 1]
        ])


for cmd, amount in commands:
    if cmd in ["F"]:
        a = position + direction * amount
        a[2] = 1
        position = a
    elif cmd in ["N", "S", "E", "W"]:
        transform = get_translation(cmd, amount)
        position = transform @ position
    elif cmd in ["L", "R"]:
        transform = get_rotation(cmd, amount)
        direction = np.round(transform @ direction).astype(np.int)

print("P1", abs(position[0]) + abs(position[1]))

# Part 2

# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left(counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right(clockwise) the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal to the given value.
# The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship
# that is, if the ship moves, the waypoint moves with it.

waypoint = np.array([10, -1, 1])
position2 = np.array([0, 0, 1])

for cmd, amount in commands:
    if cmd in ["F"]:
        a = position2 + waypoint * amount
        a[2] = 1
        position2 = a
    elif cmd in ["N", "S", "E", "W"]:
        transform = get_translation(cmd, amount)
        waypoint = transform @ waypoint
    elif cmd in ["L", "R"]:
        transform = get_rotation(cmd, amount)
        waypoint = np.round(transform @ waypoint).astype(np.int)

print("P2", abs(position2[0]) + abs(position2[1]))
