import decrypter

text = """Dear Hughie
This will probably be a short note today.
The fact is I feel a bit off-kilter
or imbalanced or lopsided this morning.
It is probably not much to worry about.
I know that if you were here I would feel centered!
Rest assured that is not a complaint.
I know we can't, because of your work, be
together all the time. That's just fine
with me, really. I cannot imagine being
in somebody's company day in day out.
Actually our penpalship satisfies
my every need (almost!). You see into me,
restoring my lost equilibrium, bringing relief.
Much love, your
Suzie xxo"""

key = "".join(line[len(line) // 2].lower() for line in text.splitlines())


@decrypter.decrypter(chapter=67)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)
