import decrypter


@decrypter.decrypter(chapter=0, has_chapter_separator=False)
def decrypt(cipher: str) -> str:
    return cipher
