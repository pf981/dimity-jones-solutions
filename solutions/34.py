import decrypter
import itertools


def is_solution(candidates, groups):
    for group in groups:
        if sum(c in group for c in candidates) != 1:
            return False
    return True


groups = [
    "zqgko",
    "juqkd",
    "qvpmg",
    "ahrst",
    "hnkau",
    "vnykq",
    "jkyzm",
    "fcznw",
    "dxhai",
    "qhijb",
    "latug",
    "tuizc",
]
letters = set("".join(groups))
solution = next(
    sorted(candidates)
    for candidates in itertools.combinations(letters, 5)
    if is_solution(candidates, groups)
)
key = ""
for i in range(len(solution)):
    key += solution[i]
    if i + 1 < len(solution):
        key += str(ord(solution[i + 1]) - ord(solution[i]) - 1)


@decrypter.decrypter(chapter=34)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, key)


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
# for chapter in range(28):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)
# reference_three_grams = get_normalised_three_grams(reference_text)


# text = '''hWlitsw ah t Irwti e Iodn tos ee
# , Iadert uh,se ev noty uo ,rwti eoPteir.e
#   - A-rbhamaC woel,y" rWtiet nniJ iueco  feLmmno."'''


# bests = []  # [(distance, sequence, text), ...]
# for block_size in range(5, 10):
#     sequence = [1] + list(range(3, block_size + 1))
#     best = (float("inf"), None, None)
#     for _ in range(200):
#         random.shuffle(sequence)
#         shuffled = decrypter.sequence_shuffle(
#             text, [2] + sequence
#         )  # Clearly starts with 'W'
#         distance = evaluate_fitness(
#             get_normalised_three_grams(shuffled), reference_three_grams
#         )

#         best = min(best, (distance, tuple([2] + sequence), shuffled))
#     bests.append(best)

# print(min(bests)[:2])
# print(min(bests)[2])
# # (1.9350260303058242, (2, 1, 4, 3, 6, 5))
# # Whilst what I write I do not see,
# # I dare thus, even to you, write Poetrie.
# #     --Abraham Cowley, "Written in Juice of Lemmon".
