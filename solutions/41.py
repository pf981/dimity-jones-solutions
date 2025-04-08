import decrypter


@decrypter.decrypter(chapter=41)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(
        cipher, "The Swift Mahogany-Colored Vixen Leaps The Unjazzed Barker Quite"
    )
