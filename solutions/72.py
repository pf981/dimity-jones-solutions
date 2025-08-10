import decrypter

text = """00 01 shoe does on 02 foot 03 belong;
I 01 04 05, which wasn't 02, 06 wrong.

She, truant 07 08 law 09, sees 08 0A.
0B 0A 06 09 director 0C 0B 05.

0D finds it 0E 0F dig his mother's 0G;
He'd, if 0D could, 0H 0G, 0E woman 0I.

0J 0K of summer 03 be called 00 0L.
0J sit by 0L, eat straight 07 0K. Oh, 0M.

0N 0O, 0P-lighted, 0Q-shaped 0R 0S 0Q;
Till round-end 0R, 0S 0O each other's clocks.

Our aunts, 0T 0U, 0V 0W 0X gift.
"00 0X 0U 0Y 0V," think we, miffed.

0I those 0Y few 0T set them, none should have 0F take 0W turn
0F 0M 08 0P and douse 08 0C 0H 0N 08 04 still burn."""

m = {
    "0Q": "box",
    # "0G": "mine",
    # "0G": "well",
    "0G": "grave",
    "0I": "save",
    "02": "right",
    "06": "but",
    "0D": "he",
    "0F": "to",
    "0W": "their",
    "0E": "hard",
    # "0P": "well",
    "01": "left",
    "03": "not",
    "00": "the",
    # "04": "her",  # ?
    "04": "fires",  # ?
    # "05": "there",  # ?
    "0Y": "bad",  # ?
    "0T": "who",
    "0M": "darn",
    "0X": "pretty",
    "07": "from",
    "08": "the",
    # "09": "man",
    "0A": "man",
    "05": "fan",
}

result = text
for a, b in m.items():
    result = result.replace(a, b)
print(result)

[word for word in words if word not in m.values()]

words = [
    "a",
    "bad",
    "box",
    "but",
    "can",
    "clean",
    "darn",
    "fair",
    "fan",
    "fires",
    "firm",
    "from",
    "grave",
    "hard",
    "he",
    "her",
    "in",
    "left",
    "man",
    "mine",
    "not",
    "present",
    "pretty",
    "right",
    "rings",
    "save",
    "that",
    "the",
    "their",
    "there",
    "they",
    "to",
    "well",
    "who",
    "you",
]


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
