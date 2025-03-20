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


line = "These make up words like feathers make birds."
chars = [c.upper() for c in line if c.isalpha()]
ranks = sorted(enumerate(chars), key=lambda pair: pair[1])
score = [0] * len(chars)
for i, (j, _) in enumerate(ranks, 1):
    score[j] = i
score


@decrypter.decrypter(chapter=10)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(
        cipher,
        score,
        # [
        #     34,
        #     15,
        #     7,
        #     30,
        #     8,
        #     23,
        #     1,
        #     19,
        #     9,
        #     36,
        #     26,
        #     37,
        #     25,
        #     27,
        #     5,
        #     31,
        #     22,
        #     17,
        #     20,
        #     10,
        #     14,
        #     11,
        #     2,
        #     35,
        #     16,
        #     12,
        #     28,
        #     32,
        #     24,
        #     3,
        #     21,
        #     13,
        #     4,
        #     18,
        #     29,
        #     6,
        #     33,
        # ],
    )
