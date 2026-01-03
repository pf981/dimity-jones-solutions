ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'\"-()[]{}|+=%/\\*#$_ \n"
ALPHABET_IDX = {c: i for i, c in enumerate(ALPHABET)}

# ciphertext = open("data/88_pages.txt").read()
ciphertext = open("data/88_tapestry.txt").read()
key = "DIsENCuMBERED"


def decrypt_additive(ciphertext, key):
    result = []
    i = 0
    for c in ciphertext:
        if c == "\n":
            # result.append('\n')
            pass
        else:
            c_idx = ALPHABET_IDX[c]
            k_idx = ALPHABET_IDX[key[i % len(key)]]
            p_idx = (c_idx - k_idx) % 89
            result.append(ALPHABET[p_idx])
            i += 1
    return "".join(result)


print(decrypt_additive(ciphertext, key))


# @decrypter.decrypter(chapter=87)
# def decrypt(cipher: str) -> str:
#     return pour(cipher)

# i = 0
# ct = ciphertext[:36]
# ct += """-w;BwCsz;K)yw!Cr;u1!,AG)'s]|Bq.5rL:"""
# ct = ciphertext[:100]
# for c in ct:
#     if c == "\n":
#         # result.append('\n')
#         pass
#     else:
#         c_idx = ALPHABET_IDX[c]
#         k_idx = ALPHABET_IDX[key[i % len(key)]]
#         p_idx = (c_idx - k_idx) % 89
#         ch = ALPHABET[p_idx]
#         print(i, c, ch)
#         i += 1
