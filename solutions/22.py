import decrypter


@decrypter.decrypter(chapter=22)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "there can be no escape")
