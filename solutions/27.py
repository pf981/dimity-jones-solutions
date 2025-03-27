import decrypter
import itertools


def rot_left(grid, r, c):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    grid_values = [grid[r + dr][c + dc] for dr, dc in deltas]
    for (dr, dc), value in zip(deltas, grid_values[1:] + [grid_values[0]]):
        grid[r + dr][c + dc] = value


def rot_right(grid, r, c):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    grid_values = [grid[r + dr][c + dc] for dr, dc in deltas]
    for (dr, dc), value in zip(deltas, [grid_values[-1]] + grid_values[:-1]):
        grid[r + dr][c + dc] = value


grid = [list(row) for row in itertools.batched(range(1, 50), 7)]

for move in "RCw CCw RBc LTw RTw CCw LBw CBc CBc CTc LCc CCc CCc RTw".split():
    c, r, direction = move
    c = "LCR".index(c) * 2 + 1
    r = "TCB".index(r) * 2 + 1
    f = rot_right if direction == "c" else rot_left
    print(f"{r=} {c=} {direction=}")
    f(grid, r, c)


@decrypter.decrypter(chapter=27)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [num for line in grid for num in line])
