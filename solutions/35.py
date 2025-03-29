import decrypter


@decrypter.decrypter(chapter=35)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "VTI QAVD PMVDR")
