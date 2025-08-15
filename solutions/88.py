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
    if chapter in [77, 78]:
        continue
    if matches := re.findall(page_regex, chapter_text):
        print(f"--- Chapter {chapter} ---")
        for match in matches:
            print(match)
[
    # --- Chapter 12 ---
    (
        r"""
z5C:.N}pC'w:rGNv;oAKos/":,+5rLmE"9v
/mLK:v;,Bw]J"L,N|:w}uB'z5C?uG:!v(,t
Kp(;;[Bv1]2:s%z;[|Bn)q),xEKl'Ptvy!9
}C,sG5(,!RKo?!-zr;KC|t7Kn;;o'rvRCqt
BF}w|sB=t,"'A{G?,.AM!pC!-z"!1";"7Ky
X[z7}9W}Cc"=Qz,A'w!"]sAB'L"/qB?sC("
A.9*ms''wICq.suz-%CU")2o)pa$9"-s:rG
|P",Bt5C?.N(oC|,Bn;PC[rs!p;Pq,z"L",
BnGNw-xswyrP"r;[1.,zM$9)-s.B)8sL-K:
SCfA5);z:C.,[qv,xIKm-\CsrwC|L-A:wsP
;s|sw/Cyr[Ks}AB}9,|"B''q.,AH{9t|;Bz
t,"s."'L'L-A.yC/vrB)1w.AM!l"Pw'B}1'
Cr.[I] A:(oC$o;._KC;;sw9z("'ywq"[.s
w4C+.sxp+PWsB.KC/mLKlC]s''wI|LuMK"o
x!3y:s%'B#aqt[!9.:C$vvpzq#4AM!p;;Cu
|t(;C?,[2?;x7{9t|;BnG3vxz9.]C/vrBwO
;"'r(SC+.H$9WPtry[SC/mLKq?%C\r{5;*.
-wIC(qMKl,:C(,]CrLz7=p;Pvn-wq"[AD(z
Cx'M!z;8,n:(1"[!s}l]/|B,xq":qszto%]
s{po:Cv' SC/qsw?s1C,sG3?=!L.]C?sv.y
z C?:'6s|:7}]C7WBq'E\+APwy"P",B[1z"
;{G),.q7z]C("Bv)q":qs|tu-".r)JC/uM!
9,|AcwyrPrrzsEr|#s::'Ptv.sCz*{s[z'\
x83t.+?:'sEq,AM!l"Pvn;GCs.AF.9"|Cp,
""",
        "TBLR",
    ),
    # --- Chapter 20 ---
    # This page (looked at from the "front") was torn at its top, bottom, and right edges; on its back, again, was a block of seemingly random characters:
    (
        r"""
;;B.'Ksy.H'!|Pzr'[5;|{swyrP.n.]Jq}uI
B[F-zt7}9?}|Bz+q);r7Kms!ozrG1Cz.F[;z
,!A3(oC/:"v(Is-uG?9o$o[Bv9'":s+.?}Cq
N}]C'?:BwOo(,E.]Cus:nG1,.A]Kq?*,qB;F
?\s;}GIs%uL:z,/|Bp'4s_A3(oC\s;'GI-):
;Bx9,xxUKqw}w;uw4C]x3:y";['BtPCxA8wn
9'L.G"(C,C;v;7z,Ac"lp|;v,]Jz*AHxq-/q
!LKz;Prv;?J}Li7K"s]zBz.7v+AMwvsPvr:G
:s/C'uwIs;zs|so\C\V_CzLy3'pC/-:rGE?L
;rnv9,!AB|]C\vn'/q":.N?sC/vrB}1'L;7"
wq$xzRKx?%sB'z1,L9":xw\]BW'Es|9s:!C'
LrH{9,|C,.wqp=;s!p;/sys%qkx:G1:C("Bn
w?"'-yy+qr;:5+?'((rB[FCyqs|ssPwz?(F.
/C;"(5z*A3(9?+s.B'Es$A]K"o/C:r:9,.q6
n{5Cyq7(9.,,[$GJo*:XK:?PoBs(9s)ps+?u
![:M+wo\s;B.EC|'K[?w/s}B !-+A7=p; "u
G.%C8#B'z1"LuL$9t|;BuwIC}q3zp;/vv?%q
)P}{{GrDfzs|ssPs.q/qWLmE"z);rB'z5C+q
B;z5C)qO.?C[s?'/q":mMK!v;C\p'Lz.AG.'
qq[)E\9w}(v'w4C+.s{po:C'u.JC[z7#9O}r
A3xz-\Cz[G8-|n3(o*1C(rGFtLoH+?';C.,}
9)-wpuGKv;:s,l-!s'B.JC"qI|9'--'B[8;[
,n:(1";"7"(|Pp":)Kw)ss).s}}BVG4?LzH|
;3z=p7K:v,"}B.EC?m5|]C\vv;GE?%qEKz,]
""",
        "TBL",
    ),
    # --- Chapter 31 ---
    # The page was carefully torn along the left and bottom edges; on the back was written the usual seeming gibberish:
    (
        r"""
CePC/u8.]C7co.sB)x/UK:v;Cn"[8?}AH,9"
":qs"l'\C'u.EuL:A.9)%?'rGZ#L;Aw:C:w;
spp;,CX..7v+!Hwo\/CqrxKC,pB|z;/vv?GZ
C$?:x)RCf;s:!C,z;,/qo|AM!pC|,y[GE?%q
".xCo+;7{t,"Cn?"5o}mGypC(,Bv[SC()s,l
5C*.NKl;;C:rs4w)ss|sw/CorxF;,AAw'w}u
'I:o|PQny!F-|{sb?-/":n[9,!{sZp!%s;;.
9!;,"y[9.x;7Knw+vr:[5[+{se9)(zy}G1"L
rBv;qw+:s)?w"w.n!SC,z5:.v;;rqG6?}ysw
u5'|mK\]C?]B'z5C,(M{l,;?";G3vx!3y:s%
;,A.?'P#*B;1.,xR$9"-sBs'L;+tswyrP'v)
+?';|Bq.Mw.qsx(CZN}B[8sLx7(r"-C,sGF-
/"yrFq)x:s"pt\C".x9,;:A.o|Po.qGGs}t3
:wSC[zs!p;Pvn:vqr;:D$9o$ov'.EuL.G"(C
z,AF)?sP"un;q":mMKztPo.B'3qx:B)yo]Cp
B?s"%?nq/q"[.UKt'Pooywq"[A3|:s/"$BsE
C[w.q!PCy!B(rC\vrzGK?LyRKl"\s.'.F,Lm
BzsEo!q6K:?P):r)KC?!H-9"-sB.'qr['4|9
8sL,H.xC$;v'[5,LuGKws{?.B,Lwzqs)yC\v
)s"l'\C**GG?,yW5[DQa[Bw4w+.K:lzPw.'(
nw/w,.GNo|AP!p"-s:B'IC).MK:?Pw.p!Lr,
s;;wE";mEKz;Ps-r;q,x;N{lzP!n:[q??AM!
[8sL:3-pC\wzr/qo)ps:yC\vrB)1.,A7(:w!
""",
        "RB",
    ),
    # --- Chapter 59 ---
    # But the professor, who had flipped over the letter, which he'd found uninteresting, now stared with scholarly tenacity at the peculiar hieroglyphic penned on the other side, which he found very interesting indeed:
    # I don't think it specified which edges...
    (
        r"""
Nzos}z[Bx9(,AR.l;/Cnt'RCqtB}9w/C.,[q
'"w-v;7'K{s[;p]w;uw4C-mL|9];o:B]Er,!
:,s3vxnE.]C,,qB"5;|.GwwC|tBuwIC(mC)?
Lu:AB(9o}Cns[5;).H(]C,,qBv5']uM.9. C
"7{(C/s.;wq??AM!l"P"r::RCfrsx(C!vn.u
pq|,;'(Lq+q6$9"-sB\d5"+qKKe?Pm,"(qg+
C.,}RC5MGz9w'C[,]X;,AL|;.+sqBtPC+t3|
|Gz;oB||Cz?"B:L'+AMwvsP"uv)qo?;7{"?%
+uF.]C,,qB!F?]q6Kl'P.n.+q";y7}9o/C.r
(rC/?zrGFtL;A.9s,;y[GK;xzL[z'("v,;qq
P"urGIs|'E|9w/Cuvy8s}AM!l,PML}GFtLoH
$Hrh:.N?sCORvz.K]LVH(p'PW.BhL{#x7KNo
s2:szpo\v}B.K'LqE.xs}";B}5;,A3"wC\vr
M)9"-w;B[5[+AAw!C\vr:w6?}qsxps}Cyv[K
C/!ry!5;LmGz9';zs*"I?[rK.lr;;}BsJChz
B['LC?uGz9o}]B'+G?|AH{9p*u;}GP?=AFw(
Z#LoH(:;|zB,{5;L-A:nvPWBusMsLmMKwo/"
yL.w(;'Bz+q);r71!C;''n[5}6A%!]C,,qB[
9w/Czv;5|L;H)9${]Bs.I'+Ab39o}rB;]Is-
;nvy8"?.K%l;:}Bgz5C[zE\9r(tsvuLz+A6.
G+,L;A.9?}sBusEr_AB|9q|,;'.K-+qLKy?P
Lt3(o|Pw'B}1'L.4=t?*'y[G3?(,H}prPo'B
{(}PW.qw5r_AB|9q,,.,[qp,ALwtrP",BwOw
""",
        "?",
    ),
    # --- Chapter 61 ---
    # The sheet was torn at the top and left; on the back was penned the usual rigmarole (which Professor Dunckan professed to find fascinatingly suggestive):
    (
        r"""
]Bs.Er|AB|!C%sn;'EC?.KKms(,tB.EC+t3|
GK?(ns:yC$vvpzq.*AP:qsPw.'wEr,ps(z"P
*.G.9t|;B(zF.L:A.9)%?'rG5(,!R|sw}u}B
{t(;rB,xq":uLKwo/"B''Lq:uG?]C,,t".Jv
/CVB(L,L.N|9?'C:,'DC[zs|sw/C?ny5=6{s
B[8w|]sWq";;Bs.MsL)7w?'P?sB[1z"AM!p;
o}y7z9o}rBz.Jz,psx(C{]B(.6s_A]Kso#sB
H|sC$s:r%qO))s)ysP?sB[8sLp7[?s/'v,;q
"(s;B[FC["7{"?%y}BsCq[tH"t'{|BpsG";.
B'z9,"AB|9w{!,:[1,+AM)9v,,tBsqzxn7"9
1q:AH|ss%}Bjwqu}qPK:?Pw.p'D!x;3xtz("
;HK;,:s:;[1,.{sw!C\vrB {s+;7{%C+;,-w
l(;Cs,]Er_AM)rs\vr:/q":qs}:;;,t'zq"[
;Bow9,!AL)9q|.z,;Gzxo7$9),'B'z1"Lz7:
;5'|{s%pC/wzzwIs.{s};t's:rvSCxz6K!!,
=!I{t';C(uwEC?uK}:CjC:rs4C;;TKM-\C'u
)z|PWB;!F)-)s{po]w]rvSC:m6Kq?%C[rsI'
-sB?]2z;oszz.,w.}G1'LyRK"w'sBv;Ks)p7
q/qr,:I::sP"urGE?LpH+m"P)ry!Z.,mG:yu
.,A8)?C,Cp,:G;,t7(!w#sB,;Cw)qs=l;(?:
M:'sP'puw4--qsyl,PprBxF-)psw:C|p.n?N
|PzvtzK,;z93!)(t'ByFo-w7..s%|BpsI;;q
v.yqw)AH{os%C',G2sLm4"pC\?Br;A?*A3(o
""",
        "TR",
    ),
    # --- Chapter 66 ---
    # The sheet of paper was torn at the top and right sides. On the back was the usual block of seeming gibberish --
    (
        r"""
+qLKlC#o;'/qw);K:no\sy[G2?[nR|?o+!rq
:rv\s,")SC.!N(vs}Cwr(5.;m6#9h-sBr{5;
-?"yvq,[;UKn?*zqB;F"_A]Kqs]"}Bt5C.qI
?!1q,{swyrP"ur(5C;:s(z"P"urGJ!xo7K\o
s);LKztP"un[qz,;M.?}PWB(.CzL:3\9?}z[
A)9,;(r:GB,,-swyrP',BuF--ps(z"PprBu8
v;;B,xq-|APw!C:s?:wJ',pUK"sP'":wC]Ln
-r)q)['Ez9q;;'n.Ez*A8:yrPvr:GCwxnB"t
7z*A6:lu}?;'.3}LTH%p(;;}Baq,[AE)yu;;
qK.9'(.?y+q-)t3[.]1Cn.vqp,o3+!sP?sBw
9w}C'uwqzx:MK:)|C[rsI'L.8Kss%Cyvx5|L
.nv!5rLy7KlC!??[%qd,!Aw.'P)rB:9u:;s!
(q.x!K:prPzvswSC).s"p'/C':sL.x;By9t|
|'K=t(;Cny'Es$A#)]C!;"r!qw)AH+?C[w.q
:yC\vn'GCs+;7{9q;;'n.Ez*A5wxsPo;Bsq'
;Cn;GE?L:N{.;('rBsKCxxE#9P;qn")5CfAM
v)q",(MKt'Pprv;7C?!7.w]Pr,.sKs.AM)9"
;,:M.oC\?Bx;F)L;Aw:Cus:nG1,.A]Kt,\s.
6KQo},v''DoLmGz9?\vr:)SC+.szzC\vrB)1
s;,B.'Ms-:TKQ-]zBqwKo;xLKl,:CnB[5,+m
n'G5w!tM.p,PoBow1-+u8+w|P,,,vCs4x3(v
qWLyR}pz'Cqvvqvx"7K:?Pzrn(EC|.F.9q|r
zDK(?*|BPzIw|;B(p}PO.qG7?[p4\p}QDCCH
""",
        "TL",
    ),
    # --- Chapter 74 ---
    # The paper, neatly torn across its top, bottom, and left sides, had on its back side the following block of gibberish in ink --
    (
        r"""
|;s);"/wqrG9"|A7(nw+vr::5,++sWq";;B'
|!C,z,.yq);;AK:v;Czn)Jw%qs(z(;zB;z5C
/w-rG1;ztB=t'\|Br:1w-uG?9v;;;r!6C:qK
v)B'L.8Kmo!y"?)q??A7=p; Cz,v9t;o3|t?
C-qL}9"-o.BFJs%qGKs-}r:rvpC.!3,:'P?s
s,z;Px";[q":qs"l'\Cq:s6"L.8K8R(.v'+q
"|;B,xq":!7.9"-?";sEr$A:(oC s'}GFtL;
n'w4_L"7{!w|,}BsErL.G"(C\v:rwqq[,B.!
1"Lt7{9)|;q}GDw!tMKlz{?;'GKo"qs::C,'
.G.9s#s:B(5o.:s|sw/}\BHrb,"7{:v;zr;)
ww}uB'z5C+!N|sC$vr.GJv,A3zxw\"rqGKvx
?:B'L;L:H(]Cb;q[1SC|t7K"o/Cor.EuLpB}
GCw+;E.9"|?Br|G?|uM)?]P",Bt5CxA6:l; 
];NKp.|"v,;1zL:5{ps:C'usKC;;s[?s\s.q
KztP',zwKv;z9Kz,;C,sG8s}AG)'s]w;'G3v
(,tBz5;L;HK";("rBsq,;o7Kww\"yrGC-z!3
v;7CfAP{t";Cv;G6?}A7=p; ?.r*YCqtB}9z
T[!s|ssP),:!4}LRH{9s#s:['EsL:A.=rP,r
Q|9w\'ryxq"[A6.nw:sBs'IC(qTKhv;,B'z5
s%C;usBsL;A.9t;o:B[8o+AL)xs|,rB:9u:;
B(z5,L;HK:v,"Bq.1;*AL!pC+o:n!9!+u5ww
qs\,7y:C,,qBsNo;;s,;;\vr:G4w|oE)!-%s
'9!9"-sB:wJ"L.8K:v;C;''I]L;Aw:C;[?ys
9"-w.xG9"LuLKl, Cxv;4C[rs[p;#s:;wq',
""",
        "TBR",
    ),
    # --- Chapter 87 ---
    # She looked at them all again, poring particularly over the what she'd supposed was gibberish that was penned on what she'd supposed was their backs. But ponder as she might, she still could make no sense of, for example, this, on the back of the letter that began with "Sweetheartkin", which Leland had found in the library:
    # Maybe need to check that chapter
    (
        r"""
9z;"'r(q#4AM!l"P"urG6?}y7{9q|,;'.K-
",BtL;*A4+:C\?B?(5',!O.9"-o'B)1r_AK
[8sL:M{l,"s:;G6?}AP!z.P'urGCw%q6$9'
,psyz.{-.vu1";.G#ADuvv;G9'LzH|9"-sB
|zC!vny!5,!qs)?C!?.'(1r;oMK:v;Cp,;K
,![B}9":A3K"?}rr:xLzL,L\nv|z,t.J"L-
p'DsL;HK:v;Cp,;3z=:B)yC\vn'/qw?A7::
*(mG+lz/*B'z1"L:A.9y;!'B'EC:qKK!v;z
N}ys/'}BsErLu6:z!,"uvuq!xuG}9";zyv;
?}C,"(qq[z6::w|,{BeF'+AE:vs]]}B}5C/
[}G1'L:A.]C,"Byw1'+{s%l'Pprt.E,;z9$
J}LUs)yz C(v)8C|t7Kso:|BnxKs}A3"w|P
A4{po[Cn?sI"$A;+:C\vrB[Io!q6\9?'C,"
:v;;B,xq-|AM!z-"v'B[8sL.M!p;Pq,"!4C
"'rvRCqt7Kl,"-v;z5rL:5)?,P;r-w1z,ps
wECxs3:y|P?.B[8sL.M!p;Pvn.vSC;;syl.
Ln7.yC'sry.EuLqQwn"]]B'z5C|mF.[DQhu
z[Ces-,[5s|AH,9v;;B('IyLy3\9p;Cv.[5
P.npz9,x;B)y'P?sB!9",!3{(C,ur.[qP}m
":qs.uM:z,P?sB:PC/u8.='Ptv:)KC+tB{:
o$.3\3v{r"nv7]$AtLev|-tuG?;.)UKy?$C
LKz,Pw.BtCw+t7Kn?{!"'wIC;xE::s%op[/
C\?Bo(9,!AM)9z(uu'GKv;:s|p[\}BCH*vx
""",
        "???",
    ),
    (
        r"""
-w;BwCsz;K)yw!Cr;u1!,AG)'s]|Bq.5rL:
'.Eq+uH(9p;z,.yJC+.s|ssP,,-wCzxArit
#LnN|9w\Cv;GKv,AF)!"P-.")Lo-{s+yo+!
EKztPvr:)q":mMKTC!o..'KCy!7.)sP"u:'
(|;v'wRDMfA:!C('Bn;qo?;7{"?%r}B.EC,
Bqw3w]t7{pr1Cn.vq":qGKwo??:v'L'-)s{
EuLP7[?s/'rqG(-|n3(o*1C?yw1',A6)9'|
;A.9;('xB'6C|,H:ww}uB['L;LrN(]C?sBr
yrP."y[9!-)s::|P?.rG3vx!3y:s%Cn'G1C
'B['LC3o3}:C,'vqwYC/t7(9-};rn(Io)sB
[8C+tK);u-C.v;KvLoB[ss%"r)[J}LiA.?s
}A3".v,pr'/qo)ps|ly;C'uwq;,y3:yr;;{
[!C,pn.vF,,pUKl"P"urGKw(qs)qC{]B(.6
,Csv;1zLoH-.w]w.t%qa*A5)y"%wo"[9?)A
,"Ps.uM)?C9.[B}9t,APw!C,Czr[9q=xH+!
rL,Ew(";''r(RC5aGK:v,"B.'Ks_AL!z-]r
MK:v;C,o;1y/mcw:_/]z"|R?x)swor%s;;G
);zy*:5o)uG?9p*'[o'4w,:sylz]w.tGKv,
rB'Kv,!s}tr;C,sGKv;:s}ss;"B,xq!x,7{
L';.G}9v,(rBt5s)A8."|P.v.'I|LmGz9'\
AM!l"P.nq/q.x'Gzp;(,tB!5"+qKK:?P.r{
pCq-]]!5CZmL|wsP'',(P}LaGK:v;C,'z5;
w.t!PC[n8+!q,",:+q.[p7$9o/C'usKC|;H
""",
        "",
    ),
]
