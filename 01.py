import decrypter


@decrypter.decrypter(chapter=1)
def decrypt(cipher: str) -> str:
    output = []

    for i in range(len(cipher) // 2 + len(cipher) % 2):
        output.append(cipher[i] + cipher[-i - 1])

    return "".join(output)
