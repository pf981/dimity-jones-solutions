import decrypter
import itertools


def chunk_shuffle(cipher: str, sequence: list[int], chunk_size: int | None = None):
    if chunk_size is None:
        chunk_size = max(sequence)

    result = []
    for buffer in itertools.batched(cipher, chunk_size):
        if len(buffer) < chunk_size:
            result.extend(buffer)
            break
        for i in sequence:
            result.append(buffer[i - 1])

    return "".join(result)


def get_alphabetical_transposition_key(s: str):
    chars = [c.upper() for c in s if c.isalpha()]
    ranks = sorted(enumerate(chars), key=lambda pair: pair[1])

    key = [0] * len(chars)
    for i, (j, _) in enumerate(ranks, 1):
        key[j] = i

    return key


# line1 = ["when_dissolving_", "your_being_so_that", "_your_stock_of_primetime_", "games_is_sufficiently", "_hardy_remember_salt"]
# # SOLVI-NG_SO-METIM-ES_IS-_HARD

# line2 = ["we_nevertheless_", "want_to_let_you_know", "_that_down_around_", "your_neck_of_the_woods", "_is_an_unguarded_grove"]
# # NEVER-_LET_-DOWN_-YOUR_-GUARD


@decrypter.decrypter(chapter=16)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(
        cipher,
        get_alphabetical_transposition_key("SOLVING SOMETIMES IS HARD NEVER LET DOWN YOUR GUARD")
    )
