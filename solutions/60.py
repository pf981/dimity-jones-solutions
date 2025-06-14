import collections
import decrypter
import itertools
import string


@decrypter.decrypter(chapter=60)
def decrypt(cipher: str) -> str:
    # Pretty sure first word ends in "r" => ....r, ....t
    return decrypter.vigenere_cipher(cipher, "cigar, quoit")  # GOOD
    # return decrypter.vigenere_cipher(cipher, "cugar, qioit")  # GOOD
    # return decrypter.vigenere_cipher(cipher, "digar, puoit")  # GOOD
    # return decrypter.vigenere_cipher(cipher, "diggz, puocl")  # not bad
    # return decrypter.vigenere_cipher(cipher, "digaz, puoil")  # good
    # return decrypter.vigenere_cipher(cipher, "injdr, kplft")  # not bad
    # return decrypter.vigenere_cipher(cipher, "fqiap, nmmiv") # bad
    # return decrypter.vigenere_cipher(cipher, "cigoau, quits")
    # return decrypter.vigenere_cipher(cipher, "cigoau, quoiq") # bad
    # Starts with e, ends with r - eh
    # # Starts with r.... b....
    # return decrypter.vigenere_cipher(cipher, "rmudu, bqafq") # bad
    # return decrypter.vigenere_cipher(cipher, "enddr, oprft") # bad
    # return decrypter.vigenere_cipher(cipher, "emhdq, oqnfu") # badish
    # return decrypter.vigenere_cipher(cipher, "enter, oprft") # bad


# key = "digar, puoit"
# key = "cigar, quoit"
# plain = decrypter.vigenere_cipher(ciphertext, key)

# print(plain)

# for a, b in zip(plain[:220], itertools.cycle(key)):
#     print(a, b)


alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""

have, want, key = r"# u"
alphabet[
    (alphabet.index(have) - (alphabet.index(want) - alphabet.index(key)))
    % len(alphabet)
]


def position_sample(text: str, positions: tuple[int], block_size: int) -> str:
    if block_size <= max(positions):
        return ValueError("Block size must be smaller than all positions")

    result = []
    for block in itertools.batched(text, block_size):
        if len(block) != block_size:
            break
        result.append("".join(block[i] for i in positions))

    return "".join(result)


# def get_normalised_frequencies(blocks: list[str]) -> dict[str, float]:
#     freqs = collections.Counter(blocks)
#     total = sum(freqs.values())
#     normalized = {}
#     for block in freqs:
#         normalized[block] = freqs[block] / total
#     return normalized


def get_normalised_ngrams(text: str, block_sizes: list[int] = [3]) -> dict[str, float]:
    normalized = {}
    for block_size in block_sizes:
        frequencies = collections.Counter(
            text[i : i + block_size]
            for i in range(0, len(text) - block_size, block_size)
        )

        total = sum(frequencies.values())
        for block in frequencies:
            normalized[block] = frequencies[block] / total
    return normalized


# def get_normalised_three_grams(text: str) -> dict[str, float]:
#     three_grams = collections.Counter(
#         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 2, 3)
#     )

#     total = sum(three_grams.values())
#     normalized = {}
#     for three_gram in three_grams:
#         normalized[three_gram] = three_grams[three_gram] / total
#     return normalized


def evaluate_fitness(
    freqs: dict[str, float],
    reference_freqs: dict[str, float],
) -> float:
    distance = 0
    all_grams = set(freqs.keys()) | set(reference_freqs.keys())

    for gram in all_grams:
        freq1 = freqs.get(gram, 0)
        freq2 = reference_freqs.get(gram, 0)
        distance += abs(freq1 - freq2)

    return distance


dec = decrypter.decrypter(chapter=60)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:500]
ciphertext = dec.decrypt_one_chapter()[:5000]

reference_text = []
for chapter in range(55):
    with open(f"data/{chapter:02}.chp") as f:
        reference_text.append(f.read())
reference_text = "".join(reference_text)


# key_template = "?????, ?????"
mid = "jokes"
for i in range(5):
    i_mid = string.ascii_lowercase.index(mid[i])
    best_chars = ""
    best_fitness = float("inf")

    for d in range(1, 26):
        l = i_mid - d
        r = i_mid + d
        if l < 0 or r >= 26:
            break

        for l, r in [(l, r), (r, l)]:
            key = f"{string.ascii_lowercase[l]}, {string.ascii_lowercase[r]}"
            positions = (i, 11 - i)

            cipher_sample = position_sample(ciphertext, positions, 12)
            decyphered_sample = decrypter.vigenere_cipher(cipher_sample, key)

            reference_sample = position_sample(reference_text, positions, 12)

            # decyphered_freqs = get_normalised_ngrams(decyphered_sample, [1, 2, 3])
            # reference_freqs = get_normalised_ngrams(reference_sample, [1, 2, 3])
            decyphered_freqs = get_normalised_ngrams(decyphered_sample, [3])
            reference_freqs = get_normalised_ngrams(reference_sample, [3])

            fit = evaluate_fitness(decyphered_freqs, reference_freqs)
            if fit < best_fitness:
                best_fitness = fit
                best_chars = key[0] + key[-1]
            # print(key, fit)
    print(best_chars, best_fitness)
    # print()
    # print()


# def position_sample(text: str, positions: tuple[int], block_size: int) -> list[str]:
#     if block_size <= max(positions):
#         return ValueError("Block size must be smaller than all positions")

#     result = []
#     for block in itertools.batched(text, block_size):
#         if len(block) != block_size:
#             break
#         result.append("".join(block[i] for i in positions))

#     return result


# def get_normalised_frequencies(blocks: list[str]) -> dict[str, float]:
#     freqs = collections.Counter(blocks)
#     total = sum(freqs.values())
#     normalized = {}
#     for block in freqs:
#         normalized[block] = freqs[block] / total
#     return normalized


# # def get_normalised_three_grams(text: str) -> dict[str, float]:
# #     three_grams = collections.Counter(
# #         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 2, 3)
# #     )

# #     total = sum(three_grams.values())
# #     normalized = {}
# #     for three_gram in three_grams:
# #         normalized[three_gram] = three_grams[three_gram] / total
# #     return normalized


# def evaluate_fitness(
#     freqs: dict[str, float],
#     reference_freqs: dict[str, float],
# ) -> float:
#     distance = 0
#     all_grams = set(freqs.keys()) | set(reference_freqs.keys())

#     for gram in all_grams:
#         freq1 = freqs.get(gram, 0)
#         freq2 = reference_freqs.get(gram, 0)
#         distance += abs(freq1 - freq2)

#     return distance


# dec = decrypter.decrypter(chapter=60)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:500]

# reference_text = []
# for chapter in range(55):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)


# # key_template = "?????, ?????"
# mid = "jokes"
# for i in range(5):
#     i_mid = string.ascii_lowercase.index(mid[i])
#     best_chars = ""
#     best_fitness = float("inf")

#     for d in range(1, 26):
#         l = i_mid - d
#         r = i_mid + d
#         if l < 0 or r >= 26:
#             break

#         for l, r in [(l, r), (r, l)]:
#             key = f"{string.ascii_lowercase[l]}, {string.ascii_lowercase[r]}"
#             positions = (i, 11 - i)

#             cipher_sample = "".join(position_sample(ciphertext, positions, 12))
#             decyphered_sample = decrypter.vigenere_cipher(cipher_sample, key)

#             decyphered_blocks = []
#             for block in itertools.batched(decyphered_sample, len(positions)):
#                 if len(block) != 5:
#                     break
#                 decyphered_blocks.append("".join(block))

#             reference_blocks = position_sample(reference_text, positions, 12)

#             decyphered_freqs = get_normalised_frequencies(decyphered_blocks)
#             reference_freqs = get_normalised_frequencies(reference_blocks)

#             fit = evaluate_fitness(decyphered_freqs, reference_freqs)
#             if fit < best_fitness:
#                 best_fitness = fit
#                 best_chars = key[0] + key[-1]
#             # print(key, fit)
#     print(best_chars, best_fitness)
#     # print()
#     # print()


# def position_sample(text: str, positions: tuple[int], block_size: int) -> list[str]:
#     if block_size <= max(positions):
#         return ValueError("Block size must be smaller than all positions")

#     result = []
#     for block in itertools.batched(text, block_size):
#         if len(block) != block_size:
#             break
#         result.append("".join(block[i] for i in positions))

#     return result


# def get_normalised_frequencies(blocks: list[str]) -> dict[str, float]:
#     freqs = collections.Counter(blocks)
#     total = sum(freqs.values())
#     normalized = {}
#     for block in freqs:
#         normalized[block] = freqs[block] / total
#     return normalized


# # def get_normalised_three_grams(text: str) -> dict[str, float]:
# #     three_grams = collections.Counter(
# #         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 2, 3)
# #     )

# #     total = sum(three_grams.values())
# #     normalized = {}
# #     for three_gram in three_grams:
# #         normalized[three_gram] = three_grams[three_gram] / total
# #     return normalized


# def evaluate_fitness(
#     freqs: dict[str, float],
#     reference_freqs: dict[str, float],
# ) -> float:
#     distance = 0
#     all_grams = set(freqs.keys()) | set(reference_freqs.keys())

#     for gram in all_grams:
#         freq1 = freqs.get(gram, 0)
#         freq2 = reference_freqs.get(gram, 0)
#         distance += abs(freq1 - freq2)

#     return distance


# dec = decrypter.decrypter(chapter=60)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:500]

# reference_text = []
# for chapter in range(55):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)


# # key_template = "?????, ?????"
# mid = "jokes"
# for i in range(5):
#     i_mid = string.ascii_lowercase.index(mid[i])
#     best_chars = ""
#     best_fitness = float("inf")

#     for d in range(1, 26):
#         l = i_mid - d
#         r = i_mid + d
#         if l < 0 or r >= 26:
#             break

#         for l, r in [(l, r), (r, l)]:
#             key = f"{string.ascii_lowercase[l]}, {string.ascii_lowercase[r]}"
#             positions = (i, 5, 6, 11 - i)

#             cipher_sample = "".join(position_sample(ciphertext, positions, 12))
#             decyphered_sample = decrypter.vigenere_cipher(cipher_sample, key)

#             decyphered_blocks = []
#             for block in itertools.batched(decyphered_sample, 5):
#                 if len(block) != 5:
#                     break
#                 decyphered_blocks.append("".join(block))

#             reference_blocks = position_sample(reference_text, positions, 12)

#             decyphered_freqs = get_normalised_frequencies(decyphered_blocks)
#             reference_freqs = get_normalised_frequencies(reference_blocks)

#             fit = evaluate_fitness(decyphered_freqs, reference_freqs)
#             if fit < best_fitness:
#                 best_fitness = fit
#                 best_chars = key[0] + key[-1]
#             print(key, fit)
#     print(best_chars, best_fitness)
#     print()
#     print()

# key.index(",")  # 5
# len(key)

# sample = position_sample(ciphertext, (1, 2, 3), 5)
# gram = get_normalised_three_grams(sample)
# evaluate_fitness(gram, gram)

# """
# If Ace and Cow convene at Bin,
# And Crab and Oven join at Itch,
# And Yuks and Magi flock at Skin,
# Two friends will meet at Jokes -- but which?
# """


# import collections
# import decrypter
# import itertools
# import string


# def position_sample(text: str, positions: tuple[int], block_size: int):
#     if block_size <= max(positions):
#         return ValueError("Block size must be smaller than all positions")

#     result = []
#     for block in itertools.batched(text, block_size):
#         if len(block) != block_size:
#             break
#         result.append("".join(block[i] for i in positions))

#     return "".join(result)


# def get_normalised_three_grams(text: str) -> dict[str, float]:
#     three_grams = collections.Counter(
#         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 2, 3)
#     )

#     total = sum(three_grams.values())
#     normalized = {}
#     for three_gram in three_grams:
#         normalized[three_gram] = three_grams[three_gram] / total
#     return normalized


# def evaluate_fitness(
#     freqs: dict[str, float],
#     reference_freqs: dict[str, float],
# ) -> float:
#     distance = 0
#     all_grams = set(freqs.keys()) | set(reference_freqss.keys())

#     for gram in all_grams:
#         freq1 = freqs.get(gram, 0)
#         freq2 = reference_freqs.get(gram, 0)
#         distance += abs(freq1 - freq2)

#     return distance


# dec = decrypter.decrypter(chapter=60)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:500]

# reference_text = []
# for chapter in range(55):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)


# # key_template = "?????, ?????"
# mid = "jokes"
# for i in range(5):
#     i_mid = string.ascii_lowercase.index(mid[i])
#     best_chars = ""
#     best_fitness = float("inf")

#     for d in range(1, 26):
#         l = i_mid - d
#         r = i_mid + d
#         if l < 0 or r >= 26:
#             break

#         for l, r in [(l, r), (r, l)]:
#             key = f"{string.ascii_lowercase[l]}, {string.ascii_lowercase[r]}"
#             positions = (i, 5, 6, 11 - i)

#             cipher_sample = position_sample(ciphertext, positions, 12)
#             decyphered_sample = decrypter.vigenere_cipher(cipher_sample, key)
#             reference_sample = position_sample(reference_text, positions, 12)

#             decyphered_three_grams = get_normalised_three_grams(decyphered_sample)
#             reference_three_grams = get_normalised_three_grams(reference_sample)

#             fit = evaluate_fitness(decyphered_three_grams, reference_three_grams)
#             if fit < best_fitness:
#                 best_fitness = fit
#                 best_chars = key[0] + key[-1]
#             # print(key, fit)
#     print(best_chars, best_fitness)
#     # print()
#     # print()

# # key.index(",")  # 5
# # len(key)

# # sample = position_sample(ciphertext, (1, 2, 3), 5)
# # gram = get_normalised_three_grams(sample)
# # evaluate_fitness(gram, gram)

# # """
# # If Ace and Cow convene at Bin,
# # And Crab and Oven join at Itch,
# # And Yuks and Magi flock at Skin,
# # Two friends will meet at Jokes -- but which?
# # """


# @decrypter.decrypter(chapter=60)
# def decrypt(cipher: str) -> str:
#     return decrypter.vigenere_cipher(cipher, "cigoau, quits")
#     # return decrypter.vigenere_cipher(cipher, "cigoau, quoiq")
#     # Starts with e, ends with r - eh
#     # # Starts with r.... b....
#     # return decrypter.vigenere_cipher(cipher, "rmudu, bqafq")
#     # return decrypter.vigenere_cipher(cipher, "enddr, oprft")
#     # return decrypter.vigenere_cipher(cipher, "emhdq, oqnfu")
#     # return decrypter.vigenere_cipher(cipher, "enter, oprft")
