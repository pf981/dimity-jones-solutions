import decrypter


@decrypter.decrypter(chapter=33)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "BGHLX ALOXZ BHMNO")
