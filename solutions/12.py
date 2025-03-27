import decrypter


# s = '??? ???? ??? ????? ????, ???????, ??????, ?????, ????, ??? ?????????? ?? ???? ???????? ??? ???? ?????? ???? ???????? ?? ???? ?? ???????????? ????????????? ???.'

# values = [128, 73, 120, 101, 1, 56, 18, 102, 37, 19, 91, 48, 127, 103, 38, 126, 74, 85, 14, 92, 20, 125, 21, 64, 104, 39, 33, 75, 121, 86, 105, 40, 106, 41, 49, 87, 15, 59, 2, 93, 107, 3, 65, 16, 34, 76, 122, 88, 108, 22, 23, 66, 109, 42, 77, 35, 110, 43, 50, 94, 95, 24, 67, 111, 25, 68, 12, 26, 4, 69, 17, 55, 123, 96, 112, 97, 84, 124, 51, 98, 44, 113, 45, 27, 62, 114, 78, 36, 28, 115, 46, 29, 89, 116, 79, 63, 5, 57, 30, 6, 70, 7, 60, 82, 47, 8, 11, 31, 117, 52, 13, 9, 61, 118, 90, 10, 71, 99, 83, 80, 100, 53, 119, 54, 81, 72, 58, 32, 129]

# result = []
# value_i = 0
# for c in s:
#     if c == '?':
#         value = values[value_i]
#         col = chr(ord('A') + ((value - 1) // 30) * 3 + 1)
#         row = ((value - 1) % 30) + 1
#         result.append(f'={col}{row}')
#         value_i += 1
#     else:
#         result.append(c)
# print('`' + ';'.join(result))

# # Put in Google Sheets
#
# # YOU TAKE THE SIXTH WORD, SEVENTH, FOURTH, THIRD, LAST, AND FOURTEENTH
# # OF THIS SENTENCE AND JUST SQUISH THEM TOGETHER TO MAKE AN ALPHABETICAL
# # TRANSPOSITION KEY


@decrypter.decrypter(chapter=12)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "SEVENTH FOURTH SIXTH THE KEY SENTENCE")
