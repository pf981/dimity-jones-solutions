import decrypter

# # What persons glimpse what here is not
# # Appear the friends that long I've sought.
# # What hero dares a doughty deed
# # Does prove himself of stalwart breed.
# # What woman does what winners do
# # Will be thereby called winner, too.
# # What children see what's hidden here
# # To me will those themselves endear.

# # peer_
# # past_
# # the_g
# # rille
# # _made
# # _by_t
# # hese_
# # moths

# text = """When you propose your fiends to smite
# Mirages melt for hotter sight.
# If flies are nude, do oceans thirst?
# If coaches play us, who serves first?
# When kiwis taste of something posh
# The innuendoes prove it's squash.
# Whenever wastrels freeze like ice
# Will I pluck out the lady's lice."""

# mask = """What **rsons glimps* what he*e is*not
# A*pe*r the friend* *hat*long I've sought.
# Wha* *ero dar*s*a dou*hty deed
# Does p*ove h*mse*f of sta*wart bre*d.
# What*wo**n *oes what winn*rs do
# Will**e thereb* called*winner, *oo.
# What c*ildr*n *ee what's hidd*n*here
# To *e will th*se **emselve* endear."""

# for line, mask_line in zip(text.splitlines(), mask.splitlines()):
#     print("".join(c1 for c1, c2 in zip(line, mask_line) if c2 == "*"))


@decrypter.decrypter(chapter=49)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(
        cipher,
        "peer past the grille made by these moths\nyou might find clues within these cloths",
    )
