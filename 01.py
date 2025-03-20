import decrypter


@decrypter.decrypter(chapter=1)
def decrypt(cipher: str) -> str:
    output = []

    for i in range(len(cipher) // 2):
        output.append(cipher[i] + cipher[-i - 1])
    if len(cipher) % 2:
        output.append(cipher[len(cipher) // 2])

    return "".join(output)
