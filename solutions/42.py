import decrypter


text = """
Who lives alone
Is heard to groan.
Who's always sad
Is never glad.

Who has no friend
Cannot pretend
That they possess
Some happiness.

Who yearns for life
Is no one's wife.
Whose life's too calm
Is no one's mom.

Who has no child
Has seldom smiled.
(A foolish brat
Excepts not that.)

Who's all too smart
Knows pangs at heart:
For their high view
Finds comrades few.

But since I'm wise
I'll tantalize
And charm and quiz
And TRAP a boy
Or sis of his
Who'll bring me joy.
"""


@decrypter.decrypter(chapter=42)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(cipher, text[1:-1])
