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


offsets = [(0, 0), (0, -1), (1, -1), (2, 0), (3, 0), (3, -1)]
S_HEIGHT = 4  # height of smallest S
S_WIDTH = 2  # width of smallest S


def gen_part(depth, part):
    dr, dc = offsets[part]
    # print(f"Gen part {depth=} {part=} {dr=} {dc=}")
    if depth == 0:
        yield dr, dc
    else:
        for r2, c2 in range_positions(depth - 1):
            # yield dr * depth * S_HEIGHT + r2, dc * depth * S_WIDTH + c2
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


def test_super_s(cipher):
    result = {}
    min_r = max_r = min_c = max_c = 0
    for (r, c), ch in zip(gen_positions_for_cipher(cipher), cipher):
        print(f"{r=} {c=} {ch=}")
        if (r, c) in result:
            print(f"### FAILED at {(r, c)=} ###")
            break
        result[(r, c)] = ch
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)

    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            print(result.get((r, c), "."), end="")
        print()


# test_super_s("123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10)
# Gen part depth=0 part=0 dr=0 dc=0
# r=0 c=0 ch='1'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=0 c=-1 ch='2'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=1 c=-1 ch='3'
# Gen part depth=0 part=3 dr=2 dc=0
# r=2 c=0 ch='4'
# Gen part depth=0 part=4 dr=3 dc=0
# r=3 c=0 ch='5'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=3 c=-1 ch='6'
# Gen part depth=1 part=1 dr=0 dc=-1
# Gen part depth=0 part=0 dr=0 dc=0
# r=0 c=-2 ch='7'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=0 c=-3 ch='8'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=1 c=-3 ch='9'
# Gen part depth=0 part=3 dr=2 dc=0
# r=2 c=-2 ch='a'
# Gen part depth=0 part=4 dr=3 dc=0
# r=3 c=-2 ch='b'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=3 c=-3 ch='c'
# Gen part depth=1 part=2 dr=1 dc=-1
# Gen part depth=0 part=0 dr=0 dc=0
# r=4 c=-2 ch='d'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=4 c=-3 ch='e'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=5 c=-3 ch='f'
# Gen part depth=0 part=3 dr=2 dc=0
# r=6 c=-2 ch='g'
# Gen part depth=0 part=4 dr=3 dc=0
# r=7 c=-2 ch='h'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=7 c=-3 ch='i'
# Gen part depth=1 part=3 dr=2 dc=0
# Gen part depth=0 part=0 dr=0 dc=0
# r=8 c=0 ch='j'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=8 c=-1 ch='k'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=9 c=-1 ch='l'
# Gen part depth=0 part=3 dr=2 dc=0
# r=10 c=0 ch='m'
# Gen part depth=0 part=4 dr=3 dc=0
# r=11 c=0 ch='n'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=11 c=-1 ch='o'
# Gen part depth=1 part=4 dr=3 dc=0
# Gen part depth=0 part=0 dr=0 dc=0
# r=12 c=0 ch='p'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=12 c=-1 ch='q'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=13 c=-1 ch='r'
# Gen part depth=0 part=3 dr=2 dc=0
# r=14 c=0 ch='s'
# Gen part depth=0 part=4 dr=3 dc=0
# r=15 c=0 ch='t'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=15 c=-1 ch='u'
# Gen part depth=1 part=5 dr=3 dc=-1
# Gen part depth=0 part=0 dr=0 dc=0
# r=12 c=-2 ch='v'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=12 c=-3 ch='w'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=13 c=-3 ch='x'
# Gen part depth=0 part=3 dr=2 dc=0
# r=14 c=-2 ch='y'
# Gen part depth=0 part=4 dr=3 dc=0
# r=15 c=-2 ch='z'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=15 c=-3 ch='A'
# Gen part depth=2 part=1 dr=0 dc=-1
# Gen part depth=1 part=0 dr=0 dc=0
# Gen part depth=0 part=0 dr=0 dc=0
# r=0 c=-4 ch='B'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=0 c=-5 ch='C'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=1 c=-5 ch='D'
# Gen part depth=0 part=3 dr=2 dc=0
# r=2 c=-4 ch='E'
# Gen part depth=0 part=4 dr=3 dc=0
# r=3 c=-4 ch='F'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=3 c=-5 ch='G'
# Gen part depth=1 part=1 dr=0 dc=-1
# Gen part depth=0 part=0 dr=0 dc=0
# r=0 c=-6 ch='H'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=0 c=-7 ch='I'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=1 c=-7 ch='J'
# Gen part depth=0 part=3 dr=2 dc=0
# r=2 c=-6 ch='K'
# Gen part depth=0 part=4 dr=3 dc=0
# r=3 c=-6 ch='L'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=3 c=-7 ch='M'
# Gen part depth=1 part=2 dr=1 dc=-1
# Gen part depth=0 part=0 dr=0 dc=0
# r=4 c=-6 ch='N'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=4 c=-7 ch='O'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=5 c=-7 ch='P'
# Gen part depth=0 part=3 dr=2 dc=0
# r=6 c=-6 ch='Q'
# Gen part depth=0 part=4 dr=3 dc=0
# r=7 c=-6 ch='R'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=7 c=-7 ch='S'
# Gen part depth=1 part=3 dr=2 dc=0
# Gen part depth=0 part=0 dr=0 dc=0
# r=8 c=-4 ch='T'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=8 c=-5 ch='U'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=9 c=-5 ch='V'
# Gen part depth=0 part=3 dr=2 dc=0
# r=10 c=-4 ch='W'
# Gen part depth=0 part=4 dr=3 dc=0
# r=11 c=-4 ch='X'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=11 c=-5 ch='Y'
# Gen part depth=1 part=4 dr=3 dc=0
# Gen part depth=0 part=0 dr=0 dc=0
# r=12 c=-4 ch='Z'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=12 c=-5 ch='1'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=13 c=-5 ch='2'
# Gen part depth=0 part=3 dr=2 dc=0
# r=14 c=-4 ch='3'
# Gen part depth=0 part=4 dr=3 dc=0
# r=15 c=-4 ch='4'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=15 c=-5 ch='5'
# Gen part depth=1 part=5 dr=3 dc=-1
# Gen part depth=0 part=0 dr=0 dc=0
# r=12 c=-6 ch='6'
# Gen part depth=0 part=1 dr=0 dc=-1
# r=12 c=-7 ch='7'
# Gen part depth=0 part=2 dr=1 dc=-1
# r=13 c=-7 ch='8'
# Gen part depth=0 part=3 dr=2 dc=0
# r=14 c=-6 ch='9'
# Gen part depth=0 part=4 dr=3 dc=0
# r=15 c=-6 ch='a'
# Gen part depth=0 part=5 dr=3 dc=-1
# r=15 c=-7 ch='b'
# Gen part depth=2 part=2 dr=1 dc=-1
# Gen part depth=1 part=0 dr=0 dc=0
# Gen part depth=0 part=0 dr=0 dc=0
# r=8 c=-4 ch='c'
# ### FAILED at (r, c)=(8, -4) ###
# IHCB8721
# J.D.9.3.
# .K.E.a.4
# MLGFcb65
# ON..ed..
# P...f...
# .Q...g..
# SR..ih..
# ..UT..kj
# ..V...l.
# ...W...m
# ..YX..on
# 761Zwvqp
# 8.2.x.r.
# .9.3.y.s
# ba54Azut


# test_super_s("12345")
# test_super_s("123456789abcdefghijkl")
# s = "0123456789" * 10
# test_super_s(s)
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
# 721
# .3.
# ..4
# .65
# ...


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
