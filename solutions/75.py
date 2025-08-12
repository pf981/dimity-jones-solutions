import decrypter

text = """My dearest Hugh ...
It was great to get your latest letter. Thank you.
I find it hard to write today. It's something merely
to do with the weather I'd bet. Although I am by now
a veteran epistolist (do you think that's the word?),
still I find every letter under a period of rain
is difficult to write ... Yes, when the sky is grey
I get a pain in my forehead. But don't worry. I'm
fine. Everything is, actually, fine. I'm well enough.
Cannot seem to write, that's all. Guess I will have to
just put this aside to finish another day. In the
meantime, I will think of you ... and draft a love note
in my mind. Wish you weren't there!
Love, Suzie"""

lines = text.splitlines()
key = ""
for r in range(len(lines) - 1):
    for c1, c2 in zip(lines[r], lines[r + 1]):
        if c1 == ".":
            key += c2


@decrypter.decrypter(chapter=75)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "get me the hell out of here")
