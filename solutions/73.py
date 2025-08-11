import re

import decrypter

text = """00 01 02 place 03 04 certain 05 06 07 08, 09 07 0A 0B 0C 0D 0E 0F 0G 0H 0I 03 07 0J.

04 0K 0D 04 0L decide 0M 0N 04 0O 0P.

07 0K drives; 0Q 0R 0M toot 07 0S.

0T 0U 06 07 0V 0W.

"0X 0Y 0Z 10?" 07 0L 11.

"12 13 0Y 0X," 14 07 0K.

07 15, 16, stingy 0L 14, "17 18 19 1A." 1B 14, "17 1C 1D 0Z 04 1E 1F."

"1G 1H 1I 1J," 14 07 0K. "1K 03 1L."

0T 1M 07 1N 0H 12 07 1O 13.

"1P 1Q 0B 1R?" 11 07 0L, 1S 0R 1O 04 1T, 1U 1V 04 0W.

"1K 1W 1X."

"1Y 1Z 0B 1V 20," 07 0L 21.

"07 22 0B 0E," 07 0K 23. "17 18 0M 24 1R."

0T 0N 07 25, 26 07 casino.

"27 19 28," 14 07 0L.

0T 29 07 2A. 07 0K, 1S 2B 1D, 2C 2D: 0Q 2C 2E 2F 07 0L, 1S 2G 2H. "1P 04 2I-2J!" 1B 14, 2K 2L 2M.

2N, 06 07 2O, 2P 04 0S band 1M 2Q 2R 2S 0D 29 0A, 07 0K 2T 04 2U, 07 0L 04 2V 12 2W. 0T 2X.

"00 0B 2E 2F 04 0W 12 2Y," 14 07 0K.

07 0L 2Z 30 31 06 32 2W. "17 0Z 0M 33 07 34," 1B 14.

09 1B 35, 1B notices 04 36 37 07 next 38.

"1P 0B 1Y 39?" 11 07 0L. "0G 3A 1E?"

"2K," 14 07 36.

"2I 1L 3B 3A 04 2X. 1P 1H 3A 0Z?"

"2D ... 1J. 04 3C Mary."

(07 0K 02 2H 3D 1A.)

04 0V 2R 1F 35 0M 3E 32 05 flirting 3F 07 0L. "3A 2E 1N 3G, 0L."

"3H 0S," 14 07 0L.

"3I 0G 3J," 14 07 1F. "3K."

"1I 3H, 3L," 14 07 36.

"3M 2Q 3N 39," 14 07 0L.

"3M 2Q 3N 3O," 14 07 1F.

"3P 3A 3E 30 0C 1T 2C 0M 3Q?"

"3A 2E 3R 3S 17 1C 3Q 3A," 14 07 1F.

"1C 1I 15, 3L," 14 07 36.

07 1F -- 2L 1B 3P 0K 0M 27 2T -- 14, "3H 3T."

"1P 0B 1G supposed 0M 15?" 14 07 0L. "3I 0G 3U, 3A 3K."

07 1F, 3V, brandishes 32 3J 0D prepares 0M 24.

07 36, 04 3W, 0F.

07 1F 3X 04 38 06 3R. 07 0L 3Y 3Z 04 2W 06 07 40; 07 0K 3Y 3Z 04 33 06 07 3O.

07 1F 41 42 04 2V.

"1Z 2H!" 14 07 0L.

07 1F 3U 07 2V; 07 0K 0B able 0M 0L 1W 06 1Q. "3M 16!"

07 0L 3T 2M 3F 04 2U 0P; 07 0K, despite 3D 10, 41 42 04 28 2O.

0T 25 07 1F 3F 2Z. 0M 3B 3G, 1B 2Y 2H 12 04 43.

07 43 2B; 2V shatters; everyone 21 3Z 08, 1X 01, 2J 0M 07 0J, 2P 32 34 2G 04 2S.

3C 31 2D 2H 12 04 0I 20.

07 0K 0D 0L 44 into 07 0U, 0D 26, fearing 04 24 12 assault 0D 22, 44 07 0O.

2N, 07 0L, 3V, 23 07 1Q 09 1G 1F 36 2H 12 07 43.

1U 07 0K, 37 40 04 3W, 14, "17 3S 1B didn't 2A."

Meanwhile, far 3G, 3X 29 2J 07 3O 12 07 36."""

replacement_words = [
    "a",
    "air",
    "an",
    "and",
    "antlers",
    "are",
    "arms",
    "asks",
    "at",
    "away",
    "back",
    "bar",
    "barry",
    "battery",
    "be",
    "bear",
    "better",
    "big",
    "bloody",
    "blows",
    "bottom",
    "breaks",
    "bubbles",
    "buck",
    "buffet",
    "but",
    "can't",
    "charge",
    "close",
    "club",
    "country",
    "course",
    "date",
    "dead",
    "deep",
    "die",
    "dives",
    "do",
    "does",
    "don't",
    "dove",
    "down",
    "drink",
    "duck",
    "dummy",
    "even",
    "face",
    "fall",
    "find",
    "flee",
    "follow",
    "for",
    "forgot",
    "get",
    "gives",
    "glass",
    "golf",
    "ground",
    "half",
    "harass",
    "have",
    "he",
    "head",
    "her",
    "him",
    "himself",
    "his",
    "hit",
    "hope",
    "horn",
    "i",
    "in",
    "is",
    "it",
    "it's",
    "just",
    "later",
    "lead",
    "leaves",
    "let",
    "likes",
    "little",
    "lot",
    "me",
    "mean",
    "my",
    "name",
    "nice",
    "nine",
    "not",
    "observes",
    "odd",
    "of",
    "okay",
    "old",
    "on",
    "one",
    "orders",
    "out",
    "pacifist",
    "park",
    "picks",
    "play",
    "punch",
    "remembers",
    "reservations",
    "returns",
    "rock",
    "roll",
    "says",
    "she",
    "single",
    "snorting",
    "some",
    "sorry",
    "story",
    "stout",
    "strikes",
    "sweet",
    "table",
    "takes",
    "tears",
    "than",
    "that",
    "that's",
    "the",
    "then",
    "these",
    "they",
    "this",
    "time",
    "to",
    "up",
    "visit",
    "wallet",
    "watch",
    "we",
    "well",
    "what",
    "when",
    "where",
    "who",
    "will",
    "window",
    "wings",
    "with",
    "wound",
    "you",
    "your",
]

m = {
    "3G": "away",
    "07": "a",  # "a" or "the"
    "0K": "club",
    "04": "the",
    "14": "says",
}
import collections

all_words = collections.Counter()
for line in text.splitlines():
    line = "".join(c for c in line if c.isalnum() or c == " ")
    words = line.split()
    all_words += collections.Counter(words)


def fix_line(line):
    li = list(line)
    if not li:
        return line

    # Line start has capital
    li[0] = li[0].upper()

    # If line starts with punctuation, then second letter is capital
    if not li[0].isalpha() and len(li) > 1:
        li[1] = li[1].upper()

    # .! followed by space (optionally with quote) is capital. Note that ?" and ?' do not result in capitals. Nor does exclamation  marks
    line = "".join(li)
    line = re.sub(
        r'[^.]\. *["\']? *[a-z]',
        lambda s: s.group(0)[:-1] + s.group(0)[-1].upper(),
        line,
    )

    # '''says, "nice arms."''' should be '''says, "Nice arms."'''
    line = re.sub(
        r'"[a-z]',
        lambda s: s.group(0)[:-1] + s.group(0)[-1].upper(),
        line,
    )

    # Bloody Mary
    line = line.replace("bloody Mary", "Bloody Mary").replace("barry", "Barry")

    return line


def get_plaintext(text: str, m: dict[str, str]) -> str:
    plaintext = text
    for a, b in m.items():
        if b == "i":
            b = b.upper()
        plaintext = plaintext.replace(a, b)
    plaintext = "\n".join(fix_line(line) for line in plaintext.splitlines())
    return plaintext


# %clear
# print(key)


@decrypter.decrypter(chapter=73)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)


import itertools

dec = decrypter.decrypter(chapter=73)(lambda x: x)
ciphertext = dec.decrypt_one_chapter()[:5000]


def to_base36(num: int) -> str:
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return "00"
    result = ""
    while num:
        num, rem = divmod(num, 36)
        result = chars[rem] + result
    return result.zfill(2)


if "mapping" not in globals():
    mapping = {
        "00": "this",
        "01": "story",
        "02": "takes",
        "03": "on",
        "04": "a",
        "05": "date",
        "06": "in",
        "07": "the",
        "08": "fall",
        "09": "when",
        "0A": "air",
        "0B": "is",
        "0C": "sweet",
        "0D": "and",
        "0E": "dead",
        "0F": "leaves",
        "0G": "are",
        "0H": "nine",
        "0I": "deep",
        "0J": "ground",
        "0K": "bear",
        "0L": "duck",
        "0M": "to",
        "0N": "visit",
        "0O": "country",
        "0P": "club",
        "0Q": "she",
        "0R": "likes",
        "0S": "horn",
        "0T": "they",
        "0U": "park",
        "0V": "big",
        "0W": "lot",
        "0X": "do",
        "0Y": "we",
        "0Z": "have",
        "10": "reservations",
        "11": "asks",
        "12": "of",
        "13": "course",
        "14": "says",
        "15": "mean",
        "16": "close",
        "17": "i",
        "18": "forgot",
        "19": "my",
        "1A": "wallet",
        "1B": "he",
        "1C": "don't",
        "1D": "even",
        "1E": "single",
        "1F": "buck",
        "1G": "that",
        "1H": "will",
        "1I": "be",
        "1J": "okay",
        "1K": "it's",
        "1L": "me",
        "1M": "play",
        "1N": "back",
        "1O": "golf",
        "1P": "what",
        "1Q": "time",
        "1R": "it",
        "1S": "who",
        "1T": "little",
        "1U": "but",
        "1V": "not",
        "1W": "just",
        "1X": "one",
        "1Y": "your",
        "1Z": "watch",
        "20": "wound",
        "21": "observes",
        "22": "battery",
        "23": "remembers",
        "24": "charge",
        "25": "buffet",
        "26": "then",
        "27": "follow",
        "28": "lead",
        "29": "roll",
        "2A": "die",
        "2B": "breaks",
        "2C": "does",
        "2D": "well",
        "2E": "better",
        "2F": "than",
        "2G": "strikes",
        "2H": "out",
        "2I": "let",
        "2J": "down",
        "2K": "sorry",
        "2L": "for",
        "2M": "himself",
        "2N": "later",
        "2O": "bar",
        "2P": "where",
        "2Q": "an",
        "2R": "old",
        "2S": "rock",
        "2T": "orders",
        "2U": "stout",
        "2V": "glass",
        "2W": "punch",
        "2X": "drink",
        "2Y": "dives",
        "2Z": "blows",
        "30": "some",
        "31": "bubbles",
        "32": "his",
        "33": "hit",
        "34": "head",
        "35": "returns",
        "36": "dove",
        "37": "at",
        "38": "table",
        "39": "name",
        "3A": "you",
        "3B": "get",
        "3C": "bloody",
        "3D": "her",
        "3E": "find",
        "3F": "with",
        "3G": "away",
        "3H": "nice",
        "3I": "these",
        "3J": "antlers",
        "3K": "dummy",
        "3L": "barry",
        "3M": "that's",
        "3N": "odd",
        "3O": "face",
        "3P": "can't",
        "3Q": "harass",
        "3R": "half",
        "3S": "hope",
        "3T": "arms",
        "3U": "wings",
        "3V": "snorting",
        "3W": "pacifist",
        "3X": "tears",
        "3Y": "gives",
        "3Z": "him",
        "40": "bottom",
        "41": "picks",
        "42": "up",
        "43": "window",
        "44": "flee",
    }
# 130 116 121 96 1 33 72 126 48 140 2 73 119 4 34 79 6 89 35 58 16 44 132 134 31 30 111 81 70 129 101 18 83 38? 137 61 106 8 93 32 110 85 29 71 53 86 135 62 40 46 112 24
# 124 143 15 [94 was somewhere here] 75 84 103 11 57 139 131 74 142 82 26 90 76 97 149 136 147 91 14 105 28 25 127 51 78 109 36 22 39 138 17 123 118 99 80 42
# 115 52 66 77 12 141 3 95 108 98 117 56 104 43 37 20 114 23 67 68 63
# ...
# 7 but need to fix caps
# for placeholder_int in range(int("44", 36) + 1):
placeholder_int = 0
while placeholder_int <= int("44", 36):
    placeholder = to_base36(placeholder_int)

    if placeholder in mapping:
        placeholder_int += 1
        continue

    start = text.index(placeholder)

    for next_placeholder_int in range(placeholder_int + 1, int("44", 36) + 1):
        next_placeholder = to_base36(next_placeholder_int + 1)
        if next_placeholder not in mapping:
            end = text.index(next_placeholder)
            break
    else:
        end = len(text)

    # Truncate excessive right context so that when we print 50 chars it includes the part of interest.
    # Try to chop at a space so that placeholders don't get split in two
    if start + 25 < end:
        end = start + 25
        while end > start + 8 and text[end - 1] != " ":
            end -= 1
    # end = min(end, start + 25)

    # before = get_plaintext(text[0:start], mapping)
    # after = text[start + 2 : end]

    print("", end="", flush=True)
    # %clear

    print(f'--- Choose replacement for "{placeholder}"---')
    plaintexts = {}
    keys = {}
    for i, word in enumerate(replacement_words, 1):
        if word in mapping.values():
            continue

        new_mapping = mapping.copy()
        new_mapping[placeholder] = word
        key = get_plaintext(text[:end], new_mapping)
        plaintext = decrypter.vigenere_cipher(ciphertext[: len(key)], key)

        plaintexts[i] = plaintext
        keys[i] = key

        print(f"\n\n{i} - {word}:")
        print(f"--- Key ---")
        print(f"{key}")
        print(f"--- Plaintext ---")
        print(f"{plaintext}")

    print("\n---------")
    print("---------")
    print("---------")
    max_key_len = max(len(key) for key in keys.values())
    for i, key in keys.items():
        key = (
            key.replace("\n", "@")
            .replace("\\", "~")
            .replace("'", "`")
            .ljust(max_key_len)
        )[-50:]
        print(f"{str(i).rjust(3)}: {key!r}")

    print("\n---------")
    print("---------")
    print("---------")
    max_plaintext_len = max(len(plaintext) for plaintext in plaintexts.values())
    for i, plaintext in plaintexts.items():
        plaintext = (
            plaintext.replace("\n", "@")
            .replace("\\", "~")
            .replace("'", "`")
            .ljust(max_plaintext_len)
        )[-50:]
        print(f"{str(i).rjust(3)}: {plaintext!r}")
    print()

    do_quit = False
    do_undo = False
    while True:
        choice = input('Choose word number (or "q" to quit, "u" to undo): ')
        if choice == "q":
            do_quit = True
            break
        if choice == "u":
            do_undo = True
            break
        if choice in [str(i) for i in range(1, len(replacement_words) + 1)]:
            break
        print("Invalid choice")

    if do_quit:
        break
    if do_undo:
        mapping.popitem()
        placeholder_int -= 1
        continue

    chosen_word = replacement_words[int(choice) - 1]
    mapping[placeholder] = chosen_word

    placeholder_int += 1


# f'{0:}'

# %clear
# print(get_plaintext(text, mapping))

# latest_key = get_plaintext(text, mapping)
# plain = '''The puzzlers began by finding the most common blanks: "07", appearing sixty-eight times, must be "the", and "04", appearing twenty-eight times, was likely "a". Dimity and Leland, stretching on tiptoe to reach the highest, filled the recesses with panels. Already this revea[ed "toot the [something]" on line three; "horn" for "0S" therefore seemed probable, especially since it would also give "a hoXu(Xand" far'''

# %clear
# print(decrypter.vigenere_cipher(ciphertext, latest_key)[:5000])

# # %clear
# for a, b in zip(plain, latest_key):
#     print(f'{a!r} {b!r}')
