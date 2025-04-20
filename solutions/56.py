import decrypter
import itertools
import string

"""
There is a word whose path's a word
Whose path's a word whose path's a letter;
It's one that every child has heard,
And means a place where things get wetter.
"""

"""
A veil begins, we all agree,
At vee, then travels nine, four, three.

A demo's route is one, eight, two,
And five, nine, ten's the course of glue.

This quandary now you may illumine:
What word, pray tell, has path of cumin?
"""


def get_path(s):
    # On a clock?
    # return [(ord(s[i]) - ord(s[i - 1])) % 13 for i in range(1, len(s))]
    return [(ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s))]


# abcdefghijklmnopqrstuvwxyz
#                      ^
#     ^   ^  ^


# abcdefghijklm
# nopqrstuvwxyz
# ^    ^    ^

get_path("veil")  # [9, 4, 3]
get_path("demo")  # [1, 8, 2]
get_path("glue")  # [5, 9, 10]
path = get_path("cumin")  # [18, 18, 22, 5]

for c in string.ascii_lowercase:
    word = c
    for d in path:
        c = string.ascii_lowercase[(string.ascii_lowercase.index(c) + d) % 26]
        word += c
    print(word)
# This doesn't yield any other words..?


def sub89(s1: str, s2: str) -> str:
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    if not s2:
        return s1

    alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
    c_to_index = {c: i for i, c in enumerate(alphabet)}
    nums1, nums2 = [[c_to_index[c] for c in s] for s in [s1, s2]]

    n = len(alphabet)
    result = []
    for a, b in zip(nums1, itertools.cycle(nums2)):
        result.append(alphabet[(a - b) % n])

    return "".join(result)


@decrypter.decrypter(chapter=56)
def decrypt(cipher: str) -> str:
    return sub89(cipher, "cuminbath")  # WIP: This is just a placeholder
