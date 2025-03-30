import decrypter


@decrypter.decrypter(chapter=37)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [7, 6, 5, 1, 3, 2, 8, 4])


# import collections
# import decrypter
# import itertools


# def get_normalised_three_grams(text: str) -> collections.Counter[float]:
#     three_grams = collections.Counter(
#         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 3, 3)
#     )

#     total = sum(three_grams.values())
#     for three_gram in three_grams:
#         three_grams[three_gram] /= total
#     return three_grams


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


# reference_text = []
# for chapter in range(36):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)
# reference_three_grams = get_normalised_three_grams(reference_text)


# with open("data/36.txt") as f:
#     text = f.read().split("#####", 1)[1]
# text = text.split("#", 1)[0]


# # heap = [] # [(distance, sequence, text), ...]
# best = (float("inf"), None, None)  # (distance, sequence, text)
# nums = tuple(range(1, 9))
# for sequence in itertools.permutations(nums):
#     shuffled = decrypter.sequence_shuffle(text, sequence)
#     distance = evaluate_fitness(
#         get_normalised_three_grams(shuffled), reference_three_grams
#     )

#     best = min(best, (distance, sequence, shuffled))

# print(best[:2])
# # 1.7478498444680888, (7, 6, 5, 1, 3, 2, 8, 4)
