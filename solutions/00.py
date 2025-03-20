import decrypter


@decrypter.decrypter(chapter=0)
def decrypt(cipher: str) -> str:
    return cipher
