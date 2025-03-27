import decrypter


@decrypter.decrypter(chapter=4)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [3, 2, 1, 7, 6, 5], 8)
