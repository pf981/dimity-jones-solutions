import itertools

import decrypter


def gen_layer_indexes():
    for n in itertools.count(1):
        for i in range(n):
            yield i


def staircase(cipher: str):
    layers = []
    it = gen_layer_indexes()
    for ch in cipher:
        i = next(it)
        if i == len(layers):
            layers.append([])
        layers[i].append(ch)

    return "".join("".join(reversed(layer)) for layer in reversed(layers))


@decrypter.decrypter(chapter=82)
def decrypt(cipher: str) -> str:
    return staircase(cipher)
