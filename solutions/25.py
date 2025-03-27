import decrypter


@decrypter.decrypter(chapter=25)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(
        cipher, "All who enter a citadel such as this'll be here always."
    )
