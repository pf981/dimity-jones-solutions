import decrypter

# IN + AN = INN
# 10 + 90 = 100


@decrypter.decrypter(chapter=29)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "10 + 90 = 100")
