import decrypter


# line1 = ["when_dissolving_", "your_being_so_that", "_your_stock_of_primetime_", "games_is_sufficiently", "_hardy_remember_salt"]
# # SOLVI-NG_SO-METIM-ES_IS-_HARD

# line2 = ["we_nevertheless_", "want_to_let_you_know", "_that_down_around_", "your_neck_of_the_woods", "_is_an_unguarded_grove"]
# # NEVER-_LET_-DOWN_-YOUR_-GUARD


@decrypter.decrypter(chapter=16)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "SOLVING SOMETIMES IS HARD NEVER LET DOWN YOUR GUARD")
