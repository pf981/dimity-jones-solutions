import decrypter


@decrypter.decrypter(chapter=28)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [5, 4, 6, 2, 1, 3])


# # 3-gram statistics
# # https://www.researchgate.net/publication/335732895_Cryptanalysis_of_the_Columnar_Transposition_Using_Meta-Heuristics

# # I'm guessing it's normalised distance?

# import collections
# import decrypter
# import random


# def get_normalised_three_grams(text: str) -> collections.Counter[float]:
#     three_grams = collections.Counter(
#         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 3, 3)
#     )

#     total = sum(three_grams.values())
#     for three_gram in three_grams:
#         three_grams[three_gram] /= total
#     return three_grams


# reference_text = []
# for chapter in range(28):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)

# reference_three_grams = get_normalised_three_grams(reference_text)


# with open("data/27.txt") as f:
#     text = f.read().split("#####", 1)[1]
# text = text.split("#", 1)[0]


# def evaluate_fitness(
#     three_grams: collections.Counter[float],
#     reference_three_grams: collections.Counter[float],
# ) -> float:
#     distance = 0

#     for s in three_grams:
#         distance += abs(three_grams[s] - reference_three_grams[s])

#     for s in reference_three_grams:
#         if s in three_grams:
#             continue
#         distance += abs(three_grams[s] - reference_three_grams[s])

#     return distance


# # evaluate_fitness(get_normalised_three_grams(text), reference_three_grams)

# bests = []  # [(distance, sequence, text), ...]
# for block_size in range(5, 40):
#     sequence = list(range(1, block_size + 1))
#     best = (float("inf"), None, None)
#     for _ in range(200):
#         random.shuffle(sequence)
#         shuffled = decrypter.sequence_shuffle(text, sequence)
#         distance = evaluate_fitness(
#             get_normalised_three_grams(shuffled), reference_three_grams
#         )

#         best = min(best, (distance, tuple(sequence), shuffled))
#     bests.append(best)

# scores = [(distance, len(sequence)) for distance, sequence, _ in bests]
# scores.sort()
# print(scores)

# print(min(bests)[2])


# # 6 tends to win.

# block_size = 6
# sequence = list(range(1, block_size + 1))
# best = (float("inf"), None, None)
# for _ in range(10000):
#     random.shuffle(sequence)
#     shuffled = decrypter.sequence_shuffle(text, sequence)
#     distance = evaluate_fitness(
#         get_normalised_three_grams(shuffled), reference_three_grams
#     )

#     best = min(best, (distance, tuple(sequence), shuffled))

# print(best[:2])
# # 1.4150794626809498, (2, 1, 3, 5, 4, 6)
# print(best[2])

# import itertools

# for block in itertools.batched(best[2], block_size):
#     print("".join({'\n': '#', ' ': '_'}.get(c, c) else c for c in block))


# for block in itertools.batched(best[2], 9):
#     print("".join({'\n': '#', ' ': '_'}.get(c, c) for c in block))


# # Well, it definitely starts with '"S' which is [5, 4]
# bests = []  # [(distance, sequence, text), ...]
# for block_size in range(5, 40):
#     sequence = [1, 2, 3] + list(range(6, block_size + 1))
#     best = (float("inf"), None, None)
#     for _ in range(200):
#         random.shuffle(sequence)
#         shuffled = decrypter.sequence_shuffle(text, [5, 4] + sequence)
#         distance = evaluate_fitness(
#             get_normalised_three_grams(shuffled), reference_three_grams
#         )

#         best = min(best, (distance, tuple(sequence), shuffled))
#     bests.append(best)

# scores = [(distance, len(sequence)) for distance, sequence, _ in bests]
# scores.sort()
# print(scores)

# min(bests)[:2]
# # (1.4174558430612008, (6, 2, 1, 3))
# print(min(bests)[2])
