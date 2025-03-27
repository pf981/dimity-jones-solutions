import decrypter


# import random

# cogwheels = ["ASWHIRST", "WILL_LIV", "TAKE_TOO", "SHE_EASI", "LY_ARTHE"]
# WHIR-L_LI-KE_T-HE_E-ARTH

# for _ in range(5000):
#     for s in cogwheels:
#         i = random.randint(1, 8)
#         print((s + s)[i:i+4], end="")
#     print()


@decrypter.decrypter(chapter=15)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, "WHIRL LIKE THE EARTH")
