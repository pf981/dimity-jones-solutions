import decrypter

text = """
BF|EGFEDE,|BAEG|B|GEED|BF,|EAFE,
FABE|EAAGEECEGF,|EBCD|EGDFBEE:
BF|B'AE,|FAD|FAAEE|BBFA|DEAEAG,|FADE
A|AEDEE|FA|BAGDED|AF,|EGDBDBEED|...?
"""

text.split("|")

m = {}
for ch in "ABCDEFG":
    replacement = []
    i = ord(ch)
    while i <= ord("Z"):
        replacement.append(chr(i))
        i += 7
    replacement = "/".join(replacement)
    m[ch] = f"({replacement})"

text2 = text.lower()
for ch, replacement in m.items():
    text2 = text2.replace(ch.lower(), replacement)
print("\n".join(text2.split("|")))

# IF (B/I/P/W)(F/M/T)
#    (E/L/S/Z)(G/N/U)(F/M/T)(E/L/S/Z)(D/K/R/Y)(E/L/S/Z),
#  ..EN  (B/I/P/W)(A/H/O/V)(E/L/S/Z)(G/N/U)
# I  (B/I/P/W)
# USED   (G/N/U)(E/L/S/Z)(E/L/S/Z)(D/K/R/Y)
# IT / IF   (B/I/P/W)(F/M/T),
#     (E/L/S/Z)(A/H/O/V)(F/M/T)(E/L/S/Z),
# THIS  (F/M/T)(A/H/O/V)(B/I/P/W)(E/L/S/Z)
# SHAG.... (E/L/S/Z)(A/H/O/V)(A/H/O/V)(G/N/U)(E/L/S/Z)(E/L/S/Z)(C/J/Q/X)(E/L/S/Z)(G/N/U)(F/M/T),
# SICK (E/L/S/Z)(B/I/P/W)(C/J/Q/X)(D/K/R/Y)
# (E/L/S/Z)(G/N/U)(D/K/R/Y)(F/M/T)(B/I/P/W)(E/L/S/Z)(E/L/S/Z):
# IF/IT     (B/I/P/W)(F/M/T)
# I'VE  (B/I/P/W)'(A/H/O/V)(E/L/S/Z),
# MAY/FAD/FAR/FOR  (F/M/T)(A/H/O/V)(D/K/R/Y)
# THESE  (F/M/T)(A/H/O/V)(A/H/O/V)(E/L/S/Z)(E/L/S/Z)
# WITH (B/I/P/W)(B/I/P/W)(F/M/T)(A/H/O/V)
# REASON    (D/K/R/Y)(E/L/S/Z)(A/H/O/V)(E/L/S/Z)(A/H/O/V)(G/N/U),
# MADE  (F/M/T)(A/H/O/V)(D/K/R/Y)(E/L/S/Z)
# A   (A/H/O/V)
# HERES   (A/H/O/V)(E/L/S/Z)(D/K/R/Y)(E/L/S/Z)(E/L/S/Z)
# TO  (F/M/T)(A/H/O/V)
# PONDER    (B/I/P/W)(A/H/O/V)(G/N/U)(D/K/R/Y)(E/L/S/Z)(D/K/R/Y)
# OF   (A/H/O/V)(F/M/T),
#      (E/L/S/Z)(G/N/U)(D/K/R/Y)(B/I/P/W)(D/K/R/Y)(B/I/P/W)(E/L/S/Z)(E/L/S/Z)(D/K/R/Y)
# ...?


from decrypter import vigenere_breaker

reference_text = ""
for chapter in range(62):
    with open(f"data/{chapter:02}.chp", "r") as f:
        reference_text += f.read()

c = decrypter.decrypter(chapter=63)(lambda x: x)
ciphertext = c.decrypt_one_chapter()[:500]

result = vigenere_breaker.try_multiple_key_lengths(
    ciphertext,
    reference_text,
    decrypter_func=decrypter.vigenere_cipher,
    min_length=1,
    max_length=40,
    key_chars=vigenere_breaker.ALPHABET,
    verbose=True,
)

decrypted, key = vigenere_breaker.break_vigenere_cipher(
    ciphertext,
    reference_text,
    decrypter.vigenere_cipher,
    max_key_length=200,
    key_chars=vigenere_breaker.ALPHABET,
)

# print(f"Key: {key}")
# print(f"Decrypted: {decrypted[:200]}...")
