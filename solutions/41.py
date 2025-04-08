import decrypter
import string


def substitution_cipher_alpha(cipher: str, key_string: str):
    keys = list({c.lower(): None for c in key_string if c.isalpha()})
    keys += [c for c in string.ascii_lowercase if c not in keys]
    m = {}
    for a, b in zip(keys, string.ascii_lowercase):
        m[a] = b
        m[a.upper()] = b.upper()

    return "".join(m.get(c, c) for c in cipher)


@decrypter.decrypter(chapter=41)
def decrypt(cipher: str) -> str:
    return substitution_cipher_alpha(
        cipher,
        "The Swift Mahogany-Colored Vixen Leaps The Unjazzed Barker Quite",
    )
