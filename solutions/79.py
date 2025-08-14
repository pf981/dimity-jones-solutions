import itertools

import decrypter


def ascending_ladder(cipher: str, rung_size: int):
    result = reversed(list(itertools.batched(cipher, rung_size)))
    return "".join(itertools.chain.from_iterable(result))


@decrypter.decrypter(chapter=79)
def decrypt(cipher: str) -> str:
    return ascending_ladder(cipher, 5)
