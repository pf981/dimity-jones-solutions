import itertools

import decrypter


#   ....
#   . .
#    . .
#   ....
#   ..
#   .
#    .
#   ..
#     ..
#     .
#      .
#     ..
#   ....
#   . .
#    . .
#   ....
#

# offsets = [(0, 0), (0, -1), (-1, 1), (2, 0), (3, 0), (3, -1)]


# def gen_part(depth, part):
#     dr, dc = offsets[part]
#     if depth == 0:
#         yield dr, dc
#     else:
#         for r2, c2 in gen_part(depth - 1, part):
#             yield dr + r2 * 4, dc + c2 * 4


# # This can have duplicates - just check
# def gen_positions():
#     yield from gen_part(0, 0)
#     for depth in itertools.count():
#         for part in range(1, 6):
#             yield from gen_part(depth, part)


# def super_s(cipher: str):
#     result = {}
#     for (r, c), ch in zip(gen_positions(), cipher, strict=False):
#         result[(r, c)] = ch

#     return "".join(result[pos] for pos in sorted(result))


# list(itertools.islice(gen_positions(), 100))

offsets = [(0, 0), (0, -1), (1, -1), (2, 0), (3, 0), (3, -1)]
S_HEIGHT = 4  # height of smallest S
S_WIDTH = 2  # width of smallest S


def gen_part(depth, part):
    dr, dc = offsets[part]
    if depth == 0:
        yield dr, dc
    else:
        for r2, c2 in range_positions(depth - 1):
            yield dr * S_HEIGHT + r2, dc * S_WIDTH + c2


def range_positions(depth):
    if not depth:
        yield from gen_part(depth, 0)
    for part in range(1, 6):
        yield from gen_part(depth, part)


def gen_positions_for_cipher(cipher):
    # coords = []
    # seen = set()
    yield from gen_part(0, 0)
    for depth in itertools.count():
        for part in range(1, 6):
            yield from gen_part(depth, part)
            # if pos in seen:
            #     continue
            # seen.add(pos)
            # coords.append(pos)
            # if len(coords) == len(cipher):
            #     return coords
    # return coords


def super_s(cipher):
    result = {}
    for (r, c), ch in zip(gen_positions_for_cipher(cipher), cipher):
        result[(r, c)] = ch
    return "".join(result[pos] for pos in sorted(result))


def test_super_s(cipher):
    result = {}
    min_r = max_r = min_c = max_c = 0
    for (r, c), ch in zip(gen_positions_for_cipher(cipher), cipher):
        print(f"{r=} {c=}")
        assert (r, c) not in result
        result[(r, c)] = ch
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)

    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            print(result.get((r, c), "."), end="")
        print()


# test_super_s("1234567")
# test_super_s("123456789abcdefghijkl")
s = "0123456789" * 10
test_super_s(s)
# test_super_s("123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
# ...
# test_super_s("12")
# test_super_s("123")

# test_super_s("123456")
# # Correctly gives:
# # 21
# # 3.
# # .4
# # 65

# test_super_s("1234567")
# Incorrectly gives:
# 27
# 3.
# .4
# 65
#
# Should be:
# 721
# .3.
# ..4
# .65


# # 4x2 basic S
# offsets = [(0, 0), (0, -1), (1, -1), (2, 0), (3, 0), (3, -1)]
# S_HEIGHT = 4
# S_WIDTH = 2

# # cache sizes of an S at each depth (in character cells)
# HEIGHTS = {0: S_HEIGHT}
# WIDTHS = {0: S_WIDTH}


# def size_at(depth):
#     if depth not in HEIGHTS:
#         for d in range(1, depth + 1):
#             if d not in HEIGHTS:
#                 HEIGHTS[d] = HEIGHTS[d - 1] * S_HEIGHT
#                 WIDTHS[d] = WIDTHS[d - 1] * S_WIDTH
#     return HEIGHTS[depth], WIDTHS[depth]


# def range_positions(depth):
#     """All (r,c) in traversal order for a full S at `depth`."""
#     if depth == 0:
#         for r, c in offsets:
#             yield r, c
#     else:
#         H, W = size_at(depth - 1)
#         for dr, dc in offsets:  # which tile (0..5)
#             for r2, c2 in range_positions(depth - 1):  # inside that tile
#                 yield dr * H + r2, dc * W + c2


# def gen_part(depth, part):
#     """All (r,c) for just one part (0..5) of an S at `depth`."""
#     if depth == 0:
#         yield offsets[part]
#     else:
#         H, W = size_at(depth - 1)
#         dr, dc = offsets[part]
#         for r2, c2 in range_positions(depth - 1):
#             yield dr * H + r2, dc * W + c2


# def gen_positions_for_cipher(n_chars):
#     """Emit positions for exactly n_chars, growing S -> super-S -> ..."""
#     emitted = 0
#     # First, the basic S (depth 0), parts 0..5
#     for p in range(6):
#         for pos in gen_part(0, p):
#             yield pos
#             emitted += 1
#             if emitted == n_chars:
#                 return
#     # Then, for each larger depth, only add parts 1..5
#     depth = 1
#     while emitted < n_chars:
#         for p in range(1, 6):
#             for pos in gen_part(depth, p):
#                 yield pos
#                 emitted += 1
#                 if emitted == n_chars:
#                     return


# def super_s(cipher: str):
#     result = {}
#     for (r, c), ch in zip(gen_positions_for_cipher(len(cipher)), cipher):
#         result[(r, c)] = ch
#     # row-major readout (top-to-bottom, left-to-right)
#     min_r = min(r for r, _ in result)
#     min_c = min(c for _, c in result)
#     max_r = max(r for r, _ in result)
#     max_c = max(c for _, c in result)
#     out = []
#     for r in range(min_r, max_r + 1):
#         for c in range(min_c, max_c + 1):
#             if (r, c) in result:
#                 out.append(result[(r, c)])
#     return "".join(out)


# def draw(cipher: str) -> str:
#     grid = {}
#     for (r, c), ch in zip(gen_positions_for_cipher(len(cipher)), cipher):
#         grid[(r, c)] = ch
#     min_r = min(r for r, _ in grid)
#     max_r = max(r for r, _ in grid)
#     min_c = min(c for _, c in grid)
#     max_c = max(c for _, c in grid)
#     lines = []
#     for r in range(min_r, max_r + 1):
#         line = []
#         for c in range(min_c, max_c + 1):
#             line.append(grid.get((r, c), "."))
#         lines.append("".join(line))
#     return "\n".join(lines)


# print(draw("123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))


@decrypter.decrypter(chapter=86)
def decrypt(cipher: str) -> str:
    return super_s(cipher)
