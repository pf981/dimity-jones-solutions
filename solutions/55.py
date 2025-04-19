import decrypter
import itertools


def add(s1: str, s2: str) -> str:
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    if not s2:
        return s1

    nums1, nums2 = [[ord(c) - ord("A") + 1 for c in s] for s in [s1, s2]]

    result = []
    for a, b in zip(nums1, itertools.cycle(nums2)):
        num = ((a + b - 1) % 26) + 1
        c = chr(num + ord("A") - 1)
        result.append(c)

    return "".join(result)


def sub(s1: str, s2: str) -> str:
    s2 = "".join(chr(((ord("Z") - ord(c) - 1) % 26) + ord("A")) for c in s2)
    return add(s1, s2)


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


text = """
The Ballad of Peale's Rum

The marauders keelhauled our Captain Peale.
"Sir, your buried liquor plan we to take,
So divulge its spot, for your children's sake."
But the Captain bravely refused to squeal.

"This deceitful, villainous blackguard," said
Their doyenne, aghast, "basely chafes my calm."
To her fiercest henchman she turned her head
And invited him, with an upturned palm,

"From the brimful cup of your fisticuff,
Won't you give him, Henry, a little sip?
Aye, jar his memory just enough
That it blossoms under your tutorship."

Well, the pirate princess attained her will:
Of our captain's screams we soon had our fill,
And revealed to her where he hid his swill.
(We may buy her rum, but it makes us ill.)
"""

words = "".join(c for c in text.upper() if c.isalpha() or c in " \n").split()

result = []

# lhs
for i in range(1, len(words)):
    lhs = []
    sum_ = ""
    for j in reversed(range(i)):
        lhs.append(words[j])
        sum_ = add(sum_, words[j])
        if sum_ == words[i]:
            equation = "+".join(reversed(lhs)) + "=" + words[i]
            result.append((j, equation))

# rhs
for i in range(1, len(words)):
    rhs = []
    sum_ = ""
    for j in range(i + 1, len(words)):
        rhs.append(words[j])
        sum_ = add(sum_, words[j])
        if sum_ == words[i]:
            equation = words[i] + "=" + "+".join(rhs)
            result.append((i, equation))

result.sort()
key_string = ";".join(equation for _, equation in result).lower()


@decrypter.decrypter(chapter=55)
def decrypt(cipher: str) -> str:
    return sub89(cipher, key_string)
