import decrypter


@decrypter.decrypter(chapter=64)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "2612400053")


# import decrypter
# from decrypter import vigenere_breaker

# reference_text = []
# for chapter in range(64):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)

# ciphertext = decrypter.decrypter(64)(lambda x: x).decrypt_one_chapter()

# result = vigenere_breaker.break_vigenere_cipher(
#     ciphertext[:1000],
#     reference_text,
#     decrypter_func=decrypter.vigenere_cipher,
#     key_chars="1234567890",
#     max_key_length=30,
#     verbose=True,
# )
