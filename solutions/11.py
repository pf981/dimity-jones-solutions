import decrypter


# s = 'The ?????? ?????? is a book that you at ????? ???? must ????.'
# values = [35, 15, 8, 29, 41, 47, 48, 20, 9, 7, 1, 32, 36, 21, 10, 17, 33, 2, 6, 24, 25, 18, 37, 16, 3, 38, 45, 26, 42, 4, 39, 11, 44, 12, 31, 46, 30, 5, 14, 13, 23, 43, 34, 40, 22, 27, 28, 19]
# s2 = [c.upper() if c != '?' else next(it) for c in s]
# print(''.join(s2))

# it = (chr(ord('a') + i) for i in itertools.count())
# chars = [c if c != '?' else next(it) for c in s2 if c.isalpha()]
# sorted(zip(values, chars))

# # THE abcdef ghijkl IS A BOOK THAT YOU AT mnopq rstu MUST vwxy.
# # THE PUZZLE CASTLE IS A BOOK THAT YOU AT EVERY PAGE MUST LOOK.


@decrypter.decrypter(chapter=11)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "PUZZLE CASTLE EVERY PAGE LOOK")
