with open("./data/01.txt") as f:
    text = f.read().split("#####", 1)[1]

# text = """liability of Limitation.risk own my at amusement the enter puzzler"), "the as to referred (hereinafter client the I,
# .puzzler the me, befall should that mental, or physical injuries, or damages, loss, any for responsibility no assume amusement the of operators and management The .puzzles and blackmail, emotional deception, lights, strobing and/or bright distortions, perceptual challenges, cognitive obstacles, to exposed be may I amusement, the of course the in that acknowledge puzzler, the I, .liability all from amusement the of operators and management the exempt hereby sentence, next the aloud saying by puzzler, the I, .contract verbal this of terms the to agree solemnly and understand hereby "I
# .time! fun a puzzler, the me, wish amusement the of operators and management the Finally,   "
# """


def reverse_words(sentence):
    word = []
    result = []
    for c in reversed(sentence):
        if c == " ":
            result.append("".join(reversed(word)))
            result.append(c)
            word.clear()
        else:
            word.append(c)
    result.append("".join(reversed(word)))

    return "".join(result)


def decrypt(text):
    sentence = []
    result = []
    for c in text:
        if c == ".":
            result.append(reverse_words(sentence))
            result.append(".")
            sentence.clear()
        else:
            sentence.append(c)
    result.append(reverse_words(sentence))

    return "".join(result)


with open("./data/02.txt", "w") as f:
    f.write(decrypt(text))
