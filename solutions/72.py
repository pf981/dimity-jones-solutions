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
    "0G": "grave",
    "0I": "save",
    "02": "right",
    "06": "but",
    "0D": "he",
    "0F": "to",
    "0W": "their",
    "0E": "hard",
    "01": "left",
    "03": "not",
    "00": "a",
    "04": "mine",
    "0Y": "bad",
    "0T": "who",
    "0M": "man",
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
    "0L": "fan",
    "0P": "well",
    "0N": "in",
    "0O": "clean",
    "0R": "rings",
    "0S": "they",
    "0U": "darn",
    "0V": "present",
}


def fix_line(line):
    li = list(line)
    if not li:
        return line
    li[0] = li[0].upper()
    if not li[0].isalpha():
        li[1] = li[1].upper()
    return "".join(li)


key = text
for a, b in m.items():
    key = key.replace(a, b)
key = "\n".join(fix_line(line) for line in key.splitlines())


@decrypter.decrypter(chapter=72)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)
