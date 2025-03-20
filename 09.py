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


lines = [
    "Apples, bitten, cause delight.",
    "Beaten dogs prove shabby sights.",
    "Ballet dancers may wear tights.",
    "Friends and family never fight.",
    "For persons who're reshelving tomes, this order helps them find them homes.",
]

scores = []
for line in lines:
    words = "".join(c.upper() for c in line if c.isalpha() or c == " ").split()
    ranks = sorted(enumerate(words), key=lambda pair: pair[1])
    score = [0] * len(words)
    for i, (j, _) in enumerate(ranks, 1):
        score[j] = i
    scores.append(score)


@decrypter.decrypter(chapter=9)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(cipher, scores[3] + scores[4][1:6])
