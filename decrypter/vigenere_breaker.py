import itertools
import collections
from typing import Dict, List, Tuple

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'\"-()[]{}|+=%/\\*#$_ \n"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz "


def position_sample(text: str, positions: Tuple[int, ...], block_size: int) -> str:
    """Extract characters at specific positions from each block."""
    if block_size <= max(positions):
        raise ValueError("Block size must be larger than all positions")

    result = []
    for block in itertools.batched(text, block_size):
        if len(block) != block_size:
            break
        result.append("".join(block[i] for i in positions))

    return "".join(result)


def get_normalized_ngrams(text: str, block_sizes: List[int] = [3]) -> Dict[str, float]:
    """Get normalized n-gram frequencies for given block sizes."""
    normalized = {}

    for block_size in block_sizes:
        frequencies = collections.Counter(
            text[i : i + block_size]
            for i in range(0, len(text) - block_size + 1, block_size)
        )

        total = sum(frequencies.values())
        if total > 0:
            for ngram, count in frequencies.items():
                normalized[ngram] = count / total

    return normalized


def evaluate_fitness(
    freqs: Dict[str, float], reference_freqs: Dict[str, float]
) -> float:
    """Calculate fitness score using Manhattan distance between frequency distributions."""
    distance = 0
    all_grams = set(freqs.keys()) | set(reference_freqs.keys())

    for gram in all_grams:
        freq1 = freqs.get(gram, 0)
        freq2 = reference_freqs.get(gram, 0)
        distance += abs(freq1 - freq2)

    return distance


def calculate_index_of_coincidence(text: str) -> float:
    """Calculate Index of Coincidence for the given text."""
    n = len(text)
    if n <= 1:
        return 0

    freq = collections.Counter(text)
    ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1))
    return ic


def find_key_length(ciphertext: str, max_length: int = 20) -> int:
    """Find most likely key length using Index of Coincidence."""
    best_length = 1
    best_avg_ic = 0

    for length in range(1, min(max_length + 1, len(ciphertext) // 2)):
        # Use position_sample to extract subsequences
        subsequences = []
        for pos in range(length):
            subseq = position_sample(ciphertext, (pos,), length)
            if len(subseq) > 1:
                subsequences.append(subseq)

        if not subsequences:
            continue

        total_ic = sum(
            calculate_index_of_coincidence(subseq) for subseq in subsequences
        )
        avg_ic = total_ic / len(subsequences)

        if avg_ic > best_avg_ic:
            best_avg_ic = avg_ic
            best_length = length

    return best_length


def find_best_key_char(
    ciphertext: str,
    reference_trigrams: Dict[str, float],
    decrypter_func,
    key_chars: str = LOWERCASE_LETTERS,
) -> Tuple[str, float]:
    """Find the best key character for a cipher subsequence."""
    best_char = "a"
    best_fitness = float("inf")

    for key_char in key_chars:
        try:
            decrypted = decrypter_func(ciphertext, key_char)

            if len(decrypted) >= 3:
                trigrams = get_normalized_ngrams(decrypted, [3])
                fitness = evaluate_fitness(trigrams, reference_trigrams)

                if fitness < best_fitness:
                    best_fitness = fitness
                    best_char = key_char
        except Exception:
            continue

    return best_char, best_fitness


def get_reference_frequencies_by_position(
    reference_text: str, key_length: int, decrypter_func
) -> List[Dict[str, float]]:
    """Get reference trigram frequencies for each key position by trying all possible keys."""
    position_references = []

    for pos in range(key_length):
        # Extract subsequence at this position
        subseq = position_sample(reference_text, (pos,), key_length)

        if len(subseq) >= 3:
            # For reference text, we assume it's already decrypted, so just get trigrams directly
            trigrams = get_normalized_ngrams(subseq, [3])
            position_references.append(trigrams)
        else:
            position_references.append({})

    return position_references


def break_vigenere_cipher(
    ciphertext: str,
    reference_text: str,
    decrypter_func,
    max_key_length: int = 20,
    key_chars: str = LOWERCASE_LETTERS,
    verbose: bool = True,
) -> Tuple[str, str]:
    """
    Break the Vigenère cipher using trigram frequency analysis.

    Args:
        ciphertext: The encrypted text
        reference_text: Sample text for frequency analysis
        decrypter_func: Function that takes (text, key) and returns decrypted text
        max_key_length: Maximum key length to test
        verbose: Whether to print progress information

    Returns:
        Tuple of (decrypted_text, key)
    """
    # Find key length
    key_length = find_key_length(ciphertext, max_key_length)
    if verbose:
        print(f"Estimated key length: {key_length}")

    # Get position-specific reference frequencies
    position_references = get_reference_frequencies_by_position(
        reference_text, key_length, decrypter_func
    )

    # Break each position of the key
    key = []
    for pos in range(key_length):
        # Extract characters at this key position using position_sample
        subseq = position_sample(ciphertext, (pos,), key_length)

        if len(subseq) > 0:
            # Use position-specific reference frequencies if available
            ref_trigrams = (
                position_references[pos] if pos < len(position_references) else {}
            )
            if not ref_trigrams:
                # Fallback to general trigrams
                ref_trigrams = get_normalized_ngrams(reference_text, [3])

            key_char, fitness = find_best_key_char(
                subseq, ref_trigrams, decrypter_func, key_chars
            )
            key.append(key_char)
            if verbose:
                print(f"Position {pos + 1}: '{key_char}' (fitness: {fitness:.4f})")

    key_str = "".join(key)
    decrypted = decrypter_func(ciphertext, key_str)

    return decrypted, key_str


def try_multiple_key_lengths(
    ciphertext: str,
    reference_text: str,
    decrypter_func,
    min_length: int = 1,
    max_length: int = 15,
    key_chars: str = LOWERCASE_LETTERS,
    verbose: bool = True,
) -> List[Tuple[str, str, float]]:
    """
    Try multiple key lengths and return results sorted by fitness.

    Returns:
        List of (decrypted_text, key, fitness_score) tuples, sorted by fitness
    """
    results = []

    for length in range(min_length, min(max_length + 1, len(ciphertext) // 3)):
        if verbose:
            print(f"\nTrying key length {length}...")

        # Get position-specific reference frequencies for this key length
        position_references = get_reference_frequencies_by_position(
            reference_text, length, decrypter_func
        )

        key = []
        for pos in range(length):
            # Use position_sample to extract subsequence
            subseq = position_sample(ciphertext, (pos,), length)

            if len(subseq) > 0:
                # Use position-specific reference frequencies if available
                ref_trigrams = (
                    position_references[pos] if pos < len(position_references) else {}
                )
                if not ref_trigrams:
                    # Fallback to general trigrams
                    ref_trigrams = get_normalized_ngrams(reference_text, [3])

                key_char, _ = find_best_key_char(
                    subseq, ref_trigrams, decrypter_func, key_chars
                )
                key.append(key_char)

        key_str = "".join(key)

        try:
            decrypted = decrypter_func(ciphertext, key_str)

            # Calculate overall fitness using general reference trigrams
            if len(decrypted) >= 3:
                decrypted_trigrams = get_normalized_ngrams(decrypted, [3])
                reference_trigrams = get_normalized_ngrams(reference_text, [3])
                overall_fitness = evaluate_fitness(
                    decrypted_trigrams, reference_trigrams
                )
            else:
                overall_fitness = float("inf")

            results.append((decrypted, key_str, overall_fitness))

            if verbose:
                print(f"Key: '{key_str}', Fitness: {overall_fitness:.4f}")
                print(f"Preview: {decrypted[:100]}...")

        except Exception as e:
            if verbose:
                print(f"Failed to decrypt with key '{key_str}': {e}")
            continue

    # Sort by fitness (lower is better)
    results.sort(key=lambda x: x[2])
    return results
