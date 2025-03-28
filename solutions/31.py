import decrypter
# import random

# # NON + NON + NON + NON + NON = IRON
# # 505N + 50O = 1000I + 100R + 10O + N

# sequence = list(range(10))
# while True:
#     random.shuffle(sequence)
#     N, O, I, R, *_ = sequence
#     if 505 * N + 50 * O == 1000 * I + 100 * R + 10 * O + N:
#         print(
#             f"{N}{O}{N} + {N}{O}{N} + {N}{O}{N} + {N}{O}{N} + {N}{O}{N} = {I}{R}{O}{N}"
#         )
#         break


@decrypter.decrypter(chapter=31)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "575 + 575 + 575 + 575 + 575 = 2875")
