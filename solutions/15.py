import decrypter
import itertools


def chunk_shuffle(cipher: str, sequence: list[int], chunk_size: int | None = None):
    if chunk_size is None:
        chunk_size = max(sequence)

    result = []
    for buffer in itertools.batched(cipher, chunk_size):
        if len(buffer) < chunk_size:
            result.extend(buffer)
            break
        for i in sequence:
            result.append(buffer[i - 1])

    return "".join(result)


def get_alphabetical_transposition_key(s: str):
    chars = [c.upper() for c in s if c.isalpha()]
    ranks = sorted(enumerate(chars), key=lambda pair: pair[1])

    key = [0] * len(chars)
    for i, (j, _) in enumerate(ranks, 1):
        key[j] = i

    return key

# import random

# cogwheels = ["ASWHIRST", "WILL_LIV", "TAKE_TOO", "SHE_EASI", "LY_ARTHE"]
# WHIR-L_LI-KE_T-HE_E-ARTH

# for _ in range(5000):
#     for s in cogwheels:
#         i = random.randint(1, 8)
#         print((s + s)[i:i+4], end="")
#     print()


@decrypter.decrypter(chapter=15)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(
        cipher,
        get_alphabetical_transposition_key("WHIRL LIKE THE EARTH")
    )
