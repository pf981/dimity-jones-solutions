import decrypter
import itertools

line = """z5C:.N}pC'w:rGNv;oAKos/":,+5rLmE"9v"""

len(line)
# So maybe 35 is the width


@decrypter.decrypter(chapter=13)
def decrypt(cipher: str) -> str:
    return cipher


import collections
# import nltk

# # nltk.download('words')
# all_words = nltk.corpus.words
# for word in {word.lower() for word in all_words.words()}
with open("./data/words.dat") as f:
    all_words = f.read().splitlines()
# all_words.extend(["dimity", "leland"])

for i in range(13):
    with open(f"./data/{i:02}.chp") as f:
        chapter_text = f.read()
    chapter_words = {
        "".join(c.lower() for c in word if c.isalpha()) for word in chapter_text.split()
    }
    all_words.extend(chapter_words)


counters = [
    (word, collections.Counter(word)) for word in {word.lower() for word in all_words}
]

cipher = decrypt.decrypt_chapter()
text = cipher[: 35 * 100].replace("\n", "#")

for line in itertools.batched(text, 35):
    line = "".join(line)
    counts = collections.Counter(line.lower())
    words = [word for word, counter in counters if counter <= counts]
    # print(line, words[:50])
    print(line)
    print(sorted(set(words)))
    print()

# import random


# def shuffle(seed=None):
#     if seed is not None:
#         random.seed(seed)
#     order = list(range(35))
#     print("\n\n")
#     print(order)
#     print()
#     random.shuffle(order)
#     for part in itertools.batched(text, 35):
#         # print("".join(part[i] for i in order))
#         print(";".join(part[i].replace('"', "*") for i in order))


# shuffle()
