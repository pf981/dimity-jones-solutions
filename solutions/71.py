import decrypter

text = """00 01 02 03 04 05 06 07;
00 01 02 07 04 05 06 03.
08 09 glided through 08 sky;
08 latter 0A 02 0B hat.

0C 0D, 02 0B, 05 06 0E.
One time he 0A his welcome out:
They 0E him 0E 0C couch 06 straw,
And "09 0D!" were heard 06 shout."""

m = {
    "08": "the",
    "03": "bat",
    "0A": "wore",
    "0E": "saw",
    "07": "fly",
    "0B": "cricket",
    "02": "a",
    "0C": "their",
    "06": "to",
    "09": "former",
    "0D": "friend",
    "05": "loved",
    "00": "there",
    "01": "was",
    "04": "who",
}

result = text
for a, b in m.items():
    result = result.replace(a, b)
# print(result)


key = """There was a bat who loved to fly;
There was a fly who loved to bat.
The former glided through the sky;
The latter wore a cricket hat.

Their friend, a cricket, loved to saw.
One time he wore his welcome out:
They saw him saw their couch to straw,
And "Former friend!" were heard to shout."""


@decrypter.decrypter(chapter=71)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)
