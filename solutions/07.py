import decrypter


@decrypter.decrypter(chapter=7)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [6, 4, 2, 1, 7])
