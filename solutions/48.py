import decrypter

# text = """Dear Hugh,
#            It is fantastic to think that since our last
# meeting, I and you have written each other one letter
# a week through all the year's days (in total, on average, of
# course). Every letter I have gotten, I have cherished; every
# one written has been a joy. Poetic I'm not! -- we use a fifth
# of our brain's power, I've been told -- nor artistic; each word,
# though, has come readily, as if I'm under some wizards' spells
# granting charisma and eloquence unprecedented! No secret
# seems too dark to disclose; no however sly or candid message
# too elusive to develop; I write as I will, as intended,
# and wow, whoopee, out it flows like a bubbling stream! For
# it seems whenever it's you I write to, whenever whoever
# my mind's eye sees receiving this scrap is you, Fluency finds
# her way into my pen! I to each line's end can fly with this
# much lilting ease! Thanks are to him who receives this letter
# due, not
#           your inarticulate
#                              Suze"""

# # each line's end
# #   => last letter of every fifth word spells secret message intended for whoever finds this letter
# words = [
#     word2 for word in text.split() if (word2 := "".join(c for c in word if c.isalpha()))
# ]
# "".join(word[-1] for word in words[4::5])


@decrypter.decrypter(chapter=48)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(
        cipher, "cruelly incarcerated please spring me"
    )
