import decrypter
import re


@decrypter.decrypter(chapter=3)
def decrypt(cipher: str) -> str:
    return "".join(w[::-1] for w in re.split(r"( )", cipher))
