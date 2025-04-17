import collections
import decrypter


@decrypter.decrypter(chapter=45)
def decrypt(cipher: str) -> str:
    counts = collections.Counter()
    l = 0
    key_string = cipher
    best_l = 0
    best_r = len(cipher)
    for r in range(len(cipher)):
        counts[cipher[r]] += 1

        while counts[cipher[l]] > 1:
            counts[cipher[l]] -= 1
            l += 1

        if len(counts) >= 89:
            if r - l + 1 < best_r - best_l + 1:
                best_l, best_r = l, r

    key_string = cipher[best_l : best_r + 1]
    cipher = cipher[:best_l] + cipher[best_r + 1 :]

    return decrypter.substitution_cipher(cipher, key_string)
