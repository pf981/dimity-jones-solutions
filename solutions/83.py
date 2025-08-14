import decrypter


def spiral(cipher: str, period: int):
    result = []
    for i in range(period):
        for j in range(i, len(cipher), period):
            result.append(cipher[j])
    return "".join(result)


@decrypter.decrypter(chapter=83)
def decrypt(cipher: str) -> str:
    return spiral(cipher, 10)
