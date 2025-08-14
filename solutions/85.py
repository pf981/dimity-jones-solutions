import math

import decrypter


def cc_centrifugal_spiral(cipher: str):
    n = math.ceil(math.sqrt(len(cipher)))
    result = [[""] * n for _ in range(n)]
    r = c = n // 2
    heading = "N"
    turn = {"W": "S", "S": "E", "E": "N", "N": "W"}
    for ch in cipher:
        result[r][c] = ch

        heading2 = turn[heading]
        r2, c2 = r, c
        r2 += (heading2 == "S") - (heading2 == "N")
        c2 += (heading2 == "E") - (heading2 == "W")
        if not result[r2][c2]:
            r, c = r2, c2
            heading = heading2
        else:
            r += (heading == "S") - (heading == "N")
            c += (heading == "E") - (heading == "W")

    return "".join("".join(layer) for layer in result)


@decrypter.decrypter(chapter=85)
def decrypt(cipher: str) -> str:
    return cc_centrifugal_spiral(cipher)
