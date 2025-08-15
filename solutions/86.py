import itertools

import decrypter

# I don't get what this "S" is supposed to look like.
# [(0, 0), (0, -1), (1, -1), (2, 0), (3, 0), (3, -1)] was not correct
offsets = [(0, 0), (0, -1), (2, -1), (2, 0), (3, 0), (3, -1)]
S_HEIGHT = 4
S_WIDTH = 2


def gen_part(depth, part):
    dr, dc = offsets[part]
    if depth == 0:
        yield dr, dc
    else:
        for r2, c2 in range_positions(depth - 1):
            scale_r = S_HEIGHT**depth
            scale_c = S_WIDTH**depth
            yield dr * scale_r + r2, dc * scale_c + c2


def range_positions(depth):
    for part in range(6):
        yield from gen_part(depth, part)


def gen_positions_for_cipher(cipher):
    yield from gen_part(0, 0)

    for depth in itertools.count():
        for part in range(1, 6):
            yield from gen_part(depth, part)


def super_s(cipher):
    result = {}
    for (r, c), ch in zip(gen_positions_for_cipher(cipher), cipher):
        result[(r, c)] = ch
    return "".join(result[pos] for pos in sorted(result))


@decrypter.decrypter(chapter=86)
def decrypt(cipher: str) -> str:
    return super_s(cipher)
