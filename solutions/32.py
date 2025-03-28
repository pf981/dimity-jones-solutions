import collections
import decrypter

text = """
Dear Hugh,

How I love to say your dear name, Hugh!

I save the name I was given -- Susan -- and say it only if someone
asks me. (From your mouth though -- oh my! -- how delightful it
sounds!)

Oh, we all feel our name, our body, our past, is only a jailer; we
all want to be someone else, want to be a pilot, or be the mother of
a prince, or a doctor, or the pilot of a prince -- someone! Want to
feel that we are -- want to be! -- unique, unique, ONLY UNIQUE,
without name, without body, and without past!

Though, given the facts, it is only a delightful fantasy. (Or are
facts only mouth sounds? Only if fantasy is what was, what is, what
might be inside us that asks what else might be, what else is, what
else was inside us!)

Love,
Your
Susan Mogh
"""

words = [
    word
    for part in text.split()
    if (word := "".join(c.lower() for c in part if c.isalpha()))
]
counts = collections.Counter(words)
uniques = [word for word, count in counts.items() if count == 1]


@decrypter.decrypter(chapter=32)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, " ".join(uniques))
