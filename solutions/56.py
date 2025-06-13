import decrypter
import itertools


def get_path(s):
    return [(ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s))]


target_path = [ord(c) - ord("a") + 1 for c in "cumin"]
assert get_path("knives") == target_path


@decrypter.decrypter(chapter=56)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(cipher, "knivessink")


# import collections


# def get_normalised_three_grams(text: str) -> collections.Counter:
#     three_grams = collections.Counter(
#         text[i] + text[i + 1] + text[i + 2] for i in range(0, len(text) - 2, 3)
#     )

#     total = sum(three_grams.values())
#     normalized = collections.Counter()
#     for three_gram in three_grams:
#         normalized[three_gram] = three_grams[three_gram] / total
#     return normalized


# def evaluate_fitness(
#     three_grams: collections.Counter,
#     reference_three_grams: collections.Counter,
# ) -> float:
#     distance = 0
#     all_grams = set(three_grams.keys()) | set(reference_three_grams.keys())

#     for gram in all_grams:
#         freq1 = three_grams.get(gram, 0)
#         freq2 = reference_three_grams.get(gram, 0)
#         distance += abs(freq1 - freq2)

#     return distance


# def encrypt89(plaintext: str, key: str) -> str:
#     """Encrypt using the reverse of decrypter.vigenere_cipher"""
#     if not key:
#         return plaintext

#     alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
#     c_to_index = {c: i for i, c in enumerate(alphabet)}

#     plain_nums = [c_to_index[c] for c in plaintext]
#     key_nums = [c_to_index[c] for c in key]

#     n = len(alphabet)
#     result = []
#     for a, b in zip(plain_nums, itertools.cycle(key_nums)):
#         result.append(alphabet[(a + b) % n])

#     return "".join(result)


# def calculate_ic_extended(text: str) -> float:
#     """Calculate Index of Coincidence for extended alphabet"""
#     n = len(text)
#     if n <= 1:
#         return 0

#     freq = collections.Counter(text)
#     ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1))
#     return ic


# def find_key_length_extended(ciphertext: str, max_length: int = 20) -> int:
#     """Find key length using Index of Coincidence for extended alphabet"""
#     best_length = 1
#     best_avg_ic = 0

#     for length in range(1, min(max_length + 1, len(ciphertext) // 2)):
#         subsequences = [""] * length
#         for i, char in enumerate(ciphertext):
#             subsequences[i % length] += char

#         # Calculate average IC for all subsequences
#         total_ic = sum(
#             calculate_ic_extended(subseq) for subseq in subsequences if len(subseq) > 1
#         )
#         avg_ic = total_ic / length if length > 0 else 0

#         if avg_ic > best_avg_ic:
#             best_avg_ic = avg_ic
#             best_length = length

#     return best_length


# def find_best_key_char(
#     ciphertext: str, reference_trigrams: collections.Counter
# ) -> tuple[str, float]:
#     """Find the best lowercase key character for a given cipher subsequence"""
#     alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
#     lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

#     best_char = "a"
#     best_fitness = float("inf")

#     for key_char in lowercase_letters:
#         # Decrypt using this key character
#         decrypted = decrypter.vigenere_cipher(ciphertext, key_char)

#         if len(decrypted) >= 3:
#             trigrams = get_normalised_three_grams(decrypted)
#             fitness = evaluate_fitness(trigrams, reference_trigrams)

#             if fitness < best_fitness:
#                 best_fitness = fitness
#                 best_char = key_char

#     return best_char, best_fitness


# def break_extended_vigenere(
#     ciphertext: str, reference_text: str, max_key_length: int = 20
# ) -> tuple[str, str]:
#     """
#     Break the extended Vigenère cipher using trigram frequency analysis

#     Args:
#         ciphertext: The encrypted text
#         reference_text: Sample text in the same language for frequency analysis
#         max_key_length: Maximum key length to test

#     Returns:
#         Tuple of (decrypted_text, key)
#     """
#     # Get reference trigrams
#     reference_trigrams = get_normalised_three_grams(reference_text)

#     # Find key length
#     key_length = find_key_length_extended(ciphertext, max_key_length)
#     print(f"Estimated key length: {key_length}")

#     # Break each position of the key
#     key = []
#     for pos in range(key_length):
#         # Extract characters at this key position
#         subseq = "".join(ciphertext[i] for i in range(pos, len(ciphertext), key_length))

#         if len(subseq) > 0:
#             # Find best key character for this position
#             key_char, fitness = find_best_key_char(subseq, reference_trigrams)
#             key.append(key_char)
#             print(f"Position {pos + 1}: '{key_char}' (fitness: {fitness:.4f})")

#     key_str = "".join(key)

#     # Decrypt the full text
#     decrypted = decrypter.vigenere_cipher(ciphertext, key_str)

#     return decrypted, key_str


# def try_multiple_key_lengths(
#     ciphertext: str, reference_text: str, max_length: int = 15
# ) -> list[tuple[str, str, float]]:
#     """
#     Try multiple key lengths and return results sorted by fitness
#     """
#     reference_trigrams = get_normalised_three_grams(reference_text)
#     results = []

#     for length in range(1, min(max_length + 1, len(ciphertext) // 3)):
#         print(f"\nTrying key length {length}...")

#         key = []
#         total_fitness = 0

#         for pos in range(length):
#             subseq = "".join(ciphertext[i] for i in range(pos, len(ciphertext), length))

#             if len(subseq) > 0:
#                 key_char, fitness = find_best_key_char(subseq, reference_trigrams)
#                 key.append(key_char)
#                 total_fitness += fitness

#         key_str = "".join(key)
#         decrypted = decrypter.vigenere_cipher(ciphertext, key_str)

#         # Calculate overall fitness
#         if len(decrypted) >= 3:
#             decrypted_trigrams = get_normalised_three_grams(decrypted)
#             overall_fitness = evaluate_fitness(decrypted_trigrams, reference_trigrams)
#         else:
#             overall_fitness = float("inf")

#         results.append((decrypted, key_str, overall_fitness))
#         print(f"Key: '{key_str}', Fitness: {overall_fitness:.4f}")
#         print(f"Preview: {decrypted[:100]}...")

#     # Sort by fitness (lower is better)
#     results.sort(key=lambda x: x[2])
#     return results


# reference_text = []
# for chapter in range(55):
#     with open(f"data/{chapter:02}.chp") as f:
#         reference_text.append(f.read())
# reference_text = "".join(reference_text)

# d = decrypter.decrypter(chapter=56)(lambda x: x)
# ciphertext = d.decrypt_one_chapter()[:500]
# result = try_multiple_key_lengths(ciphertext, reference_text, 10)
