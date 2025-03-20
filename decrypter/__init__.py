from typing import Callable
from pathlib import Path


class Decrypter:
    def __init__(self, func: Callable[[str], str], chapter: int, path: str):
        self.func = func
        self.chapter = chapter
        self.path = Path(path)

    def __call__(self, cipher: str) -> str:
        return self._decrypt(cipher)

    def decrypt_chapter(self) -> str:
        cipher = self._read_file(f"{self.chapter:02}.txt").split("#####", 1)[1]
        return self._decrypt(cipher)

    def decrypt_one_chapter(self) -> str:
        return self.decrypt_chapter().split("#####", 1)[0]

    def decrypt_example(self, example: int) -> str:
        cipher = self._read_file(f"{self.chapter:02}.ex{example}")
        return self._decrypt(cipher)

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


def decrypter(
    chapter: int, path: str = "./data/"
) -> Callable[[Callable[[str], str]], Decrypter]:
    def decorator(func: Callable[[str], str]) -> Decrypter:
        return Decrypter(func, chapter, path)

    return decorator
