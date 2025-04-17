import decrypter
# import hashlib
# import num2words

# for seat_num in range(1, 41):
#     word = "-".join(
#         word.capitalize() for word in num2words.num2words(seat_num).split("-")
#     )
#     key_string = f"{word} ({seat_num})."
#     print(key_string)
#     expected_hash = "eb476713d43e3dc4532895511d213f1890228323529edf69720fb50757df0758"

#     @decrypter.decrypter(chapter=46)
#     def decrypt(cipher: str) -> str:
#         return decrypter.substitution_cipher(cipher, key_string)

#     path = decrypt.write_chapter()
#     decrypt.write_one_chapter()

#     with open(path, "br") as f:
#         h = hashlib.file_digest(f, "sha256").hexdigest()
#     if h == expected_hash:
#         break


@decrypter.decrypter(chapter=46)
def decrypt(cipher: str) -> str:
    return decrypter.substitution_cipher(cipher, "Ten (10).")
