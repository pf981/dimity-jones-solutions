import decrypter


@decrypter.decrypter(chapter=20)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "EROSION")
