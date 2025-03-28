# 3-gram statistics
# https://www.researchgate.net/publication/335732895_Cryptanalysis_of_the_Columnar_Transposition_Using_Meta-Heuristics

# I'm guessing it's normalised distance?

import collections
import decrypter
import random


def get_normalised_three_grams(text: str) -> collections.Counter[float]:
    three_grams = collections.Counter(
        text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 3, 3)
    )

    total = sum(three_grams.values())
    for three_gram in three_grams:
        three_grams[three_gram] /= total
    return three_grams


reference_text = []
for chapter in range(28):
    with open(f"data/{chapter:02}.chp") as f:
        reference_text.append(f.read())
reference_text = "".join(reference_text)

reference_three_grams = get_normalised_three_grams(reference_text)


with open("data/27.txt") as f:
    text = f.read().split("#####", 1)[1]
text = text.split("#", 1)[0]


def evaluate_fitness(
    three_grams: collections.Counter[float],
    reference_three_grams: collections.Counter[float],
) -> float:
    distance = 0

    for s in three_grams:
        distance += abs(three_grams[s] - reference_three_grams[s])

    for s in reference_three_grams:
        if s in three_grams:
            continue
        distance += abs(three_grams[s] - reference_three_grams[s])

    return distance


# evaluate_fitness(get_normalised_three_grams(text), reference_three_grams)

bests = []  # [(distance, sequence, text), ...]
for block_size in range(5, 40):
    sequence = list(range(1, block_size + 1))
    best = (float("inf"), None, None)
    for _ in range(200):
        random.shuffle(sequence)
        shuffled = decrypter.sequence_shuffle(text, sequence)
        distance = evaluate_fitness(
            get_normalised_three_grams(shuffled), reference_three_grams
        )

        best = min(best, (distance, tuple(sequence), shuffled))
    bests.append(best)

scores = [(distance, len(sequence)) for distance, sequence, _ in bests]
scores.sort()
print(scores)

print(min(bests)[2])


# 6 tends to win.

block_size = 6
sequence = list(range(1, block_size + 1))
best = (float("inf"), None, None)
for _ in range(10000):
    random.shuffle(sequence)
    shuffled = decrypter.sequence_shuffle(text, sequence)
    distance = evaluate_fitness(
        get_normalised_three_grams(shuffled), reference_three_grams
    )

    best = min(best, (distance, tuple(sequence), shuffled))

print(best[:2])
# 1.4150794626809498, (2, 1, 3, 5, 4, 6)
print(best[2])

import itertools

for block in itertools.batched(best[2], block_size):
    print("".join({'\n': '#', ' ': '_'}.get(c, c) else c for c in block))

    
for block in itertools.batched(best[2], 9):
    print("".join({'\n': '#', ' ': '_'}.get(c, c) for c in block))


# Well, it definitely starts with '"S' which is [5, 4]
bests = []  # [(distance, sequence, text), ...]
for block_size in range(5, 40):
    sequence = [1, 2, 3] + list(range(6, block_size + 1))
    best = (float("inf"), None, None)
    for _ in range(200):
        random.shuffle(sequence)
        shuffled = decrypter.sequence_shuffle(text, [5, 4] + sequence)
        distance = evaluate_fitness(
            get_normalised_three_grams(shuffled), reference_three_grams
        )

        best = min(best, (distance, tuple(sequence), shuffled))
    bests.append(best)

scores = [(distance, len(sequence)) for distance, sequence, _ in bests]
scores.sort()
print(scores)

min(bests)[:2]
# (1.4174558430612008, (6, 2, 1, 3))
print(min(bests)[2])


# So maybe we

# 6 and 2

# bests.sort(key=lambda x: x[0])

# bests[0]
...

# import decrypter
# import itertools
# import statistics

# # @decrypter.decrypter(chapter=28)
# # def decrypt(cipher: str) -> str:
# #     return decrypter.string_shuffle(cipher, "L6I4G2B1T1F1A1")


# @decrypter.decrypter(chapter=28)
# def decrypt(cipher: str) -> str:
#     return cipher


# chapter = decrypt.decrypt_chapter().split("#", 1)[0]
# 123456789012345678901234567890
# # 36 or 37
# # block_size_counts = []  # [(block_size, vowels, consonants, other), ...]
# stats = []  # [(block_size, avg_percent_vowel, stdev), ...]
# for block_size in range(5, 50):
#     percent_vowels = []
#     for block in itertools.batched(chapter, block_size):
#         vowels = consonants = other = 0
#         for c in block:
#             c = c.lower()
#             if c in "aeiou":
#                 vowels += 1
#             elif c.isalpha():
#                 consonants += 1
#             else:
#                 other += 1
#         if vowels or consonants:
#             percent_vowels.append(vowels / (vowels + consonants))
#         else:
#             percent_vowels.append(1)

#     avg_percent_vowel = statistics.mean(percent_vowels)
#     stdev = statistics.stdev(percent_vowels)
#     stats.append((block_size, avg_percent_vowel, stdev))

# stats.sort(key=lambda x: x[2])
# stats

# text = """
# Little Lance's father was trying to get Little Lance to eat his Brussels sprouts. "They're delicious, and very good for you."

# "I'll give them a little taste," Little Lance bargained at last, "but IF + I = GAG, I'm not going to eat them!"
# """

# uppers = [c for c in text if c.isupper()]
# collections.Counter(uppers)

# # First letters
# first_letters = [c for word in text.split() if (c := next((c for c in word if c.isalpha()), None))]
# collections.Counter(first_letters)

# # Observations
# #  IF + I = GAG
# #  There are a lot of L's.
# #  I really have no clue WHAT is being asked? The answer will have numbers and letters. Or just a number?
# #  Is it just asking for a numerical solution to I*F + I = G*A*G = ???. But there are inifitely many of those...
# #  How does the rest of the text fit in?
# #  "Little Lance" could mean stalagmite?
# #  Crystals are mentioned, so maybe refraction of the text?

# # IF + I = GAG
# # 4 1  3 = 423

# [ord(c.lower()) - ord('a') + 1 for c in text if c.isalpha()]

# # Sometimes A is greater than B
# # "Sometimes A" > "B"?

# inscription = "Sometimes A is greater than B"
# collections.Counter(inscription.lower())

# import collections


# counts = collections.Counter(text)
# # IF + I = GAG
# # 41 + 4 = 212
# counts['I']
# counts['F']
# counts['G']
# counts['A']
# # IF + I = GAG


# counts = collections.Counter(text.lower())
# print(f'{counts["i"]} {counts["f"]} + {counts["i"]} = {counts["g"]} {counts["a"]} {counts["g"]}')

# import string

# string.ascii_uppercase.index("I") + 1  # 9
# string.ascii_uppercase.index("F") + 1  # 6
# string.ascii_uppercase.index("G") + 1  # 7
# string.ascii_uppercase.index("A") + 1  # 1


# # 9 6 + 9 = 7 1 7


# 26 - string.ascii_uppercase.index("I")  # 18
# 26 - string.ascii_uppercase.index("F")  # 21
# 26 - string.ascii_uppercase.index("G")  # 20
# 26 - string.ascii_uppercase.index("A")  # 26

# # 18 21 + 18 = 20 26 20

# #                                                                                          Dimity  alphabetical A's F's G's
# #          1         2
# # 12345678901234567890
# # m aS"ow ebyevnec ohtotr eltes  sietreh  nttaiqeuot no ebrunmris sfs u?t"tseggemii dD" Lyt. ,akiebaeplhlalitcA'',y o ni snad,e  'i' Fmu,,s ,x s i' Gnadvee 'sa n n,'I  d'dl owu...eb en.n ieLl
# # "
# # "Some "
# # 546213
# # "So many we have no b"
# # "So many we even have both c"


# # t ynad9 ,epd9 ,6 ,1 ,7 ,nit7  eh  otapdekyst  .Ieencsreifb rutryl r eendT"h.d acnta eb t' A nti.,y wyateyinn xas-iinndn no' edkae tmevns ednrh unadde evns e.n"etehO,
#             1 1
# # 0123456789012
# # "egtI   !'i tsi 'A teiosmg remsre aet n'hta
# # "I get it! At most
# #       11
# # 04521630287
# #   ?  ?    ?

# import decrypter


# @decrypter.decrypter(chapter=28)
# def decrypt(cipher: str) -> str:
#     return cipher


# chapter = decrypt.decrypt_chapter()[:10000]
# # #                 ?           ?             ?
# # mini_seq = [0, 4, 5, 2, 1, 3, 6, 10, 12, 8, 7]
# mini_seq = [0, 4, '[', 5, ']', 2, 1, 3, '[', 6, ']', 10, 12, 8, '[', 7, ']']
# for i in range(1000):
#     chars = [chapter[i + di] if di not in ('[', ']') else di for di in mini_seq]
#     print(i, '\t', ''.join(chars))
# # 359

# #       11
# # 0452130287

# print(chapter)
