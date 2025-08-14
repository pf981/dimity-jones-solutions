import itertools

import decrypter


def zig_zag(cipher: str, height: int):
    lines = [[] for _ in range(height)]
    it = itertools.cycle(itertools.chain(range(height), reversed(range(1, height - 1))))

    for ch in cipher:
        lines[next(it)].append(ch)
    return "".join(itertools.chain.from_iterable(lines))


@decrypter.decrypter(chapter=80)
def decrypt(cipher: str) -> str:
    return zig_zag(cipher, 3)
