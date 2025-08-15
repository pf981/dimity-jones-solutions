import decrypter


def swap_pairs(cipher: str):
    result = []
    for i in range(0, len(cipher), 2):
        if i + 1 < len(cipher):
            result.append(cipher[i + 1])
        result.append(cipher[i])
    return "".join(result)


text1 = """oS ,onhtni gey tniT eh esis eeen
,uB tosnoa  seginlaH ae tawmr shteew tiih,nA
n web-ro noWdoo  faviruo siLen shtre ergwo;sH
re eubsda  n,Aa dnt ehera B 
,eHers rpuosta V  ,na dhtre e a,TA
dna llt ehf olrusiihgnL teetsrs atdni  noRsw
.    --bAarah moClwye ,W"irttnei  nuJci efoL meom"n."""

text2 = """tSli,ls eeylP pare ,htuow li thtni
khTtaa llt ih simhg tsaw le lebw ir tniI kn
.hOn ;ot ehers's neesi  nhtsi ,na dyMtsreei
;hTuon wom iatsc ahgn eht yuAhtro sanem
,nA doth reH na dal yonlb elcia;mF
roa  shS eeRda,ss ehM kaset ehw rosdi  nhTee
.    --bAarah moClwye ,W"irttnei  nuJci efoL meom"n."""

print(swap_pairs(text1))
# So, nothing yet in Thee is seene,
# But soon as genial Heat warms thee within,
# A new-born Wood of various Lines there grows;
# Here buds an A, and there a B,
# Here sprouts a V, and there a T,
# And all the flourishing Letters stand in Rows.
#     --Abraham Cowley, "Written in Juice of Lemmon".
import collections

poem1 = swap_pairs(text1)
collections.Counter(poem1)
"".join(ch for ch in poem1 if ch.isupper())

for line in poem1.splitlines():
    lengths = []
    for word in line.split():
        word = "".join(c for c in word if c.isalpha())
        lengths.append(len(word))
    print(lengths)

# Number of capitals is non-decreasing per line. Could fit "Lines there grows"? Also "Letters stand in Rows"
# I still don't understand "For as She Reads, she Makes the words in Thee". There are no capital E's, so it's not as though I could make "THEE".
for line in poem1.splitlines():
    print("".join(c for c in line if c.isupper()))
# ST
# BH
# AWL
# HAB
# HVT
# ALR
# ACWJL

counts1 = collections.Counter(c for c in poem1 if c.isupper())
counts2 = collections.Counter(c for c in poem2 if c.isupper())
# FROM
# Mogh - there is no g

# Same here!
for line in poem2.splitlines():
    print("".join(c for c in line if c.isupper()))
# SP
# TI
# OM
# TA
# AH
# FSRMT
# ACWJL

# - Concatenate
#     STSP
#     BHTI
#    AWLOM
#    HABTA
#    HVTAH
#   ALRFSRMT
#  ACWJLACWJL


# - Invert second
# STACWJL
# BHFSRMT
#   AWLAH
#   HABTA
#   HVTOM
#   ALRTI
# ACWJLSP


for word in poem1.split():
    word = "".join(c for c in word if c.isalpha())
    if word and word[0].isupper():
        print(word)
for word in poem2.split():
    word = "".join(c for c in word if c.isalpha())
    if word and word[0].isupper():
        print(word)


for line in poem1.splitlines():
    print(len(line))
for line in poem1.splitlines():
    print(len(line.split()))

print(swap_pairs(text2))
# Still, seely Paper, thou wilt think
# That all this might as well be writ in Ink.
# Oh no; there's sense in this, and Mysterie;
# Thou now maist change thy Authors name,
# And to her Hand lay noble claim;
# For as She Reads, she Makes the words in Thee.
#     --Abraham Cowley, "Written in Juice of Lemmon".

# There are old-fashioned spellings and capitals
# So get capitals, column transposition cipher?
# "A new-born Wood" could refer to a tree like chapter 83:
# > Transpose the following ciphertext onto a tree that grows out of a single character, branching upwards to first left then right; then branching left from each of those new branches (and in order from left to right) before branching right from each (in order from left to right); and so on.

# So will the deciphered text start with "88. "?


# Also in this chapter were
# These are all the same length
["RETRIEVE WH", "ATE'ER YOU ", "LET THIS BY", "LTIPLIED.", "ELP UNHIDE:"]
# Well, I assume it's saying go back and look at all the torn pages. And then mutiply something?

# RETRIEVEWH
# ATE'ER YOU
# LET THIS BY
# HELP UNHIDE:
# MLTIPLIED

# # There is no "U"
# STBHAWLHABHVTALRACWJLSPTIOMTAAFSRTACWJL

# "Thee" must be significant
# 1. It is both capitalised and not meaning capitals are relevant
# 2. All three mentioned say "in": "in Thee", "thee within", "in Thee".

poem2 = swap_pairs(text2)
for line in poem2.splitlines():
    print(len(line.split()))


"".join(ch for ch in poem1 + poem2 if ch.isupper())

# STBHAWLHABHVTALRACWJLSPTIOMTAAHFSRMTACWJL
# There are no E's. There are a lot of A's though
collections.Counter("STBHAWLHABHVTALRACWJLSPTIOMTAAHFSRMTACWJL")
# HALF LAW WAR MAP STBHABHVTCJLSTIOTAHSRMTACWJL


# Also: wrath, jot, warmth
@decrypter.decrypter(chapter=87)
def decrypt(cipher: str) -> str:
    return pour(cipher)
