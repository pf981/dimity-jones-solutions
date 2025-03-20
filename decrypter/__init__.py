from typing import Callable
from pathlib import Path


class Decrypter:
    def __init__(self, func: Callable[[str], str], chapter: int, path: str):
        self.func = func
        self.chapter = chapter
        self.prev_chapter = max(chapter - 1, 0)
        self.path = Path(path)

    def __call__(self, cipher: str) -> str:
        return self._decrypt(cipher)

    def decrypt_chapter(self) -> str:
        cipher = self._read_file(f"{self.prev_chapter:02}.txt")
        if self.chapter:
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
            with open(path, "w") as f:
                f.write(output)
        except FileNotFoundError as e:
            raise e
        return path


def decrypter(
    chapter: int, path: str = "./data/"
) -> Callable[[Callable[[str], str]], Decrypter]:
    def decorator(func: Callable[[str], str]) -> Decrypter:
        return Decrypter(func, chapter, path)

    return decorator
