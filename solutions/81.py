import itertools

import decrypter


def switchback(cipher: str, height: int):
    result = []
    for i, column in enumerate(itertools.batched(cipher, height)):
        n = len(column)
        column += ("",) * (height - n)

        if i % 2 == 0:
            column = reversed(column)

        result.append(column)

    return "".join(itertools.chain.from_iterable(zip(*result, strict=True)))


@decrypter.decrypter(chapter=81)
def decrypt(cipher: str) -> str:
    return switchback(cipher, 15)
