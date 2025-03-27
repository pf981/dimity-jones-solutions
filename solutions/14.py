import decrypter


@decrypter.decrypter(chapter=14)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "BEHOLD MY GENIUS")
