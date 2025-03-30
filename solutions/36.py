import decrypter


# groups = [
#     "tbrqfxzy",
#     "qsjoimgf",
#     "pzwyeltx",
#     "onvqdcla",
#     "syupzngx",
#     "btasunjm",
#     "jaesgutc",
#     "zumbrqof",
#     "xzrswnuc",
#     "mlfbxhrw",
#     "qmvxacne",
#     "csfktivh",
#     "vxfowicb",
#     "cezbuhdv",
#     "wfknqpoe",
# ]
# nth_letter_groups = list(zip(*groups))
# result = []
# solved_count = [0] * len(groups)


# def backtrack(i):
#     if i == len(nth_letter_groups):
#         return all(count == 1 for count in solved_count)

#     for c in nth_letter_groups[i]:
#         if c in result:
#             continue

#         result.append(c)
#         for j, c2 in enumerate(nth_letter_groups[i]):
#             if c2 == c:
#                 solved_count[j] += 1

#         if all(count <= 1 for count in solved_count) and backtrack(i + 1):
#             return True

#         result.pop()
#         for j, c2 in enumerate(nth_letter_groups[i]):
#             if c2 == c:
#                 solved_count[j] -= 1

#     return False


# backtrack(0)
# key = "".join(result)
# # 'tefsicox'


@decrypter.decrypter(chapter=36)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "tefsicox")
