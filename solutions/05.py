import decrypter


@decrypter.decrypter(chapter=5)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [7, 6, 8, 3, 2, 1, 9, 5, 4], 9)
