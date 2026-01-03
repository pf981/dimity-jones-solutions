import itertools
from typing import Callable
from pathlib import Path


class Decrypter:
    def __init__(
        self,
        func: Callable[[str], str],
        chapter: int,
        has_chapter_separator: bool,
        path: str,
    ):
        self.func = func
        self.chapter = chapter
        self.prev_chapter = max(chapter - 1, 0)
        self.has_chapter_separator = has_chapter_separator
        self.path = Path(path)
        self.input_file = f"{self.prev_chapter:02}.txt"

    def __call__(self, cipher: str) -> str:
        return self._decrypt(cipher)

    def decrypt_chapter(self) -> str:
        cipher = self._read_file(self.input_file)
        if self.has_chapter_separator:
            cipher = cipher.split("#####", 1)[1]
        return self._decrypt(cipher)

    def decrypt_one_chapter(self) -> str:
        return self.decrypt_chapter().split("#####", 1)[0]

    def decrypt_example(self, example: int) -> str:
        cipher = self._read_file(f"{self.prev_chapter:02}.ex{example}")
        return self._decrypt(cipher)

    def write_chapter(self) -> Path:
        output = self.decrypt_chapter()
        return self._write_file(f"{self.chapter:02}.txt", output)

    def write_one_chapter(self) -> Path:
        output = self.decrypt_one_chapter()
        return self._write_file(f"{self.chapter:02}.chp", output)

    def write_example(self, example: int) -> Path:
        output = self.decrypt_example(example)
        return self._write_file(f"{self.chapter:02}.ex{example}", output)

    def _decrypt(self, cipher: str) -> str:
        return self.func(cipher)

    def _read_file(self, file: str) -> str:
        path = self.path / file
        try:
            with open(path) as f:
                cipher = f.read()
        except FileNotFoundError as e:
            # print(f"File not found: {path}")
            raise e
        return cipher

    def _write_file(self, file: str, output: str) -> Path:
        path = self.path / file
        try:
            # newline="" required to prevent windows changing
            # line endings and the hashes not matching
            with open(path, "w", newline="") as f:
                f.write(output)
        except FileNotFoundError as e:
            raise e
        return path


def decrypter(
    chapter: int, has_chapter_separator: bool = True, path: str = "./data/"
) -> Callable[[Callable[[str], str]], Decrypter]:
    def decorator(func: Callable[[str], str]) -> Decrypter:
        return Decrypter(func, chapter, has_chapter_separator, path)

    return decorator


def sequence_shuffle(cipher: str, sequence: list[int], chunk_size: int | None = None):
    if chunk_size is None:
        chunk_size = max(sequence)

    result: list[str] = []
    for buffer in itertools.batched(cipher, chunk_size):
        if len(buffer) < chunk_size:
            result.extend(buffer)
            break
        for i in sequence:
            result.append(buffer[i - 1])

    return "".join(result)


def string_shuffle(cipher: str, key_string: str):
    return sequence_shuffle(cipher, _get_alphabetical_transposition_key(key_string))


def _get_alphabetical_transposition_key(s: str):
    chars = [c.upper() for c in s if c.isalpha() or c.isdigit()]
    ranks = sorted(enumerate(chars), key=lambda pair: pair[1])

    key = [0] * len(chars)
    for i, (j, _) in enumerate(ranks, 1):
        key[j] = i

    return key


def substitution_cipher(cipher: str, key_string: str):
    alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
    keys = list(dict.fromkeys(key_string))
    keys += [c for c in alphabet if c not in keys]
    assert len(keys) == len(alphabet)
    m = {}
    for a, b in zip(keys, alphabet):
        m[a] = b

    return "".join(m.get(c, c) for c in cipher)


def vigenere_cipher(cipher: str, key_string: str) -> str:
    s1, s2 = cipher, key_string
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    if not s2:
        return s1

    alphabet = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!:;'"-()[]{}|+=%/\\*#$_ \n"""
    c_to_index = {c: i for i, c in enumerate(alphabet)}
    nums1, nums2 = [[c_to_index[c] for c in s] for s in [s1, s2]]

    n = len(alphabet)
    result = []
    for a, b in zip(nums1, itertools.cycle(nums2)):
        result.append(alphabet[(a - b) % n])

    return "".join(result)
