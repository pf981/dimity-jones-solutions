import decrypter


@decrypter.decrypter(chapter=39)
def decrypt(cipher: str) -> str:
    pairs = ["oi", "uo", "ea", "ie", "au"]
    m = {}
    for a, b in pairs:
        m[a] = b
        m[a.upper()] = b.upper()
    return "".join(m.get(c, c) for c in cipher)
