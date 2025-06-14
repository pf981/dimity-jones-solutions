import decrypter


@decrypter.decrypter(chapter=60)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "cigar, quoit")


# import collections
# import itertools
# import string

# dec = decrypter.decrypter(chapter=60)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:5000]

# key = "cigar, quoit"
# plain = decrypter.vigenere_cipher(ciphertext, key)

# print(plain)

# for a, b in zip(plain[:220], itertools.cycle(key)):
#     print(a, b)

# alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
# have, want, key = r"# u"
# alphabet[
#     (alphabet.index(have) - (alphabet.index(want) - alphabet.index(key)))
#     % len(alphabet)
# ]


# def position_sample(text: str, positions: tuple[int], block_size: int) -> str:
#     if block_size <= max(positions):
#         return ValueError("Block size must be smaller than all positions")

#     result = []
#     for block in itertools.batched(text, block_size):
#         if len(block) != block_size:
#             break
#         result.append("".join(block[i] for i in positions))

#     return "".join(result)


# def get_normalised_ngrams(text: str, block_sizes: list[int] = [3]) -> dict[str, float]:
#     normalized = {}
#     for block_size in block_sizes:
#         frequencies = collections.Counter(
#             text[i : i + block_size]
#             for i in range(0, len(text) - block_size, block_size)
#         )

#         total = sum(frequencies.values())
#         for block in frequencies:
#             normalized[block] = frequencies[block] / total
#     return normalized


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
# ciphertext = dec.decrypt_one_chapter()[:5000]

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

#             cipher_sample = position_sample(ciphertext, positions, 12)
#             decyphered_sample = decrypter.vigenere_cipher(cipher_sample, key)

#             reference_sample = position_sample(reference_text, positions, 12)

#             # decyphered_freqs = get_normalised_ngrams(decyphered_sample, [1, 2, 3])
#             # reference_freqs = get_normalised_ngrams(reference_sample, [1, 2, 3])
#             decyphered_freqs = get_normalised_ngrams(decyphered_sample, [3])
#             reference_freqs = get_normalised_ngrams(reference_sample, [3])

#             fit = evaluate_fitness(decyphered_freqs, reference_freqs)
#             if fit < best_fitness:
#                 best_fitness = fit
#                 best_chars = key[0] + key[-1]
#             # print(key, fit)
#     print(best_chars, best_fitness)
#     # print()
#     # print()
