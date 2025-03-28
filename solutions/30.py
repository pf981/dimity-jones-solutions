import decrypter
# import random

# TOO + TOO + TOO + TOO = GOOD
# 400T + 44O = 1000G + 110O + D

# sequence = list(range(10))
# while True:
#     random.shuffle(sequence)
#     T, O, G, D, *_ = sequence
#     if 400 * T + 44 * O == 1000 * G + 110 * O + D:
#         break
# # (1, 6, 0, 4)


@decrypter.decrypter(chapter=30)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "166 + 166 + 166 + 166 = 0664")
