import decrypter


@decrypter.decrypter(chapter=68)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(
        cipher,
        "MildredFourteenChignonVoileSingingLeoraThirteenUpdoSateenMagicElsayTenBobCottonDancingTaddyTwelveBraidsLinenMemoryGillianNinePonytailRayonMathematicsAndaElevenMulletPolyesterRunning",
    )


# import itertools

# dec = decrypter.decrypter(chapter=68)(lambda x: x)
# ciphertext = dec.decrypt_one_chapter()[:500]


# names = ["Anda", "Taddy", "Gillian", "Leora", "Elsay", "Mildred"]
# ages = ["Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen"]
# hairstyles = ["Braids", "Bob", "Chignon", "Mullet", "Ponytail", "Updo"]
# pajamas = ["Cotton", "Linen", "Polyester", "Rayon", "Sateen", "Voile"]
# talents = ["Dancing", "Magic", "Mathematics", "Memory", "Running", "Singing"]

# key_length = len(
#     "AndaNineBraidsCottonDancingElsayTenBobLinenMagicGillianElevenChignonPolyesterMathematicsLeoraTwelveMulletRayonMemoryMildredThirteenPonytailSateenRunningTaddyFourteenUpdoVoileSinging"
# )

# final_key = ""

# final_names = []
# final_ages = []
# final_hairstyles = []
# final_pajamas = []
# final_talents = []


# def choose_attribute(
#     attribute_name: str, candidates: list[str], final: list[str]
# ) -> None:
#     global final_key

#     print(f"\n\n{attribute_name.capitalize()}:")
#     for i, candidate in enumerate(candidates, 1):
#         if candidate in final:
#             continue

#         print(f"\n\n{i}. {candidate}")
#         key = final_key + candidate
#         key += "X" * (key_length - len(key))
#         plain = decrypter.vigenere_cipher(ciphertext, key)
#         print(plain)

#     candidate_index = int(input(f"Choose {attribute_name} for bunk {bunk}: "))
#     choice = candidates[candidate_index - 1]
#     print(f"Adding {choice} to bunk {bunk}")
#     final.append(choice)
#     final_key += choice


# for bunk in range(1, 7):
#     print(f"\n\n--- Bunk {bunk} ---")
#     choose_attribute("name", names, final_names)
#     choose_attribute("age", ages, final_ages)
#     choose_attribute("hairstyle", hairstyles, final_hairstyles)
#     choose_attribute("pajama", pajamas, final_pajamas)
#     choose_attribute("talent", talents, final_talents)

# print(final_key)
