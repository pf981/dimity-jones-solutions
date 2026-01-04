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
    elif match := pop_prefix("(a |the )?comma", rest):
        return ",", match[1]
    elif match := pop_prefix("(a |the )?colon", rest):
        return ":", match[1]
    elif match := pop_prefix("(a |the )?period", rest):
        return ".", match[1]
    elif match := pop_prefix("(a |the )?line break", rest):
        return "\n", match[1]
    elif match := pop_prefix("(a |the )?question mark", rest):
        return "?", match[1]
    elif match := pop_prefix("(a |the )?dash", rest):
        return "-", match[1]
    elif match := pop_prefix("(a |the )?quotation mark", rest):
        return '"', match[1]
    elif match := pop_prefix("(a |the )?semicolon", rest):
        return ";", match[1]
    elif match := pop_prefix("(a |the )?close parenthesis", rest):
        return ")", match[1]
    elif match := pop_prefix("(an |the )?open parenthesis", rest):
        return "(", match[1]
    elif match := pop_prefix("(an |the )?exclamation mark", rest):
        return "!", match[1]
    else:
        # raise ValueError(f"Cannot pop word {s=}")
        return None


def ordinal_words_upto(n: int) -> list[str]:
    ones = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    ord_exceptions = {
        "one": "first",
        "two": "second",
        "three": "third",
        "five": "fifth",
        "eight": "eighth",
        "nine": "ninth",
        "twelve": "twelfth",
    }

    def cardinal(num: int) -> str:
        if num == 0:
            return ""
        if num < 20:
            return ones[num]
        if num < 100:
            t, r = divmod(num, 10)
            base = tens[t * 10]
            return base if r == 0 else f"{base}-{ones[r]}"
        h, r = divmod(num, 100)
        base = f"{ones[h]} hundred"
        return base if r == 0 else f"{base} and {cardinal(r)}"

    def ordinal(num: int) -> str:
        if num <= 19:
            return ord_exceptions.get(ones[num], ones[num] + "th")

        if num < 100:
            if num % 10 == 0:
                tens_ordinals = {
                    20: "twentieth",
                    30: "thirtieth",
                    40: "fortieth",
                    50: "fiftieth",
                    60: "sixtieth",
                    70: "seventieth",
                    80: "eightieth",
                    90: "ninetieth",
                }
                return tens_ordinals[num]
            head = cardinal(num - num % 10)
            tail = ordinal(num % 10)
            return f"{head}-{tail}"

        if num % 100 == 0:
            return cardinal(num) + "th"

        return f"{cardinal(num - num % 100)} and {ordinal(num % 100)}"

    return [ordinal(i) for i in range(1, n + 1)]


ordinals = ordinal_words_upto(600)


def pop_position(s: str) -> tuple[int, str]:
    for i, prefix in enumerate(ordinals):
        if match := pop_prefix(f"the {prefix}", rest):
            return i, match[1]
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
                rest = match[1]
                if word_first := pop_word(rest):
                    before, rest = word_first
                    if before == "the period":
                        print("!")
                else:
                    position_before, rest = pop_position(rest)
                    before, rest = pop_word(rest)  # ty:ignore[not-iterable]

                _, rest = pop_prefix("and ", rest)  # ty:ignore[not-iterable]

                # After
                if word_first := pop_word(rest):
                    before, rest = word_first
                else:
                    position_after, rest = pop_position(rest)
                    after, rest = pop_word(rest)  # ty:ignore[not-iterable]

                assert rest == "."
            else:
                raise ValueError(f"{rest=}")

        elif match := pop_prefix("On second thought, delete ", rest):
            rest = match[1]

        else:
            raise ValueError(f"{rest=}")
    except (AssertionError, TypeError, ValueError) as e:
        print(f"Cannot parse {instruction=}\n{e}")
        break
