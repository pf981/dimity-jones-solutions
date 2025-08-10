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
    "00": "a",
    # "04": "her",  # ?
    "04": "mine",  # ?
    # "05": "there",  # ?
    "0Y": "bad",  # ?
    "0T": "who",
    "0M": "man",  #
    "0X": "pretty",
    "07": "from",
    "08": "the",
    "09": "firm",
    "0A": "fair",
    "05": "there",
    "0B": "her",
    "0C": "fires",
    "0H": "that",
    "0J": "you",
    "0K": "can",
    "0L": "fan",  # ?
}

result = text
for a, b in m.items():
    result = result.replace(a, b)  # .replace("called a man.", "called a Man.")
print(result)

[word for word in words if word not in m.values()]

[word for word in words if len(word) == 4]


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


key = result


# key = 'A left shoe does on right foot not belong;\nI left fires fan, which wasn\'t right, but wrong.\n\nShe, truant from the law firm, sees the fair.\nthe fair but firm director 0C the fan.\n\nhe finds it hard to dig his mother\'s grave;\nHe\'d, if he could, 0H grave, hard woman save.\n\n0J 0K of summer not be called a 0L.\n0J sit by 0L, eat straight from 0K. Oh, darn.\n\n0N 0O, 0P-lighted, box-shaped 0R 0S box;\nTill round-end 0R, 0S 0O each other\'s clocks.\n\nOur aunts, who 0U, 0V their pretty gift.\n"a pretty 0U bad 0V," think we, miffed.\n\nsave those bad few who set them, none should have to take their turn\nto darn the 0P and douse the 0C 0H 0N the fires still burn.'
def fix_line(line):
    l = list(line)
    if not l:
        return line
    l[0] = l[0].upper()
    if not l[0].isalpha():
        l[1] = l[1].upper()
    return "".join(l)


key = "\n".join(fix_line(line) for line in result.splitlines())


@decrypter.decrypter(chapter=72)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)


import itertools

dec = decrypter.decrypter(chapter=72)(lambda x: x)
ciphertext = dec.decrypt_one_chapter()[:5000]

# key = "A left shoe does on right foot not belong;\nI left mine there, which wasn't right, but wrong.\n\nShe, truant from the law firm, sees the fair.\n0B man but 09 director 0C 0B fan.\n\nhe finds it hard to dig his mother's grave;\nHe'd, if he could, 0H grave, hard woman save.\n\n0J 0K of summer not be called a 0L.\n0J sit by 0L, eat straight from 0K. Oh, darn.\n\n0N 0O, 0P-lighted, box-shaped 0R 0S box;\nTill round-end 0R, 0S 0O each other's clocks.\n\nOur aunts, who 0U, 0V their pretty gift.\n\"a pretty 0U bad 0V,\" think we, miffed.\n\nsave those bad few who set them, none should have to take their turn\nto darn the 0P and douse the 0C 0H 0N the fires still burn."
plain = decrypter.vigenere_cipher(ciphertext, key)

# print(plain)
print(plain[:600])

for a, b in zip(plain[:370], itertools.cycle(key)):
    print(f"{a!r}, {b!r}")

alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
have, want, k = r"uld"
alphabet[
    (alphabet.index(have) - (alphabet.index(want) - alphabet.index(k))) % len(alphabet)
]
