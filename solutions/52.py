import decrypter


@decrypter.decrypter(chapter=52)
def decrypt(cipher: str) -> str:
    letters = "ABCDEHIKMOTUVWXY"
    table = [
        # A
        # BCDEHIKMOTUVWXY
        "012345678ABCDEFG",  # A
        "HIKMNQSUVWXYabcd",  # B
        "efghijklmnopqrtu",  # C
        """vwxyz.,?!:;'"-()""",  # D
        "[]{}|+=%/\\*#$\n",  # E
        "Z",  # H
        "J",  # I
        "L",  # K
        "O",  # M
        "T",  # O
        "R",  # T
        " ",  # U
        "s",  # V
        "9",  # W
        "P",  # X
        "_",  # Y
    ]

    result = []
    i = 0
    while i < len(cipher):
        row = letters.index(cipher[i])

        if len(table[row]) == 1:
            result.append(table[row])
        else:
            i += 1
            col = letters.index(cipher[i])
            result.append(table[row][col])
        i += 1

    return "".join(result)
