import numpy as np
from functools import reduce
from collections import deque

raw = open("input.txt").read()

tile_transforms = [
    lambda m: m,
    lambda m: np.rot90(m, k=1),
    lambda m: np.rot90(m, k=2),
    lambda m: np.rot90(m, k=3),
    lambda m: np.fliplr(m),
    lambda m: np.rot90(np.fliplr(m), k=1),
    lambda m: np.rot90(np.fliplr(m), k=2),
    lambda m: np.rot90(np.fliplr(m), k=3)
]

class Tile:
    def __init__(self, text_tile):
        self.id = int(text_tile[0].split()[1].strip(":"))
        self.org_data = np.array([[c for c in line] for line in text_tile[1:]])
        self.variant = 6 # To match up with example orientation
        self.variants = range(len(tile_transforms))
        self.connections = [
            None,
            None,
            None,
            None
        ]
        self.locked = False

    def __repr__(self):
        return "\n" + "\n".join([" ".join(d) for d in self.data()])
        # return str(self.id)

    def data(self):
        return tile_transforms[self.variant](self.org_data)
    
    def cropped(self):
        return self.data()[1:-1, 1:-1]

    def edges(self):
        return [
            self.data()[0, :],
            self.data()[:, -1],
            self.data()[-1, :],
            self.data()[:, 0]
        ]

    def set_variant(self, x):
        if not self.locked:
            self.variant = x
        return self


tiles = [Tile(text_tile.split("\n")) for text_tile in raw.split("\n\n")]

tiles[0].locked = True
q = deque([tiles[0]])
done = []

while q:
    tile = q.popleft()
    for i, edge_connection in enumerate(tile.connections):
        if edge_connection == None:
            found = False
            edge = tile.edges()[i]
            for candidate in tiles:
                if candidate in done:
                    continue
                for variant in candidate.variants:
                    if not candidate.locked:
                        candidate.set_variant(variant)
                    candidate_opposite_edge_id = (i + 2) % 4
                    if np.all(edge == candidate.edges()[candidate_opposite_edge_id]):
                        tile.connections[i] = candidate
                        candidate.connections[candidate_opposite_edge_id] = tile
                        candidate.locked = True
                        q.append(candidate)
                        found = True
                        break
                    if candidate.locked:
                        break
                if found:
                    break
    done.append(tile)

corners_pieces = [tile for tile in tiles if tile.connections.count(None) == 2]

print("Part 1:", reduce(lambda a, b: a*b, [tile.id for tile in corners_pieces]))

#### Part 2

top_left = [tile for tile in tiles if tile.connections[0]
            == None and tile.connections[3] == None][0]

rows_starters = [top_left]
new = rows_starters[-1].connections[2]
while new:
    rows_starters.append(new)
    new = rows_starters[-1].connections[2]

sorted_tiles = []
for first in rows_starters:
    row = []
    next_tile = first
    while next_tile:
        row.append(next_tile)
        next_tile = row[-1].connections[1]
    sorted_tiles.append(row)

image = np.vstack([np.hstack([tile.cropped() for tile in tiles]) for tiles in sorted_tiles])

# for row_str in ["".join(r) for r in image]:
#     print(row_str)

monster = np.array([
    [c for c in "                  # "],
    [c for c in "#    ##    ##    ###"],
    [c for c in " #  #  #  #  #  #   "]
])

hash_count = (monster == "#").sum()

monster_count = 0

for transform in tile_transforms:
    morphed_monster = transform(monster)
    monstershape = morphed_monster.shape

    for i in range(image.shape[0] - monstershape[0]):
        for j in range(image.shape[1] - monstershape[1]):
            sample = image[i:i + monstershape[0], j:j + monstershape[1]]
            found = (sample == morphed_monster).sum() == hash_count
            if found:
                monster_count += 1

wave_count = (image == "#").sum() - (monster_count * hash_count)

print("Part 2:", wave_count)
