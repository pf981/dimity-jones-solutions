import decrypter


def pour(cipher: str):
    highest = 0
    result = {}
    for ch in cipher:
        r = highest - 1
        c = 0

        while True:
            assert (r, c) not in result

            # Floor
            if r == 0:
                break

            # Down
            if (r + 1, c) not in result:
                r += 1
                continue

            # Left
            if (r + 1, c - 1) not in result:
                r += 1
                c -= 1
                continue

            # Right
            if (r + 1, c + 1) not in result:
                r += 1
                c += 1
                continue

            # Settle
            break

        highest = min(highest, r)
        result[(r, c)] = ch

    return "".join(result[pos] for pos in sorted(result))


@decrypter.decrypter(chapter=87)
def decrypt(cipher: str) -> str:
    return pour(cipher)
