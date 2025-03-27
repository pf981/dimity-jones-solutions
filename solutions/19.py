import decrypter


@decrypter.decrypter(chapter=19)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(
        cipher, "there is no one who knows the extent of my grief"
    )
