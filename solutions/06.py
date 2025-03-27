import decrypter


@decrypter.decrypter(chapter=6)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [2, 9, 1, 5, 8, 4, 6])
