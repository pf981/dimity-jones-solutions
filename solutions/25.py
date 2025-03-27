import decrypter


@decrypter.decrypter(chapter=25)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(
        cipher, "All who enter a citadel such as this'll be here always."
    )


# hint = " .'tsfreelt isrtwl idte d'nsarhe-ttihrgwi rd esdenmaiht-etmfoesl  tdunba  ,,etshagci re hstt lsiyta wglnai ttiornw dsn'athI"
# hint = hint[::-1]
# print("".join(hint[0::2]) + "".join(hint[1::2]))

# Maxine and Molly were playing a game of tic-tac-toe.

# Maxine, who was right-handed, played first, and placed her X in the left-center square.

# Molly, left-handed, had the idea that the center-center square would be the best place to put her O.

# Maxine, hoping to start building a line on the left side, then placed her second X in the left-bottom square.

# From this point onward, each player was forced to put their mark in the square that would prevent their opponent from winning.

# After seven of the nine squares had been filled, they agreed to call it a draw.

# L4 R7 ??
# R1 L2 ??
# R3 L6 R5

# A L l _ W H O
# E N t E r # A
# C I T a d E L
# S U c H _ A S
# T H I s ' l l
# B E _ H e R e
# A l w a y s .

# -- Original  --
# e a l w r h o
# c N _ E d # a
# t c w l t e l
# i U i H a A s
# s h _ l _ l e
# t E a H s R .
# b a l y ' e s


# c a l w d h o
# e N t E r # a
# t c w l _ s l
# i U i H a A s
# s h a l _ l s
# b E _ H e R e
# t a l y ' e .

# all who
# enter a
# witches
#
# caution


# a l l _ w h o
# e N t E r # a
# w i t c h ' s
# s U c H _ A s
# i d a l a l s
# b E _ H e R e
# t a l y e l .

# sUcH_As
# bUsH_At
# ?U?H?A?
