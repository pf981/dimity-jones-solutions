import decrypter


# def do_move(state: list[int], move: str) -> None:
#     match move:
#         case "Lc":
#             order = [5, 0, 1, 3, 4, 10, 6, 2, 8, 9, 11, 12, 7, 13, 14]
#         case "Lw":
#             order = [1, 2, 7, 3, 4, 0, 6, 12, 8, 9, 5, 10, 11, 13, 14]
#         case "Rc":
#             order = [0, 1, 7, 2, 3, 5, 6, 12, 8, 4, 10, 11, 13, 14, 9]
#         case "Rw":
#             order = [0, 1, 3, 4, 9, 5, 6, 2, 8, 14, 10, 11, 7, 12, 13]
#     state[:] = [state[i] for i in order]


# # 0  1  2  3  4
# # 5  6  7  8  9
# # 10 11 12 13 14

# # Lc
# # 5  0  1  3  4
# # 10 6  2  8  9
# # 11 12 7 13 14

# # Lw
# # 1  2  7  3  4
# # 0  6  12 8  9
# # 5  10 11 13 14

# # Rc
# # 0  1  7  2  3
# # 5  6  12 8  4
# # 10 11 13 14 9

# # Rw
# # 0  1  3  4  9
# # 5  6  2  8 14
# # 10 11 7  12 13

# # L -> 6
# # R -> 8
# # c -> Clockwise
# # w -> Counterclockwise


# def find_solution() -> str:
#     text = """
#     Lw Rc Rc Lc Lc Rc Rw Rc Rw Rc Rw Rc Rw Lc Rw Rw Lc Lc Lw Rc Lc Lc Lc Lc Rw Rw Rw Rw Rc Lw Lw Lc Rw Lc Lc Lc Lw Lc Rc Rc Rw Lw Rw Lc Lw Rw Lc Lc Lc Lw Rw Rc Rw Lc Rc Rw Rw Lc Lc Lw Rw Lc Lw Rw Lc Rw Rc Rw Rc Lw Rc Lw Lw Lw Lc Rw Rc Rw Rc Lw Lw Rc Rw Lc Lw Rc Rw Lc Lc Rc Lc Rc Lw Lc Lw Rc Rc Lc Lw Rw Lc Rw Rc Rc Lc Lc Lc Lw Rw Lw Lw Rc Lw Lw Rc Lw Lw Rc Rc Rc Lw Lc Rw Rw Lc Rw Rc Rw Lc Lw Rc Rw Rw Lc Rw Lw Lw Rc Rw Rc Lw Rw Lw Lw Lw Rc Rc Rw Lc Lw Lw Rw Lw Lc Lc Lc Rc Lc Rw Lc Rw Rc Lw Rc Lc Rw Rw Lc Lc Lw Rc Lw Lc Lw Lw Rc Lc Lw Lw Lw Rc Lc Lw Rw Lc Rw Rw Lw Lc Lw Lc Rc Rc Rc Rw Rw Rc Rw Lc Rw Rw Rw Rc Lw Lc Lc Rw Rc Rw Rw Rw Lc Lw Lc Rc Rw Rw Lc Lc Lc Rw Rw Rw Lw Rw Lc Lw Rc Rc Lw Rw Rc Lw Rc Rc Lc Rc Rc Rw Rw Lc Lc Rc Lw Rc Rw Lc Rw Lc Lc Rw Lc Lw Rw Rc Lw Lc Rc Rw Rc Lc Lw Lc Rc Lc Lw Lc Lc Rw Lc Rc Lw Lw Lc Rw Rc Lw Rw Lw Rc Lc Lc Rw Rc Rw Rw Lc Lw Rc Rw Lc Rc Lc Rc Lc Lc Lw Rc Rc Lc Lw Lc Rw Lc Lc Rc Lw Rc Rw Lc Rw Lc Lc Rw Lc Lw Rw Rc Lw Lc Rc Rw Rc Lc Lw Lc Rc Lc Lw Lc Lc Rw Lc Rc Lw Lw Lc Rw Rc Lw Rw Lw Rc Lc Lc Rw Rc Rw Rw Lc Lw Rc Rw Lc Rc Lc Rc Lc Lc Lw Rc Rc Lc Lw Lc Rw Lc Lc Rc Lw Rc Rw Lc Rw Lc Lc Rw Lc Lw Rw Rc Lw Lc Rc Rw Rc Lc Lw Lc Rc Lc Lw Lc Lc Rw Lc Rc Lw Lw Lc Rw Rc Lw Rw Lw Rc Lc Lc Rw Rc Rw Rw Lc Lw Rc Rw Lc Rc Lc Rc Lc Lc Lw Rc Rc Lc Lw Lc Rw Rw Lw Rw Rw Lw Lc Rc Rc Rc Lw Lc Rw Lc Rw Rc Lw Lc Rc Lw Lw Rc Lc Rc Rc Rw Rw Lw Lw Lw Rc Lc Lw Lc Rw Rw Lc Rw Rc Lw Lc Lc Lw Lw Rw Lc Rw Rc Rc Rw Lw Lw Lw Rc Lw Lc Lw Lw Lc Lw Rc Lc Rc Rc Lc Rw Rw Rw Rc Rw Lw Rc Lc Rc Rc Rc Lw Lw Rc Lw Lw Rw Lw Lw Rc Rc Lw Rc Rc Lc Rw Rw Rw Lc Lw Lc Rc Rc Lw Lc Lw Lw Lc Rw Rw Rw Lc Rw Rw Lw Lw Rw Lc Lw Lw Rw Rw Rc Rc Lw Rc Lw Rc Lc Rc Lw Lc Lc Rc Lw Lw Rc Rc Lw Lw Rc Rw Rc Lw Rw Rw Lw Rw Lc Rw Lw Rc Rc Rc Rc Lw Lc Rw Rc Rc Rc Lw Rc Rw Rw Lw Lw Lw Rw Lc Lw Rc Rc Lw Rw Lc Rc Rw Rc Rw Lw Lc Lc Rw Lc Lc Rc Rc Lc Lc Lw Rw Lc Lc Lw Rc Rc Rw Lw Lw Rc Lc Lc Rc Rw Rw Lc Rc Lc Rc Lw Rw Lw Lw Lc Rc Lw Rw Rw Lc Rc Lw Rw Rc Rw Lw Rc Lw Lc Rc Lc Lc Rc Lw Rw Rc Lc Rc Lw Rw Rc Lc Lc Rc Lw Rw Rc Rc Rc Lw Lc Lw Lw Rw Lw Lc Rc Lw Rw Lc Lw Lc Rc Lw Rw Lc Rc Lw Rw Lc Rw Rw Rw Rc Lc Rc Lw Rw Rw Rc Lw Lw Lw Lw Lw Lc Rc Lw Rw Rc Rw Rc Lc Rc Rc Rc Lw Rw Rw Rc Lc Rc Lw Rw Lc Rc Lw Rw Lw Rw Rc Rw Lw Lc Rc Lw Rw Lw Lw Rw Rw Lc Lc Lw Lw Lc Rc Lw Rw Lw Lc Lc Rw Rc Lc Lc Rc Lc Lw Lc Lw Rw Rw Rc Rc Rw Lw Rc Lw Lc Rc Rc Lc Rc Lw Rw Lc Lw Lc Lc Rc Lw Rw Rw Rw Lc Lc Rc Lc Rc Lw Rw Lc Rc Lw Rw Rc Lc Rw Lw Lc Lc Rc Lw Rw Lw Lc Rc Lw Rw Lc Rc Lw Lw Rw Rw Rc Rw Rc Rc Lw Rw Rw Lc Rc Lw Rw Lw Rw Rw Lw Lc Rc Lw Rw Rc Lc Rc Rc Lc Rc Lw Rw Rw Lc Rc Lw Rw Lc Lw Lw Lc Rc Lw Rw Rc Rw Lw Lc Lc Lw Lc Rc Lw Rw Rc Lc Lc Rc Lw Rw Lc Lc Rc Lw Rw Lc Rc Lw Rw Lw Lc Rc Lw Rw Rw Lw Lw Rw Lc Rc Lw Rw Lc Rc Lw Rw Rw Lc Rw Rw Rc Lc Rc Lw Rw Lw Rc Rc Rw Rw Rw Rc Lw Lc Lc Rc Rc Lc Rc Lw Rw Rc Lc Rc Lw Rw Lc Rc Lw Rw Rc Rw Lc Rw Lw Rw Lc Lc Rc Lw Rw Lw Lw Rc Rw Lw Lc Lc Rc Lw Rw Lw Lc Lc Lc Rc Lw Rw Lw Rc Lc Rc Lw Rw Rw Lc Rw Lc Rc Lw Rw Rc Lc Lc Rc Lw Rw Lw Rw Lc Rc Lw Rw Lw Lc Lc Rc Lw Rw Lw Rw Lc Lc Rc Lw Rw Lw Rc Lc Rc Rc Rc Lw Lw Lw Rw Rw Lc Rc Rw Rw Rw Rw Rc Lc Rc Lw Rw Lc Rc Lw Rw Rc Lc Rc Lw Rw Rw Lw Lw Lc Rc Lw Rw Rc Lc Lw Lc Lc Rc Lw Rw Lw Rw Lc Rc Lw Rw Rw Lc Lc Rc Lw Rw Lw Rc Lc Lc Rc Lw Rw Lw Lc Rc Lw Rw Lc Lw Lc Lc Rc Lw Rw Lw Lc Lc Rc Lw Rw Lw Rc Lc Rc Lw Rw Lc Lc Rc Rc Lc Lc Rc Lw Rw Lw Lc Rc Lw Rw Rc Lw Rw Lc Lc Rc Lw Rw Lw Rc Lc Rc Lw Rw Lw Rc Lc Lc Rc Lw Rw Lc Lc Rc Lw Rw Lc Rc Lw Rw Rc Lc Lc Rc Lw Rw Lw Rc Lc Rc Lw Rw Lc Lc Rc Lw Rw Lc Lc Rw Lc Lc Rw Lc Rc Lw Rw Rc Rw Rw Lw Rc Lw Rw Rw Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Rc Rc Lc Rw Lc Lc Lc Rc Lw Rw Lw Lw Rc Rc Rc Lc Lc Lc Rc Lw Rw Lw Lw Rw Rw Rw Lc Rw Lw Rw Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Rc Lc Rc Lw Lw Rw Lc Lc Rc Lc Lc Rc Lw Rw Lw Rw Lw Lw Rc Lc Lc Rw Lw Lw Rw Lc Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Lw Rc Lc Lc Rc Lw Rw Rw Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Rc Rc Lc Rc Rc Rc Rc Lw Rw Rw Rw Rw Lc Lc Lc Rc Lw Rw Lw Lw Rc Rc Rc Rc Lc Rw Rw Rw Rw Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw
#     """

#     moves = text.split()
#     start = list(range(15))
#     target_string = "thereis_noexit."
#     for i in range(len(moves)):
#         state = start.copy()
#         for j in range(i, len(moves)):
#             do_move(state, moves[j])
#             cur_string = "".join("tohexisentire._"[i] for i in state)
#             if cur_string == target_string:
#                 return " ".join(moves[i : j + 1])


# key = find_solution()
key = "Lw Rc Lw Rw Rw Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Rc Rc Lc Rw Lc Lc Lc Rc Lw Rw Lw Lw Rc Rc Rc Lc Lc Lc Rc Lw Rw Lw Lw Rw Rw Rw Lc Rw Lw Rw Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Rc Lc Rc Lw Lw Rw Lc Lc Rc Lc Lc Rc Lw Rw Lw Rw Lw Lw Rc Lc Lc Rw Lw Lw Rw Lc Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Lw Rc Lc Lc Rc Lw Rw Rw Lc Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw Lw Rc Rc Lc Rc Rc Rc Rc Lw Rw Rw Rw Rw Lc Lc Lc Rc Lw Rw Lw Lw Rc Rc Rc Rc Lc Rw Rw Rw Rw Rc Rc Lc Lc Rc Lw Rw Lw Rw Rw"


@decrypter.decrypter(chapter=24)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, key)
