import decrypter


def reverse_words(sentence: list[str]) -> str:
    word: list[str] = []
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


@decrypter.decrypter(chapter=2)
def decrypt(cipher: str) -> str:
    sentence: list[str] = []
    result = []
    for c in cipher:
        if c == ".":
            result.append(reverse_words(sentence))
            result.append(".")
            sentence.clear()
        else:
            sentence.append(c)
    result.append(reverse_words(sentence))

    return "".join(result)
