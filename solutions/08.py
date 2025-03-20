import decrypter
import itertools


def chunk_shuffle(cipher: str, sequence: list[int], chunk_size: int | None = None):
    if chunk_size is None:
        chunk_size = max(sequence)

    result = []
    for buffer in itertools.batched(cipher, chunk_size):
        if len(buffer) < chunk_size:
            result.extend(buffer)
            break
        for i in sequence:
            result.append(buffer[i - 1])

    return "".join(result)


nums = [
    2095,
    845,
    8673,
    3547,
    8478,
    8780,
    4695,
    1987,
    3114,
    2335,
    1461,
    2698,
    6850,
    4556,
    6976,
    3021,
    5441,
    5657,
    7737,
    5780,
]

for w in range(1, len(nums) + 1):
    for subset in itertools.combinations(nums, w):
        if sum(subset) == 29290:
            break
    else:
        continue
    break

sequence = [nums.index(num) + 1 for num in sorted(subset)]


@decrypter.decrypter(chapter=8)
def decrypt(cipher: str) -> str:
    return chunk_shuffle(cipher, sequence)
