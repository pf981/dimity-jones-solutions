import decrypter


text = """
Vku Szbiv Ntkxctfd-Exwxpuq Abyuf Wutjs Vku Lfrtgguq Htpoup Mlbvu
by Doctor Mildred Mogh

Zho lives alone
Is keard to groan.
Zko's alzays saq
Is never claq.

Zko kas no friunq
Eannot prutunq
Vkav vkuy possuss
Somu kajjinuss.

Zko yuapns fop lifu
Bs no onu's zbfu.
Zkosu lbiu's voo ealm
Bs fo ofu's mom.

Zko kas fo ekbwq
Kas suwqon snbwuq.
(A ioowbsk hpav
Uyeujvs fov vkav.)

Zkx's aww vxx snapv
Ofxzs jafcs av kuapv:
Ixp vkubp kbck abuz
Ibfqs exnptqus iuz.

Hlv sbfeu B'n zbsu
B'ww vtfvtwbgu
Tfq ektpn tfq mlbg
Tfq VPTJ t hxd
Xp sbs xi kbs
Zkx'ww hpbfc nu rxd.
"""

pairs = [
    "zw",
    "kh",
    "qd",
    "cg",
    "ue",
    "ec",
    "vt",
    "jp",
    "pr",
    "bi",
    "if",
    "fn",
    "wl",
    "nm",
    "hb",
    "yx",
    "xo",
    "ok",
    "av",
    "ta",
    "lu",
    "gz",
    "mq",
    "dy",
    "ss",
    "rj",
]
m = {}
pair_i = 0
for line in text.splitlines()[4:]:
    if line and pair_i < len(pairs):
        a, b = pairs[pair_i]
        pair_i += 1
        m[a] = b
        m[a.upper()] = b.upper()

    # print("".join(m.get(c, c) for c in line))


@decrypter.decrypter(chapter=40)
def decrypt(cipher: str) -> str:
    return "".join(m.get(c, c) for c in cipher)
