import decrypter


ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'\"-()[]{}|+=%/\\*#$_ \n"
ALPHABET_IDX = {c: i for i, c in enumerate(ALPHABET)}

key = "DIsENCuMBERED"


def decrypt_additive(cipher: str, key: str) -> str:
    result = []
    i = 0
    for c in cipher:
        if c == "\n":
            continue

        c_idx = ALPHABET_IDX[c]
        k_idx = ALPHABET_IDX[key[i % len(key)]]
        p_idx = (c_idx - k_idx) % 89
        result.append(ALPHABET[p_idx])
        i += 1
    return "".join(result)


@decrypter.decrypter(chapter=89, has_chapter_separator=False)
def decrypt(cipher: str) -> str:
    return decrypt_additive(cipher, key)


decrypt.input_file = "87a.txt"
