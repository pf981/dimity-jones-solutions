import decrypter


# dials = [
#     ["u", "l", "w", "i", "m"],
#     ["q", "g", "i", "k", "p"],
#     ["y", "k", "f", "z", "g"],
#     ["z", "v", "c", "d", "f"],
#     ["x", "b", "v", "j", "w"],
# ]

# Thoug|h
# 34215
# 12345
# uoThgtih  luwod e bsnatrgote  EKLI ydAr,s  Iusoppeis, nh cee s iocebjtleivy n airogna ,ntinoncsreida ,tewynhi,le sfsb-aoderb tabr.oF


@decrypter.decrypter(chapter=18)
def decrypt(cipher: str) -> str:
    return decrypter.sequence_shuffle(cipher, [3, 4, 2, 1, 5])
