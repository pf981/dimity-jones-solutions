import decrypter

text = """The Logic Teacher's Lament

Four ["Yes!"] students -- differently rude,
Loud, slack, and dumb -- my peace preclude. ["Lovely!"]

The rudest's louder than the slackest;
The slackest's dumber than ["Oh divine!"] the rudest;
The second slackest's ruder than the second loudest.
Of logic teachers, I'm the beatenest and bowedest.

The loudest's ["Keep going!"] slacker than the dumbest;
The dumbest's ruder than the loudest;
The second dumbest's louder than the second slackest.
Of logic teachers' dispositions, ["Thank you!"] mine is blackest.

The second rudest's not the dumbest.
Of logic ["You angels!"] teachers, I'm the glummest.
"""

# r1.l < s1.l
# s1.d < r1.d
# s2.r < l2.r
# l1.s < d1.s
# d1.r < l1.r
# s2 != d1

# 3 2 4
# 4 1 3
# 2 4 1
# 1 3 2


@decrypter.decrypter(chapter=66)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(
        cipher,
        "ThirdSecondFourthFourthFirstThirdSecondFourthFirstFirstThirdSecond",
    )
