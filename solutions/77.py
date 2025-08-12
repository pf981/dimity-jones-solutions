import decrypter

"""A sobot, you are introduced to five
New friends, whose sort you seek to there derive.

You ask of Hal, "How many of you tell
Untruths?" He answers, "_____." You ponder. "Well,

"Of Hal and _____," you ask, "how many say
What's so?" Gal answers, "One." This claim you weigh.

"All four of these my friends," Hal volunteers,
"Speak _____." But no solution yet appears.

You therefore ask, "Is Val a fauxbot?" "Yes,"
Says _____. --And now you know! You need not guess!

You thank them: "That much testimony was
Enough to tell who doesn't and who does

Lie: Al's a _____; Gal's a _____; Hal's
A _____; Sal's a _____; lastly, Val's
A _____. Knowing you, I call you pals!"""

key = "TwoValtruthsHalfauxbotsobotfauxbotfauxbotsobot"


@decrypter.decrypter(chapter=77)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)
