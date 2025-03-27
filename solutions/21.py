import dateutil
import decrypter


text = """
Dear Hugh,

Today is yet another fine, cold, clear, bright day that finds me not
much in the mood for writing, unfortunately.

Nevertheless, if you need reminding of the way I feel about you, all
you have to do is review my letters! Take a look at the ones dated
January 8, February 5, May 19, March 14, August 2, October 17,
February 19, April 19, July 23, June 12, September 19, June 18, May
4, April 5, November 17, August 17, February 29, and October 19, in
particular.

Dated now this December 2.

With love as ever,

Your Suze
"""

dates = [
    "January 8",
    "February 5",
    "May 19",
    "March 14",
    "August 2",
    "October 17",
    "February 19",
    "April 19",
    "July 23",
    "June 12",
    "September 19",
    "June 18",
    "May 4",
    "April 5",
    "November 17",
    "August 17",
    "February 29",
    "October 19",
]

letters = "".join(c for c in text if c.isalpha())
key = "".join(
    letters[dateutil.parser.parse(f"{date} 2024").timetuple().tm_yday - 1]
    for date in dates
)


@decrypter.decrypter(chapter=21)
def decrypt(cipher: str) -> str:
    return decrypter.string_shuffle(cipher, key)
