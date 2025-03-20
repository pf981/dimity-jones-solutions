import decrypter


@decrypter.decrypter(chapter=0)
def decrypt(cipher: str) -> str:
    return cipher


decrypt.decrypt_one_chapter()[:100]
