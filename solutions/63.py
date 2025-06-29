import decrypter

key = """It enters, when I need it, late,
This evanescent, sick surmise:
If I've, for those with reason, made
A verse to wonder at, surprised ...?"""


@decrypter.decrypter(chapter=63)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)


# import decrypter
# from decrypter import vigenere_breaker

# reference_text = []
# for chapter in range(63):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)

# ciphertext = decrypter.decrypter(63)(lambda x: x).decrypt_one_chapter()

# result = vigenere_breaker.break_vigenere_cipher(
#     ciphertext[:1000],
#     reference_text,
#     decrypter_func=decrypter.vigenere_cipher,
#     key_chars=vigenere_breaker.ALPHABET,
#     max_key_length=160,
#     verbose=True,
# )

# result = vigenere_breaker.try_multiple_key_lengths(
#     ciphertext,
#     reference_text,
#     decrypter_func=decrypter.vigenere_cipher,
#     min_length=120,
#     max_length=160,
#     key_chars=vigenere_breaker.ALPHABET,
#     verbose=True,
# )


# text = """BF|EGFEDE,|BAEG|B|GEED|BF,|EAFE,
# FABE|EAAGEECEGF,|EBCD|EGDFBEE:
# BF|B'AE,|FAD|FAAEE|BBFA|DEAEAG,|FADE
# A|AEDEE|FA|BAGDED|AF,|EGDBDBEED|...?"""


# import itertools

# dec = decrypter.decrypter(chapter=63)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:5000]

# key = """It|enters,|when|I|need|it,|late,
# This|evanescent,|sick|surmise:
# If|I've,|for|those|with|reason,|made
# A|verse|to|wonder|at,|surprised|...?"""
# key = key.replace("|", " ")
# plain = decrypter.vigenere_cipher(ciphertext, key)

# print(plain)
# print(plain[:-550])

# for a, b in zip(plain[:-550], itertools.cycle(key)):
#     print(a, b)

# alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
# have, want, key = r")wE"
# alphabet[
#     (alphabet.index(have) - (alphabet.index(want) - alphabet.index(key)))
#     % len(alphabet)
# ]


# import collections
# import random
# import re


# def to_notes(s: str) -> str:
#     return "".join(chr((ord(c) - ord("A")) % 7 + ord("A")) for c in s.upper())


# def to_letters(note: str) -> str:
#     result = []
#     i = ord(note)
#     while i <= ord("Z"):
#         result.append(chr(i))
#         i += 7
#     return result


# def get_candidates(notes: str, n_candidates: int) -> list[str]:
#     result = []
#     letters_list = [to_letters(note) for note in notes]
#     for _ in range(n_candidates):
#         candidate = [random.choice(letters) for letters in letters_list]
#         result.append("".join(candidate))
#     return result


# ref_words = re.sub(r"[^a-z ]", "", reference_text.lower()).split()
# ref_counts = collections.Counter(ref_words)
# m = collections.defaultdict(list)
# for word, count in ref_counts.items():
#     m[to_notes(word)].append((count, word))

# for notes in m:
#     m[notes].sort(reverse=True)


# notes_list = re.sub(r"[^A-G|]", "", text).split("|")

# for notes in notes_list:
#     if not notes:
#         continue
#     candidates = m[notes][:5]
#     print(notes, "->", ", ".join(word for _, word in candidates))

# text = """BF|EGFEDE,|BAEG|B|GEED|BF,|EAFE,
# FABE|EAAGEECEGF,|EBCD|EGDFBEE:
# BF|B'AE,|FAD|FAAEE|BBFA|DEAEAG,|FADE
# A|AEDEE|FA|BAGDED|AF,|EGDBDBEED|...?"""


# notes = 'EGFEDE'
# notes = 'BAEG'
# notes = 'FABE' # THIS
# notes = 'EGDFBEE' # SURMIZE / SURMISE
# notes = 'EAFE'
# notes = "EAAGEECEGF"  # EAAGEEcent
# [to_letters(note) for note in notes]
# get_candidates(notes, 20)
# [['E', 'L', 'S', 'Z'],
#  ['G', 'N', 'U'],
#  ['F', 'M', 'T'],
#  ['E', 'L', 'S', 'Z'],
#  ['D', 'K', 'R', 'Y'],
#  ['E', 'L', 'S', 'Z']]
# ... ENTERS
...

# BF -> it, if, im, wf, pm                                 If
# EGFEDE, ->                                               enters
# BAEG ->                                                  when
# B -> i, b, p, w                                          I
# GEED -> need, used                                       need
# BF, -> it, if, im, wf, pm                                it,
# EAFE, -> some, same, safe, late, lots                    some
# FABE -> this, fail, tops, tail, maws, maps               this
# EAAGEECEGF, ->                                           ,
# EBCD -> lick, sick                                       sick
# EGDFBEE:                                                 SURMIZE / SURMISE:
# BF -> it, if, im, wf, pm
# B'AE -> was, ive, woe, pal                               I've
# FAD -> for, may, far, thy, mad                           for
# FAAEE -> those, moves, tools, fools, faves               those
# BBFA -> with, bifa                                       with
# DEAEAG, -> reason                                        reason,
# FADE -> more, make, take, made, tore, fake, toys, fade   more
# A ->                                                     a
# AEDEE -> verse, heres                                    verse
# FA -> to, fo, ta, ma, mh                                 to
# BAGDED -> wonder, poured                                 ponder
# AF, -> of, at, am, ot                                    of
# EGDBDBEED ->                                             EGDBDBEed

# BF -> pm, wf, im, if, it
# EGFEDE, ->
# BAEG -> when
# B -> w, p, b, i
# GEED -> used, need
# BF, -> pm, wf, im, if, it
# EAFEFABE ->
# EAAGEECEGF, ->
# EBCD -> lick
# EGDFBEE: ->
# BF ->
# B'AE -> pal, woe, ive, was                   I've
# FAD -> fad, tad, toy, mad, thy
# FAAEE -> faves, fools, tools, moves, those
# BBFA -> bifa, with
# DEAEAG -> reason
# FADEA -> torso
# AEDEE -> heres, verse
# FA -> th, mh, ma, ta, fo
# BAGDED -> poured, wonder
# AF -> ot, am, at, of
# EGDBDBEED ->
