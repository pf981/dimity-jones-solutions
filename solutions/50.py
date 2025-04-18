import decrypter


@decrypter.decrypter(chapter=50)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(
        cipher,
        "The quick brown fox jumps over the lazy hound.",
    )
