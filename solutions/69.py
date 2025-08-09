import collections
import constraint
import itertools
import re

import decrypter


text = """
Thirteen Ways of Looking At The Same Five People

1.
Five friends, Cath, Ed, Kate, Lore, and Paul,
    Hold different things, are different ages,
Wear different hats upon their heads; and all
    Prefer to read from different poets' pages.

2.
One likes above all poets Blake; one's twelve years old;
One's name is Cath; one holds a ski; one's hat is gold.

3.
One's favorite poet's Plath; another holds a kite;
One's name is Ed; one's sixty-four; one's hat is white.

4.
One's name is Kate; one's hat is red; one's twenty-one;
One holds an awl; another's best-loved poet's Donne.

5.
One has the name of Paul; one's favorite poet's Stein;
One's fifty-three; one's hat is blue; one holds a sign.

6.
One holds a rake; one's thirty-eight; one's hat is taupe;
Another's name is Lore; another likes best Pope.

7.
Two of the friends
    Collect odd odds and ends:
The one is Lore;
    The other's sixty-four.

8.
One's twenty-one; another nothing reads but Plath;
One's hat is taupe; one holds a sign; one's name is Cath.

9.
One's name is Lore; one's hat is white; one's fifty-three;
One's favorite poet's Donne; another holds a ski.

10.
One's sixty-four; one's hat is gold; one's name is Paul;
Another reads but Pope; another holds an awl.

11.
One's favorite poet's Blake; another's name is Kate;
One holds a kite; one's hat is blue; one's thirty-eight.

12.
One's age is twelve; one holds a rake; one's hat is red;
Another favors Stein; another's name is Ed.

13.
Two of the five
    Can't swim, don't float, won't dive:
The one loves Blake;
    The other holds a rake.
"""


names = ["Cath", "Ed", "Kate", "Lore", "Paul"]
holds = ["Ski", "Kite", "Awl", "Sign", "Rake"]
ages = [
    "Twelve",
    "Twenty-One",
    "Thirty-Eight",
    "Fifty-Three",
    "Sixty-Four",
]
hats = ["Gold", "White", "Red", "Blue", "Taupe"]
poets = ["Blake", "Plath", "Donne", "Stein", "Pope"]

words = list(itertools.chain(names, holds, ages, hats, poets))

clues = []
for clue_text in text.lower().split("\n\n")[1:]:
    clue = []
    clue_words = re.findall(r"[a-z-]+", clue_text)

    for word in words:
        if word.lower() in clue_words:
            clue.append(word)
    clues.append(clue)


problem = constraint.Problem()

# Each attribute is assigned to one name
for word in words:
    if word in names:
        continue
    problem.addVariable(word, names)

# Each name attribute is assigned to its corresponding name
for name in names:
    problem.addVariable(name, [name])

# Names can't have more than one attribute from the same attribute group
problem.addConstraint(constraint.AllDifferentConstraint(), names)
problem.addConstraint(constraint.AllDifferentConstraint(), holds)
problem.addConstraint(constraint.AllDifferentConstraint(), ages)
problem.addConstraint(constraint.AllDifferentConstraint(), hats)
problem.addConstraint(constraint.AllDifferentConstraint(), poets)

for clue in clues:
    problem.addConstraint(constraint.AllDifferentConstraint(), clue)

solution = problem.getSolution()
result = collections.defaultdict(lambda: [None, None, None, None])

for attr, name in solution.items():
    for i, words in enumerate([holds, ages, hats, poets]):
        if attr in words:
            result[name][i] = attr
            break

key = ""
for name in names:
    key += "".join(result[name])


@decrypter.decrypter(chapter=69)
def decrypt(cipher: str) -> str:
    return decrypter.vigenere_cipher(
        cipher,
        "RakeSixty-FourBlueDonneAwlFifty-ThreeTaupeBlakeSignTwelveWhitePopeKiteTwenty-OneGoldSteinSkiThirty-EightRedPlath",
    )
