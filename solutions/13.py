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


text = """
H.:

(I mean nothing puritanical by resorting thus to your initial, my
sweet woodchuck; I am only practicing nonchalance!)

It has been eleven years since that lucky, magical day that I and you
first met. I'll never forget how you primed my unpurring pump with
your zany jokes and soft, smiling eyes. Zowie!

And I remember your first letter's charming evasiveness and truly
touching reluctance to come right out and announce your smittenness!
(Now, of course, I know that you'd fallen in love with me, too. How
utterly exhilarating to think it, to be able to say it truthfully!)

And ever since, nothing's been able to dampen my happiness for long.

I eagerly await the next letter from you. Whether you write a lot or
a little is not of prime importance. Just write!

Love, S.
"""

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541}

words = text.split()
key = ''.join(next(c for c in word if c.isalpha()) for i, word in enumerate(words, 1) if i in primes)
# ImprisonedInpuzZlecastlesendhelp


@decrypter.decrypter(chapter=13)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(
        cipher,
        get_alphabetical_transposition_key(key)
    )
