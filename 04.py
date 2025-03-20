import decrypter
import itertools


def chunk_shuffle(cipher: str, sequence: list[int]):
    result = []
    for buffer in itertools.batched(cipher, 8):
        if len(buffer) < 8:
            result.extend(buffer)
            break
        for i in sequence:
            result.append(buffer[i - 1])
    return "".join(result)


@decrypter.decrypter(chapter=4)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(cipher, [3, 2, 1, 7, 6, 5])
