import decrypter
import itertools


def add(s1: str, s2: str) -> str:
    nums1, nums2 = [[ord(c) - ord("A") + 1 for c in s] for s in [s1, s2]]

    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1

    result = []
    for a, b in zip(nums1, itertools.cycle(nums2)):
        num = ((a + b - 1) % 26) + 1
        c = chr(num + ord("A") - 1)
        result.append(c)

    return "".join(result)


def sub(s1: str, s2: str) -> str:
    s2 = "".join(chr(((ord("Z") - ord(c) - 1) % 26) + ord("A")) for c in s2)
    return add(s1, s2)


text = """When my dearest rabbit Ivy awakes,
To my room her way for breakfast she makes.
Though I feed her grandly, Ivy has yet
To reveal herself a ravenous pet."""

words = "".join(c for c in text.upper() if c.isalpha() or c in " \n").split()

result = []
for i in range(len(words) - 1):
    sum_ = add(words[i], words[i + 1])
    if i and words[i - 1] == sum_:
        result.append(f"{words[i - 1]}={words[i]}+{words[i + 1]}")
    if i + 2 < len(words) and words[i + 2] == sum_:
        result.append(f"{words[i]}+{words[i + 1]}={words[i + 2]}")

    difference = sub(words[i], words[i + 1])
    if i and words[i - 1] == difference:
        result.append(f"{words[i - 1]}={words[i]}-{words[i + 1]}")
    if i + 2 < len(words) and words[i + 2] == difference:
        result.append(f"{words[i]}-{words[i + 1]}={words[i + 2]}")

key_string = ";".join(result).lower()


@decrypter.decrypter(chapter=54)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(cipher, key_string)
