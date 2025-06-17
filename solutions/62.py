import collections
import string

import decrypter

text = """
Dear Hugh,

At midnight, I have been trying to fix things in my mind.

Counting up things ... my excuses, my sins, my shortsightednesses, my anxieties, my wounds, my anguish, my former mistakes ... Counting up exactly my many EX-SLIP-UPs.

Hoping you're not unable to forgive
your
Suzi
"""

counts = collections.Counter(text.lower())
result = "".join(string.ascii_lowercase[counts[ch] - 1] for ch in "exslipup")
print(result)  # rescueme


@decrypter.decrypter(chapter=62)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "rescue me")


# from decrypter import vigenere_breaker

# reference_text = ""
# for chapter in range(61):
#     with open(f"data/{chapter:02}.chp", "r") as f:
#         reference_text += f.read()

# c = decrypter.decrypter(chapter=62)(lambda x: x)
# ciphertext = c.decrypt_one_chapter()[:500]

# decrypted, key = vigenere_breaker.break_vigenere_cipher(
#     ciphertext, reference_text, decrypter.vigenere_cipher
# )

# print(f"Key: {key}")
# print(f"Decrypted: {decrypted[:200]}...")
