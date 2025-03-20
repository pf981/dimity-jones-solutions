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


@decrypter.decrypter(chapter=7)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(cipher, [6, 4, 2, 1, 7])


# z = [
#     "we",
#     "ing",
#     "visit",
#     "with a",
#     " puzzlers who meet doctor mogh should always remember to greet her ",
# ]
# sum(len(s) for s in z)
# "visit""ing"" puzzlers who meet doctor mogh should always remember to greet her ""with a""we"

# strings = [
#     "we",
#     "ing",
#     "ors ",
#     "visit",
#     "with a",
#     "nswers should not be made to wait if visit",
#     "lcome at all times in the castle when puzzl",
#     " persons who see doctor mogh will likely regret be",
#     "in lieu of a dog any cat or domesticated pet will s",
#     "if doctor mogh agrees to see us we hereby solemnly s",
#     "s to doctor mogh are welcome as long as every visitor ",
#     "ar that we will obey all posted and unposted rules that ",
#     "ppropriate precautions every person shall have a wonderful ",
#     " puzzlers who meet doctor mogh should always remember to greet her ",
#     "alth rewards the swiftest and the daring, but beauty will enrich who does the star",
# ]

# lengths = [len(s) for s in strings]

# 83
# import itertools

# possibilities = set()
# nums = lengths[:5]
# for w in range(1, len(nums) + 1):
#     for subset in itertools.combinations(nums, w):
#         possibilities.add(sum(subset))
# print(possibilities)

# 67 - 83


# 16 + 67
# for w in range(1, len(nums) + 1):
#     for subset in itertools.combinations(nums, w):
#         if sum(subset) == 16:
#             print(subset)
# pass

# Leland Dimity


# "How did you know which blocks to use"?
# 6421
# woaHv"  daiFdyk


#       8 13   9
# 4 2 1 7 9 11 13 14
# woaHv"  daiFdyk nuuonw {wuoh h-cEibkciobls o]tB u"?NeNs vrGa\medeWlIl imJiDDtr z,|yeeimrbtv g3nbitt (eqhh d'r(ik
# .Ryke


# # 7+4+14+6+1+15+11+8+5+10+2

# 6, 4, 2, 1, 7

# "with a" (1)
# " puzzlers who meet doctor mogh should always remember to greet her " (2)
# "in lieu of a dog any cat or domesticated pet will s" (3)
# "ing" (4)
# "if doctor mogh agrees to see us we hereby solemnly s" (5)
# "visit" (6)
# "we" (7)
# " persons who see doctor mogh will likely regret be" (8)
# "alth rewards the swiftest and the daring, but beauty will enrich who does the star" (9)
# "s to doctor mogh are welcome as long as every visitor " (10)
# "lcome at all times in the castle when puzzl" (11)
# "ar that we will obey all posted and unposted rules that " (12)
# "ppropriate precautions every person shall have a wonderful " (13)
# "ors " (14)
# "nswers should not be made to wait if visit" (15)


# "       we" (7)
# "    ing" (4)
# "              ors " (14)
# "      visit" (6)
# " with a" (1)
# "               nswers should not be made to wait if visit" (15)
# "           lcome at all times in the castle when puzzl" (11)
# " persons who see doctor mogh will likely regret be" (8)
# "in lieu of a dog any cat or domesticated pet will s" (3)
# "if doctor mogh agrees to see us we hereby solemnly s" (5)
# "s to doctor mogh are welcome as long as every visitor " (10)
# "ar that we will obey all posted and unposted rules that " (12)
# "ppropriate precautions every person shall have a wonderful " (13)
# " puzzlers who meet doctor mogh should always remember to greet her " (2)
# "alth rewards the swiftest and the daring, but beauty will enrich who does the star" (9)


# "we" (7)
# "ing" (4)
# "ors " (14)
# "visit" (6)
# "with a" (1)
# "nswers should not be made to wait if visit" (15)
# "lcome at all times in the castle when puzzl" (11)
# " persons who see doctor mogh will likely regret be" (8)
# "in lieu of a dog any cat or domesticated pet will s" (3)
# "if doctor mogh agrees to see us we hereby solemnly s" (5)
# "s to doctor mogh are welcome as long as every visitor " (10)
# "ar that we will obey all posted and unposted rules that " (12)
# "ppropriate precautions every person shall have a wonderful " (13)
# " puzzlers who meet doctor mogh should always remember to greet her " (2)
# "alth rewards the swiftest and the daring, but beauty will enrich who does the star" (9)


# "lcome at all times in the castle when puzzl"
# "visit""ors ""with a""nswers should not be made to wait if visit"
# " persons who see doctor mogh will likely regret be""ing"
#  (11)
#  (8)
# "in lieu of a dog any cat or domesticated pet will s" (3)

# "if doctor mogh agrees to see us we hereby solemnly s""we""ar that we will obey all posted and unposted rules that "
# "s to doctor mogh are welcome as long as every visitor " (10)
#  (12)
# "ppropriate precautions every person shall have a wonderful " (13)
# " puzzlers who meet doctor mogh should always remember to greet her " (2)
# "alth rewards the swiftest and the daring, but beauty will enrich who does the star" (9)
