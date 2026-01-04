import collections
import re

import decrypter

text = decrypter.decrypter(89, False)(lambda x: x).decrypt_chapter()
instructions = text.split("\n\n")[15:-12]  # Trim off introduction and "Stop writing."

words = ["fuck", "you"]


def pop_prefix(regex: str, s: str) -> tuple[str, str] | None:
    if match := re.match(f"^{regex}", s):
        group = match.group()
        return group, s[len(group) :].lstrip()

    return None


def pop_word(s: str) -> tuple[str, str] | None:
    if match := pop_prefix('".+?"', rest):
        return match[0].strip('"'), match[1]
    elif match := pop_prefix("(a )?comma", rest):
        return ",", match[1]
    elif match := pop_prefix("(a )?colon", rest):
        return ":", match[1]
    elif match := pop_prefix("(a )?period", rest):
        return ".", match[1]
    elif match := pop_prefix("(a )?line break", rest):
        return "\n", match[1]
    elif match := pop_prefix("(a )?question mark", rest):
        return "?", match[1]
    elif match := pop_prefix("(a )?dash", rest):
        return "-", match[1]
    elif match := pop_prefix("(a )?quotation mark", rest):
        return '"', match[1]
    elif match := pop_prefix("(a )?semicolon", rest):
        return ";", match[1]
    elif match := pop_prefix("(a )?close parenthesis", rest):
        return ")", match[1]
    elif match := pop_prefix("(an )?open parenthesis", rest):
        return "(", match[1]
    elif match := pop_prefix("(an )?exclamation mark", rest):
        return "!", match[1]
    else:
        # raise ValueError(f"Cannot pop word {s=}")
        return None


def pop_position(s: str) -> tuple[int, str]:
    if match := pop_prefix("the first", rest):
        return 1, match[1]
    elif match := pop_prefix("the second", rest):
        return 2, match[1]
    elif match := pop_prefix("the fifth", rest):
        return 5, match[1]
    else:
        raise ValueError(f"Cannot pop position {s=}")


for instruction in instructions:
    try:
        rest = instruction
        if match := pop_prefix("Write ", rest):
            rest = match[1]
            to_insert, rest = pop_word(rest)  # ty:ignore[not-iterable]

            if match := pop_prefix("before ", rest):
                rest = match[1]
                if word_first := pop_word(rest):
                    before, rest = word_first
                else:
                    position_before, rest = pop_position(rest)
                    before, rest = pop_word(rest)  # ty:ignore[not-iterable]
                assert rest == "."

            elif match := pop_prefix("after ", rest):
                rest = match[1]
                if word_first := pop_word(rest):
                    after, rest = word_first
                else:
                    position_after, rest = pop_position(rest)
                    after, rest = pop_word(rest)  # ty:ignore[not-iterable]
                assert rest == "."

            elif match := pop_prefix("between ", rest):
                pass
            else:
                raise ValueError(f"{rest=}")

        elif match := pop_prefix("On second thought, delete ", rest):
            rest = match[1]

        else:
            raise ValueError(f"{rest=}")
    except (ValueError, TypeError) as e:
        print(f"Cannot parse {instruction=}\n{e}")
