import decrypter


@decrypter.decrypter(chapter=70)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "hellofludderbee")
