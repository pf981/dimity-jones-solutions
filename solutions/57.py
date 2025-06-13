import decrypter
# import string
# import z3


# text = """
# Cub reporter Ivy Kildare, almost too late to see the beheading, arrived breathless by bike.

# "Lad," Prince Thaddeus was saying, "when you are ready, and have taken aim, you may, at will -- fire."

# "Of rifles however no sign," puzzled Ivy's pen.

# "Oof!" cried the condemned man, though the blow fell upon his nape no more heavily than a stone of hail.

# "Ax isn't sharp," feebly muttered the royal executioner (who, no lad, had been salvaged from superannuation for this job) as the frenzied crowd began to boo.

# "Rub it on the whetstone," hissed the royal cremator, "or stand there like a fool and gawp!"

# "Do hurry," whispered the royal urn-keeper, polishing the urn.

# "Tad," pleaded the doomed man (for he would not call the prince, his former lover, "Sire"). "Be a pal and get me out of this jam."

# He looked up into the prince's eyes, and the prince looked down into his.

# ("Me a jam and get be out of this pal," hastily jotted Ivy.)

# "My will is firm," declared the prince at last, and grandiosely turned away, while silently imploring his heart not to break, not to break, not yet.
# """

# sentences = text.replace("\n", ".").split(".")
# pairs = []
# for sentence in sentences:
#     words = [
#         "".join(c for c in word if c.isalpha())
#         for word in sentence.lower().strip().split(" ")
#     ]
#     if len(words) < 2:
#         continue
#     first, *_, last = words
#     pairs.append((first, last))

# o = z3.Solver()
# # o = z3.Optimize()
# o.set("arith.solver", 2) # Not sure what this does, but it is signficantly faster

# letters = {c: z3.Int(c) for c in string.ascii_lowercase}
# for c, letter in letters.items():
#     o.add(letter <= 26)
#     o.add(letter >= 1)
#     for c2, other_letter in letters.items():
#         if c != c2:
#             o.add(letter != other_letter)

# o.add(letters["p"] == 1)
# o.add(letters["o"] == 2)
# o.add(letters["e"] == 3)
# o.add(letters["z"] != 19)  # This solution didn't work

# for first, last in pairs:
#     c = last[0]
#     for c1, c2 in zip(first, last[1:]):
#         o.add(((letters[c] + letters[c1] - 1) % 26) + 1 == letters[c2])
#         c = c2

# if not o.check() == z3.sat:
#     raise ValueError("No solution")

# result = [""] * 26
# for c in string.ascii_lowercase:
#     pos = o.model()[letters[c]].as_long() - 1
#     result[pos] = c
# result = "".join(result)


@decrypter.decrypter(chapter=57)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "poehwakimjscfrdnvgqylbtzux"[-23:])
