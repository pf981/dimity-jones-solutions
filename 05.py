import decrypter
import itertools


def chunk_shuffle(cipher: str, chunk_size: int | None, sequence: list[int]):
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


@decrypter.decrypter(chapter=5)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(cipher, 9, [7, 6, 8, 3, 2, 1, 9, 5, 4])
