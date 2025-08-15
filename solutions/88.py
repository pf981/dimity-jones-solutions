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
poem2 = swap_pairs(text2)

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

# Chapter 78 has more snippets!
# 'THAT BE MU'
# 'CAST ASIDE'
# 'WHAT O'ER'
# 'WROTE'LL' # 'WROTE' -- or 'WROTE'LL', actually, I think ..."

# Chapter 59
# "And the same thing," Dimity realized, "happened to all the other letters when they got singed in the dining room!" She pulled from her notebook and spelled aloud the other fragments: "CAST ASIDE;"; "WHAT O'ER I"; and " WROTE'LL H".


# RETRIEVE WH
# ATE'ER YOU
# CAST ASIDE;
# WHAT O'ER I
# WROTE'LL H
# ELP UNHIDE:
# LET THIS BY
# THAT BE MU
# LTIPLIED.

# "What over I wrote be multiplied" might mean line up the back and front pages and multiply where the numbers intersect letters or something?


# "LTIPLIED." is shorter. So maybe that is the last piece - which makes sense because it ends in period.


# # There is no "U"
# STBHAWLHABHVTALRACWJLSPTIOMTAAFSRTACWJL

# "Thee" must be significant
# 1. It is both capitalised and not meaning capitals are relevant
# 2. All three mentioned say "in": "in Thee", "thee within", "in Thee".

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
    return cipher


import re

chapters = []
for chapter in range(88):
    with open(f"data/{chapter:02}.chp") as f:
        chapters.append(f.read())

# page_regex = re.compile('"""\n' + ".{36}\n" * 24 + '"""', re.MULTILINE)
page_regex = re.compile('"""\n' + "(?:.{10,40}\n){10,50}" + '"""', re.MULTILINE)
# page_regex = re.compile('"""\n' + ".*\n" + '"""', re.MULTILINE)
# page_regex = re.compile('"""', re.MULTILINE)
# page_regex = re.compile('"', re.MULTILINE)
# page_regex = re.compile(r"\"\"\"\n" + ".*\n" * 24 + r"\"\"\"", re.MULTILINE)

# re.match(r'"""\n1', '"""\n1')

pages = []
for chapter, chapter_text in enumerate(chapters):
    if matches := re.findall(page_regex, chapter_text):
        print(f"--- Chapter {chapter} ---")
        for match in matches:
            print(match)


# """
# ;;B.'Ksy.H'!|Pzr'[5;|{swyrP.n.]Jq}uI
# B[F-zt7}9?}|Bz+q);r7Kms!ozrG1Cz.F[;z
# ,!A3(oC/:"v(Is-uG?9o$o[Bv9'":s+.?}Cq
# N}]C'?:BwOo(,E.]Cus:nG1,.A]Kq?*,qB;F
# ?\s;}GIs%uL:z,/|Bp'4s_A3(oC\s;'GI-):
# ;Bx9,xxUKqw}w;uw4C]x3:y";['BtPCxA8wn
# 9'L.G"(C,C;v;7z,Ac"lp|;v,]Jz*AHxq-/q
# !LKz;Prv;?J}Li7K"s]zBz.7v+AMwvsPvr:G
# :s/C'uwIs;zs|so\C\V_CzLy3'pC/-:rGE?L
# ;rnv9,!AB|]C\vn'/q":.N?sC/vrB}1'L;7"
# wq$xzRKx?%sB'z1,L9":xw\]BW'Es|9s:!C'
# LrH{9,|C,.wqp=;s!p;/sys%qkx:G1:C("Bn
# w?"'-yy+qr;:5+?'((rB[FCyqs|ssPwz?(F.
# /C;"(5z*A3(9?+s.B'Es$A]K"o/C:r:9,.q6
# n{5Cyq7(9.,,[$GJo*:XK:?PoBs(9s)ps+?u
# ![:M+wo\s;B.EC|'K[?w/s}B !-+A7=p; "u
# G.%C8#B'z1"LuL$9t|;BuwIC}q3zp;/vv?%q
# )P}{{GrDfzs|ssPs.q/qWLmE"z);rB'z5C+q
# B;z5C)qO.?C[s?'/q":mMK!v;C\p'Lz.AG.'
# qq[)E\9w}(v'w4C+.s{po:C'u.JC[z7#9O}r
# A3xz-\Cz[G8-|n3(o*1C(rGFtLoH+?';C.,}
# 9)-wpuGKv;:s,l-!s'B.JC"qI|9'--'B[8;[
# ,n:(1";"7"(|Pp":)Kw)ss).s}}BVG4?LzH|
# ;3z=p7K:v,"}B.EC?m5|]C\vv;GE?%qEKz,]
# """
