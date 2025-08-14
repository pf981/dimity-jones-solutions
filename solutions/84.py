import decrypter


def gen_layer_indexes():
    width = 1
    while True:
        for i in range(0, width, 2):
            yield i
        for i in range(1, width, 2):
            yield i

        width *= 2


def tree(cipher: str):
    result = []
    it = gen_layer_indexes()
    width = 1
    for ch in cipher:
        i = next(it)
        if i == 0:
            result.append([""] * width)
            width *= 2

        result[-1][i] = ch

    return "".join("".join(layer) for layer in reversed(result))


@decrypter.decrypter(chapter=84)
def decrypt(cipher: str) -> str:
    return tree(cipher)
