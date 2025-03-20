import decrypter
import itertools


def chunk_shuffle(cipher: str, sequence: list[int], chunk_size: int | None = None):
    if chunk_size is None:
        chunk_size = max(sequence)

    result = []
    for buffer in itertools.batched(cipher, chunk_size):
        if len(buffer) < chunk_size:
            result.extend(buffer)
            break
        for i in sequence:
            result.append(buffer[i - 1])

    return "".join(result)


# lines = [
#     "Apples, bitten, cause delight.",
#     "Beaten dogs prove shabby sights.",
#     "Ballet dancers may wear tights.",
#     "Friends and family never fight.",
#     "For persons who're reshelving tomes, this order helps them find them homes.",
# ]

# for line in lines:
#     line = "".join(c.upper() for c in line if c.isalpha() or c == " ")
#     print(line.split())
#     # l = [i for i, _ in sorted(enumerate(line, 1), key=lambda pair: pair[1])]
#     # print(l)


@decrypter.decrypter(chapter=9)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(
        cipher,
        [4, 1, 2, 5, 3, 6, 12, 7, 11, 10],
    )


# Wel"l, [Fas"d iiDmtbS,yi"te hr'EI ses aamn }lunybesmr siBt aer heaeMIw rrd osi nnaenh ecsnes[cnt."
# e
# "iUohgR,"st adM.L iladen."-+uB  wutolnu t'devr eys)Ane enetc ua.tsjbeo  n,ZYt eo,tw he29,erfor u,egMct teaer?Ih2m  an e,ee(Syrvset necA7 entatsrswUyti  isht i]5srf wrtod |7ht,n teisswfce nd o,teI% nhtsti hr]y di..
# ."
# M$uya"e ebw'ex,s rppsuoe g*otdrer arn3
