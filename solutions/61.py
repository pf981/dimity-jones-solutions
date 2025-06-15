import decrypter


@decrypter.decrypter(chapter=61)
def decrypt(cipher: str) -> str:
    # return decrypter.vigenere_cipher(cipher, "00:00") # Not bad?
    # return decrypter.vigenere_cipher(cipher, "01:25")  # Not bad?
    # return decrypter.vigenere_cipher(cipher, "03:01")  # QUITE GOOD!
    # return decrypter.vigenere_cipher(cipher, "03:00")  # QUITE GOOD!
    # return decrypter.vigenere_cipher(cipher, "03:09")  # QUITE GOOD!
    return decrypter.vigenere_cipher(cipher, "03:04")  # Correct


# import itertools

# dec = decrypter.decrypter(chapter=61)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:500]

# key = "03:09"
# plain = decrypter.vigenere_cipher(ciphertext, key)

# print(plain)

# for a, b in zip(plain[:150], itertools.cycle(key)):
#     print(a, b)

# alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
# have, want, key = r"+*9"
# alphabet[
#     (alphabet.index(have) - (alphabet.index(want) - alphabet.index(key)))
#     % len(alphabet)
# ]

# text = """Though I prefer to sleep in, I get woken by the neighbor's stupid rooster no later than this (in winter; in June it's even worse): 06:15

# When I have my lunch (liver w/ onions or a burger w/ the fixings are two faves): 12:30

# Last night I started cooking supper at this time exactly: 18:15

# I will climb into bed with a dull book (to zonk out to): 23:55

# In the wee hours I wake; I peer at the clock, but haven't the faintest hypothesis as to what the figures signify. When is this? Where is this? What is happening? Who is this, even, asking or trying to answer these questions? I (if it is not an untruth to utter that pronoun) appear to be a hazy hunk of nothingness wafting without purpose in an inky opaqueness so infinite that this thing I happen to be is too weak, too tiny, to probe or assess it. Terror saturates this nonentity's arteries. Gasping for air, I shriek:"""

# # He supposed that one of the clocks lining the walls must constitute the key that would unlock the puzzle. But, aside from the seemingly random heterogeneity of the times they displayed, they all appeared to be identical: hundreds of plain round analog clocks whose twenty-four hours were marked with Roman numerals (and a "0" for midnight).
