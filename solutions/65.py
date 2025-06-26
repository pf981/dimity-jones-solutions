import decrypter


# key = "gtmgtngMng|ngW_hq(gt0vtnjtngrvut*gtwgtngtneynan-ggngtk,HntJnvtnc*nrlmgtncongtlWtngtngGvdun%tngMIgnmgung8nga[gtngtngynftngtnitngNngv5#tngt gDGgEnggngF2ge2gtnvxn2tnxtnjtnc,ngt;gtngtkgwmctngtngtugrngtnu8nQvwgtngtrGMn"

# # 1001
# for i in range(2, 1001):
#     if 1001 % i == 0:
#         print(i)
# # 7
# # 11
# # 13
# # 77
# # 91
# # 143
# # key = key[:7] # Okay
# # key = key[:11]  # Eh
# # key = key[:13]  # okay
# # key = key[:77]  # Eh
# # key = key[:91]  # okay
# key = key[:143]  # good?

key = "gtngtngMng|ngW_hq(gt0vtnjtngrvut*gtwgtngtneynan-ggngtk,HntJnvtnc*nrlmgtncongtlWtngtngGvdun%tngMIgnmgung8nga[gtngtngynftngtnitngNngv5#tngt gDGgE"


@decrypter.decrypter(chapter=65)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, key)


# import itertools

# dec = decrypter.decrypter(chapter=65)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:5000]

# key = "gtngtngMng|ngW_hq(gt0vtnjtngrvut*gtwgtngtneynan-ggngtk,HntJnvtnc*nrlmgtncongtlWtngtngGvdun%tngMIgnmgung8nga[gtngtngynftngtnitngNngv5#tngt gDGgE"
# plain = decrypter.vigenere_cipher(ciphertext, key)

# # print(plain)
# print(plain[:100])

# for a, b in zip(plain[:100], itertools.cycle(key)):
#     print(a, b)

# alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
# have, want, key = r"FLg"
# alphabet[
#     (alphabet.index(have) - (alphabet.index(want) - alphabet.index(key)))
#     % len(alphabet)
# ]

# ...

# result[0]

# import decrypter
# from decrypter import vigenere_breaker

# reference_text = []
# for chapter in range(65):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)

# ciphertext = decrypter.decrypter(65)(lambda x: x).decrypt_one_chapter()

# result = vigenere_breaker.break_vigenere_cipher(
#     ciphertext[:10000],
#     reference_text,
#     decrypter_func=decrypter.vigenere_cipher,
#     key_chars=vigenere_breaker.ALPHABET,
#     max_key_length=300,
#     verbose=True,
# )

# hint = """18/556 + 22/391 + 3/221, 4/6239577959 + 13/313 + 8/581, 18/912 + 2/848 + 17/254 + 19/485 + 15/611 + 23/271, 4/2270709097 + 13/809 + 4/1803027605 + 20/363 !"""

# text = """EXAM
# (Or: 3/1 + 9/86 + 11/101 + 4/2000000)

# 21/458 + 1/14, 1/591 + 15/645 + 6/487 + 9/504, 21/521 + 22/575, 1/460 + 6/41 + 7/813 + 17/213, 2/679 + 16/861, 18/415 + 6/842 + 4/472 + 4/526 + 9/219, 2/444 + 1/408, 5/802 + 16/403 + 9/956 + 2/786 + 9/685
# 15/299 + 22/836, 1/317 + 23/883 + 9/480 + 4/591 + 2/762, 3/259 + 1/500, 9/102 + 20/158 + 22/548 + 19/784 + 5/87 + 18/252, 22/795, 7/44 + 8/266, 10/78 ?

# 2/896 + 16/651, 1/308 + 7/42 + 15/641, 3/210 + 3/59, 17/651 + 2/286 + 21/414 + 4/12 + 22/697 + 9/238, 2/671 + 1/758, 22/393 + 2/12 + 22/434, 22/934 + 18/859, 17/147 + 15/602 + 1/183
# 20/146 + 22/727, 8/74 + 3/264 + 6/938 + 10/367, 3/251 + 14/147, 1/56 + 15/118 + 15/943 + 1/336 + 20/422, 22/833, 22/891 + 24/424, 8/54 ?

# 2/524 + 20/455, 18/857 + 2/87 + 18/373 + 14/686, 21/184 + 23/375, 20/948 + 8/39 + 23/368 + 5/462 + 27/378, 2/994 + 1/665, 23/752 + 3/10 + 19/248, 1/116 + 14/148, 19/492 + 10/486 + 7/449
# 2/903 + 15/979, 21/175 + 22/692 + 18/314 + 8/267, 3/258 + 1/524, 18/950 + 21/452 + 9/264 + 18/809 + 6/74 + 18/251, 6/8702199, 1/109 + 10/725, 8/823 ?

# 17/704 + 4/85, 6/7253130 + 2/599 + 20/296 + 17/166 + 4/471 + 10/408 + 21/996 + 14/116, 4/1251199 + 22/174 + 16/185 + 2/330, 5/45 + 21/662 + 6/566 + 8/646, 17/150 + 2/17 + 20/946 + 5/897 + ' + 19/257, 12/418, 4/2735886277 + 9/595 + 9/633 + 9/281 + 1/0 + 9/207 ;
# 20/796 + 4/257 + 21/998, 12/955 + 19/507 + 16/367 + 22/922 + 22/647 + 8/141 + 15/474, 2/265 + 17/934 + 18/512 + 17/711, 4/6882698185 + 21/928, 1/421 + 1/159 + 6/929 + 6/287 + 8/997, 20/242 + 15/260 + 5/90 + 9/68, 4/375 + 13/371 + 1/634 + 20/415 ;

# 12/909, 6/3096154602 + 12/428 + 4/2849747819 + 1/815, 2/229 + 17/745 + 6/946 + 17/212 + 8/994, 4/887 + 13/770 + 9/528 + 14/442 + 4/12 + 20/850, 16/158 + 13/704 + 2/957 + 16/511, 15/931 + 3/273, 15/560 + 9/656 + 1/830
# 2/427 + 24/187 + 9/277 + ' + 1/68, 2/460 + 8/306 + 4/501, 1/344 + 16/527 + 15/204, 17/159 + 6/827 + 10/34 + 24/845 + 4/358, 11/633 + 8/605 + 9/657, 17/347, 7/467, 26/783 !"""
