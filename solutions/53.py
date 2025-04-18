import decrypter
# import string


# text = """Sweetheartkin,

# O Hugh, I feel this embarrassing sting when unconsciously I
# underestimate a signification.

# Measurementally unhandy, bungling, dim, I measure badly, most
# approximately, never precisely!

# I misappreciate everybody. Bewilderedness is a bane! Minglemangling,
# never quite ever particularizing ...

# Indeed, I, maladroit, feel sentenced to sadly imitate all
# misapprehensive cabinetmakers who've miscut, lamenting
# disconsolately, "Damn, I underestimated your length!"

# Overoptimistically (?) yours,
# Yours sentimentally,
# Susan"""

# words = "".join(c.lower() for c in text if c.isalpha() or c in " \n").split()

# print("".join([string.ascii_lowercase[len(word) - 1] for word in words]))


@decrypter.decrypter(chapter=53)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(
        cipher,
        "mad addled mama mogh caged me i am in bad need of aid i beg come find and free me",
    )
