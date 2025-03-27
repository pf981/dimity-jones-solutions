import decrypter


@decrypter.decrypter(chapter=23)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "there is no exit")
