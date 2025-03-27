import decrypter


@decrypter.decrypter(chapter=10)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "These make up words like feathers make birds.")
