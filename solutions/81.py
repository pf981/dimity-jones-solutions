import itertools

import decrypter


def switchback(cipher: str, height: int):
    result = []
    for i, column in enumerate(itertools.batched(cipher, height)):
        n = len(column)

        if i % 2 == 0:
            column = column[::-1]
            column = ("",) * (height - n) + column
        else:
            column = column + ("",) * (height - n)
        result.append(column)

    return "".join(itertools.chain.from_iterable(zip(*result, strict=True)))


@decrypter.decrypter(chapter=81)
def decrypt(cipher: str) -> str:
    return switchback(cipher, 15)
